


class Sentence(object):
    """docstring for Sentence"""
    def __init__(self, words, tags):
        self._words_tags = zip(words, tags)
        self.words = words
        self.tags = tags
        self.length = len(words)

    def __getitem__(self, index):
        return self._words_tags[index]

    # def __repr__(self):
    #     # return self._words_tags
    #     return self._words_tags

    def __repr__(self):
        str_word_tag = [w + '\t' + t for w, t in self._words_tags]
        return '\n'.join(str_word_tag) + '\n'
