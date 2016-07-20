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

  def test_module_separate_tokenize_list_into_sentence_lists_if_multiple(self):
    self.assertIsInstance(self.tokenizer.sentences_list[0], list)

  def test_module_assign_behavior_to_keywords_in_one_sentence(self):
    self.assertIsInstance(self.tokenizer.sentences_list[0].keywords, list)
    self.assertTrue(self.lexicon.behaviors.inquisitive.__contains__('exploration'))
    self.assertEqual(self.behavior.sentence_behavior_list[-1], 'inquisitive')

  def test_module_assign_numeric_value(self):
    self.assertIsInstance(self.behavior.sentence_behavior_list, list)
    self.assertIsInstance(self.behavior.behavior_number[0], dict)
    self.assertTrue(0 < self.behavior.behavior_percentage[0] <= 1)

if __name__ == '__main__':
  unittest.main()

