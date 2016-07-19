import unittest
from sentiment import *

class TestSentiment(unittest.TestCase):

  @classmethod
  def setUpClass(self):

    self.sentiment = Sentiment()

    self.test_pos_word_count = ["The", "man", "was", "fond", "of", "fish", ",", "he", "loved", "them", "a", "great", "deal", "."] # 4 pos words
    self.test_neg_word_count = ["The", "man", "was", "dejected", "by", "fish", "," "he", "hated", "them", "and", "thought", "they", "were", "dumb"] # 3 neg words
    self.test_weighted_more_positive = ["The", "great", "man", "was", "fond", ".", "He", "loved", "dejectged", "fish"] # pos + 2
    self.test_weighted_more_negative =  ["The", "dejected", "fish", "hated", "the", "man"] # neg 1



  def test_positive_words_present(self):
    self.assertEqual(self.sentiment.pos_sentiment(self.test_pos_word_count), 4)

  def test_negitive_words_present(self):
    self.assertEqual(self.sentiment.neg_sentiment(self.test_neg_word_count), 3)

  def test_weighted_more_positive(self):
    self.assertEqual(self.sentiment.weighted_output(self.test_weighted_more_positive), 2)

  def test_weighted_more_negitive(self):
    self.assertEqual(self.sentiment.weighted_output(self.test_weighted_more_negative), -3)

if __name__ == '__main__':
  unittest.main()