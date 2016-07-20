import unittest
from bespoken import *
from behavior import *

class TestBehavior(unittest.TestCase):

  @classmethod
  def setUpClass(self):

    self.behavior = Behavior()
    self.tokenizer = Bespokenize()

    self.test_string = "The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal."
    self.tokenizer.parse_phrase(self.test_string)

  def test_module_separate_tokenize_list_into_sentence_lists_if_multiple(self):
    self.assertIsInstance(self.sentences_list[0], list)

  def test_module_assign_behavior_to_punctuation_in_one_sentence(self):
    self.assertEqual(self.test_parsed_sentence[-1], punc)
    self.assertTrue(self.excited_behaviors.__contains__('!'))
    self.assertEqual(self.sentence_behavior_list[-1], 'excited')

  def test_module_assign_behavior_to_keywords_in_one_sentence(self):
    self.assertIsInstance(self.test_parsed_sentence.keywords, list)
    self.assertTrue(self.endearment_behaviors.__contains__('love'))
    self.assertEqual(self.sentence_behavior_list[-1], 'endearment')

  def test_module_assign_numeric_value(self):
    self.assertIsInstance(self.sentence_behavior_list, list)
    self.assertIsInstance(self.behavior_number[0], dict)
    self.assertTrue(0 < self.behavior_percentage[0] <= 1)

if __name__ == '__main__':
  unittest.main()

