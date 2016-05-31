from lib.util import sentences_in_ptb, sentences_in_a_ptb_file



import unittest

class TestCase(unittest.TestCase):
    """test for ghmm.util"""
    def test_sentences_in_ptb_file(self):
        for s in sentences_in_a_ptb_file('data/test/ptb_pos_sample.pos'):
            print s


    def test_sentences_in_ptb(self):
        for s in sentences_in_ptb('data/test'):
            print s

if __name__ == "__main__":
    unittest.main()

