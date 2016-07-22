import unittest
from bespoken import *
from behavior import *
from lexicon import *

class TestBehavior(unittest.TestCase):

  @classmethod
  def setUpClass(self):

    self.test_string = "The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal."
    self.behavior = Behavior(self.test_string)
    self.tokenizer = Bespokenize()
    self.lexicon = lexicon
    self.behavior.find_behaviors()
    self.behavior.find_weighted_behavior_value()
    self.behavior.generate_phrase_behavior_report()
    self.behavior.print_report()

  # Done
  def test_module_iterate_parsed_sentence_for_behaviors(self):
    self.assertIsInstance(self.behavior.sentence_behaviors, list)
    self.assertIsInstance(self.behavior.sentence_behavior_list, list)
    self.assertIsInstance(self.behavior.sentence_behavior_list[0], list)
    self.assertTrue(len(self.behavior.sentence_behavior_list[0]) > 0)

  # Done
  def test_module_get_percentage_by_sentence(self):
    self.assertIsInstance(self.behavior.behavior_count, list)
    self.assertIsInstance(self.behavior.behavior_percentage_weighted, list)

  # Done
  def test_module_generating_report_logic(self):
    self.assertIsInstance(self.behavior.sentence_count_sum, float)
    self.assertIsInstance(self.behavior.phrase_averaged_behaviors, list)
    self.assertIsInstance(self.behavior.raw_report, dict)
    self.assertIsInstance(self.behavior.report, dict)

if __name__ == '__main__':
  unittest.main()

