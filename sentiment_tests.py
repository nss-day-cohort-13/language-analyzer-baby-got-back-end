import unittest
import string
from bespoken import *
from sentiment import *

class TestSentiment(unittest.TestCase):

  @classmethod
  def setUpClass(self):

    self.test_string = "The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal. How would your life be different if you stopped making negative judgmental assumptions about people you encounter? Let today be the day you look for the good in everyone you meet and respect their journey."
    self.sentiment = Sentiment(self.test_string)

  def test_calculate_word_count(self):
    positive_count, negative_count, neutral_count = self.sentiment.calculate_word_count(self.sentiment.sentence_list[0])
    self.assertEqual(positive_count, 1)
    self.assertEqual(negative_count, 2)
    self.assertEqual(neutral_count, 21)

  def test_sentence_count(self):
    self.sentiment.process_sentences()
    self.assertEqual(len(self.sentiment.sentence_count), len(self.sentiment.sentence_list))
    test_count = [[1, 2, 21], [2, 1, 25], [0, 1, 16], [2, 0, 16]]
    self.assertEqual(self.sentiment.sentence_count, test_count)


  def test_module_removes_punctuation(self):
    self.assertFalse(True in [punc in self.sentiment.sentence_list for punc in string.punctuation])
    self.assertFalse(self.sentiment.sentence_list == '')

  def test_calculate_positive_percentage(self):
    self.assertEqual(self.sentiment.calculate_positive_percent(self.sentiment.sentence_list), 0.3)

  def test_calculate_negative_percentage(self):
    self.assertEqual(self.sentiment.calculate_negative_percent(self.sentiment.sentence_list), 0.2)

  def test_final_sentence_calculation(self):
    report = {
      'positive': .3,
      'negative': .2,
      'neutral': .5
    }
    self.assertEqual(self.sentiment.calculate_sentence(self.sentiment.sentence_list), report)


if __name__ == '__main__':
  unittest.main()