import unittest
from bespoken import *
from behavior import *
from lexicon import *

class TestBehavior(unittest.TestCase):

  @classmethod
  def setUpClass(self):

    self.behavior = Behavior()
    self.tokenizer = Bespokenize()
    self.lexicon = Lexicon()

    self.test_string = "The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal."
    self.tokenizer.parse_phrase(self.test_string)
    self.tokenizer.sentences_list(self.tokenizer.parsed)

  def test_module_assign_behavior_to_keywords_in_one_sentence(self):
    self.assertIsInstance(self.behavior.sentence_keywords, list)
    self.assertTrue(len(self.behavior.sentence_keywords) == len(self.behavior.sentence_behaviors))
    self.assertIsInstance(self.behavior.sentence_behavior_list, list)
    self.assertIsInstance(self.behavior.sentence_behavior_list[0], list)
    self.assertTrue(len(self.behavior.sentence_behavior_list[0]) > 0)

  def test_module_sentiment_analysis_lists(self):
    self.assertIsInstance(self.behavior.behavior_modifiers, list)
    self.assertIsInstance(self.behavior.behavior_modifiers[0], list)

  def test_module_assign_numeric_value(self):
    self.assertIsInstance(self.behavior.behavior_counters[0][0], dict)
    self.assertIsInstance(self.behavior.report, dict)
    self.assertTrue(0 < self.behavior.report.values() <= 1)

if __name__ == '__main__':
  unittest.main()

