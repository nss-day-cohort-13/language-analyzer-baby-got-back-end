import unittest
import string
from bespoken import *
from domain import *

class TestDomainAnalysis(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.test_string = 'Oh man, I love sentences. Do you also love sentences?'
    self.domain_mod = DomainModule(self.test_string)

  def test_module_creates_list_of_lists_of_sentences(self):
    self.assertIsInstance(self.domain_mod.dom_parsed, list)
    self.assertTrue(len(self.domain_mod.dom_parsed) > 0)
    self.assertIsInstance(self.domain_mod.dom_parsed[0], list)

  def test_module_creates_list_of_keywords_in_sentences(self):
    self.domain_mod.find_keywords()
    self.assertEqual(self.domain_mod.keyword_list, [['man', 'love', 'sentences'], ['love', 'sentences']])

  def test_module_creates_list_of_domains_present_in_sentences(self):
    self.assertEqual(self.domain_mod.find_domains, [['people', 'preference', 'grammar'], ['preference', 'grammar']])

  def test_module_creates_dictionary_for_report(self):
    report = {
      'people': 0.20,
      'preference': 0.35,
      'grammar': 0.45
    }
    self.assertEqual(self.domain_mod.create_report, report)

if __name__ == '__main__':
  unittest.main()
