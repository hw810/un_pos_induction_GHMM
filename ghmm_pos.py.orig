import numpy as np
from hmmlearn.hmm import GaussianHMM
import gensim
from util import *


print("preparing data...")
model = gensim.models.Word2Vec.load('data/w2v_model_v2')
word_embedding = get_embedding_from_word2vec(model, has_tag=True)
em_dim = len(word_embedding.values()[0])

X = []
X_lens = []
S = []

for s in sentences_in_ptb('data/wsj'):
    len_s = s.length
    cur_x = np.zeros((len_s, em_dim))

    for i, w in enumerate(s.words):
        cur_x[i] = word_embedding[w]
    X.append(cur_x)
    X_lens.append(len_s)
    S.append(s.words)
X = np.concatenate(X)

print("started to train HMM")
ghmm = GaussianHMM(n_components=100, covariance_type="diag", n_iter=1000).fit(X, X_lens)
