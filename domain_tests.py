import unittest
import string
from bespoken import *
from domain import *

class TestDomainAnalysis(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.test_string = 'Oh man, I love sentences. Do you also love sentences?'
    self.domain_mod = DomainModule(self.test_string)
    self.domain_mod.find_keywords_and_domains()
    self.domain_mod.create_phrase_report()

  def test_module_creates_list_of_lists_of_sentences(self):
    self.assertIsInstance(self.domain_mod.dom_parsed, list)
    self.assertTrue(len(self.domain_mod.dom_parsed) > 0)
    self.assertIsInstance(self.domain_mod.dom_parsed[0], list)

  def test_module_creates_list_of_keywords_in_sentences(self):
    self.assertIsInstance(self.domain_mod.keyword_list, list)
    self.assertTrue(len(self.domain_mod.keyword_list[0]) > 0)
    self.assertIsInstance(self.domain_mod.keyword_list, list)
    self.assertTrue(len(self.domain_mod.keyword_list[0]) > 0)
    self.assertIsInstance(self.domain_mod.keyword_list[0][0], str)
    self.assertEqual(self.domain_mod.keyword_list, [['man', 'love', 'sentences'], ['love', 'sentences']])

  def test_module_creates_list_of_domains_present_in_sentences(self):
    self.assertIsInstance(self.domain_mod.domain_list, list)
    self.assertTrue(len(self.domain_mod.domain_list[0]) > 0)
    self.assertIsInstance(self.domain_mod.domain_list, list)
    self.assertTrue(len(self.domain_mod.domain_list[0]) > 0)
    self.assertIsInstance(self.domain_mod.domain_list[0][0], str)
    self.assertEqual(self.domain_mod.domain_list, [['people', 'preference', 'grammar'], ['preference', 'grammar']])

  def test_module_creates_phrase_report_by_sentence(self):
    report = [{'people': 2, 'preference': 1, 'grammar': 2}, {'preference': 2, 'grammar': 2}]
    self.assertEqual(self.domain_mod.phrase_report, report)

  def test_calculate_full_report_maths_correctly(self):
    report = {
      'people': .20,
      'preference': .35,
      'grammar': .45
    }
    self.assertEqual(self.domain_mod.full_report, report)

if __name__ == '__main__':
  unittest.main()
