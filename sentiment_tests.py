import unittest
import string
from bespoken import *
from sentiment import *

class TestSentiment(unittest.TestCase):

  @classmethod
  def setUpClass(self):

    self.test_string = "The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal."
    self.sentiment = Sentiment(self.test_string)

  def test_calculate_sentiment(self):
    self.assertEqual(self.sentiment.calculate_sentiment)

  def test_module_removes_punctuation(self):
    self.assertFalse(True in [punc in self.sentiment.sent_parsed for punc in string.punctuation])
    self.assertFalse(self.sentiment.sent_parsed == '')

  def test_calculate_positive_percentage(self):
    self.assertEqual(self.sentiment.calculate_positive_percent(self.sentiment.sent_parsed), 0.3)

  def test_calculate_negative_percentage(self):
    self.assertEqual(self.sentiment.calculate_negative_percent(self.sentiment.sent_parsed), 0.2)

  def test_final_sentence_calculation(self):
    report = {
      'positive': .3,
      'negative': .2,
      'neutral': .5
    }
    self.assertEqual(self.sentiment.calculate_sentence(self.sentiment.sent_parsed), report)


if __name__ == '__main__':
  unittest.main()