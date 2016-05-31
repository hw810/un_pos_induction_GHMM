import gensim
from collections import defaultdict
import numpy as np
from pos_tool import *
import os


def get_embedding_from_word2vec(model, has_tag=False):
    dim = len(model.syn0[0])
    word_embedding = defaultdict(lambda: np.zeros(dim))
    if has_tag:
        # combine word with multiple tags
        for w_tag, vocab in model.vocab.items():
            ind = vocab.index
            w = w_tag.split(".")[0]
            word_embedding[w] += model.syn0[ind]
    return word_embedding


def sentences_in_a_ptb_file(fname):
    '''sentence generator for a Penn Treebank file
    '''
    words = []
    tags = []
    with open(fname) as f:
        for l in f:
            line = l.strip()
            if line == "" or line[0] == "=":
                if words and tags:
                    sent = Sentence(words, tags)
                    yield sent
                words = []
                tags = []
            else:
                if line[0] == "[" and line[-1] == "]":
                    line = line[1:-1].strip()  # remove [ ]
                # print line.split(' ')
                ls_word_tag = line.split(' ')
                for w_t in ls_word_tag:
                    if '/' in w_t:
                        w, t = w_t.split('/')[:2]  # can have alternative tags
                        words.append(w.lower().replace('.', ''))
                        tags.append(t)

        # print the last sentence
        if words and tags:
            sent = Sentence(words, tags)
            yield sent


def sentences_in_ptb(dir_name):
    for root, subFolders, files in os.walk(dir_name):
        for fname in files:
            if '.pos' not in fname:
                continue
            full_fname = os.path.join(root, fname)
            for sent in sentences_in_a_ptb_file(full_fname):
                yield sent


# if __name__ == "__main__":
    # model = gensim.models.Word2Vec.load('data/w2v_model_v2')
    # word_index = extract_word_embedding_from_model(model, has_tag=True)

