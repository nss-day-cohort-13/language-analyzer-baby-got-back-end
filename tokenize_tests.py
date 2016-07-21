import unittest
from bespoken import *
from sentiment import *
from behavior import *
from domain import *

class TestTokenizer(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.tokenizer = Bespokenize()

    self.test_string1 = 'Oh man, I love sentences.'
    self.test_string2 = 'Oh man, I love sentences. Do you also love sentences?'

    self.test_parsed1 = ["oh", "man", ",", "i", "love", "sentences", "."]
    self.test_parsed2 = ["oh", "man", ",", "i", "love", "sentences", ".", "do", "you", "also", "love", "sentences", "?"]

    self.tkn_1 = Bespokenize()
    self.tkn_1.parse_phrase(self.test_string1)

    self.tkn_2 = Bespokenize()
    self.tkn_2.parse_phrase(self.test_string2)

  def test_tokenize_string_input_is_string(self):
    self.assertIsInstance(self.test_string1, str)
    self.assertIsInstance(self.test_string2, str)

  def test_parse_phrase_output_is_list(self):
    self.assertIsInstance(self.tokenizer.parse_phrase(self.test_string1), list)
    self.assertIsInstance(self.tokenizer.parse_phrase(self.test_string2), list)

  def test_parse_phrase_output_is_saved_as_parsed(self):
    self.assertEqual(self.tokenizer.parse_phrase(self.test_string1), self.tokenizer.parsed)
    self.assertEqual(self.tokenizer.parse_phrase(self.test_string2), self.tokenizer.parsed)

  def test_parse_phrase_output_is_parsed_and_lowercase(self):
    self.assertEqual(self.tkn_1.parsed, ["oh", "man", ",", "i", "love", "sentences", "."])
    self.assertEqual(self.tkn_2.parsed, ["oh", "man", ",", "i", "love", "sentences", ".", "do", "you", "also", "love", "sentences", "?"])

  def test_punctuation_is_filtered(self):
    self.assertEqual(self.tkn_1.filter_punctuation(), [["oh", "man", "i", "love", "sentences"]])
    self.assertEqual(self.tkn_2.filter_punctuation(), [["oh", "man", "i", "love", "sentences"], ["do", "you", "also", "love", "sentences"]])

  def test_sentences_seperated(self):
    self.assertEqual(self.tkn_1.seperate_into_sentences(), [["oh", "man", ",", "i", "love", "sentences", "."]])
    self.assertEqual(self.tkn_2.seperate_into_sentences(), [["oh", "man", ",", "i", "love", "sentences", "."], ["do", "you", "also", "love", "sentences", "?"]])

  def test_words_counted_per_sentence(self):
    self.assertEqual(self.tkn_1.word_count(), [5])
    self.assertEqual(self.tkn_2.word_count(), [5, 5])

  def test_alpha_numeric_characters(self):
    self.assertEqual(self.tkn_1.alphanum_characters(), "acehilmnostv")
    self.assertEqual(self.tkn_2.alphanum_characters(), "acdehilmnostuvy")

  def test_sentences_counted(self):
    self.assertEqual(self.tkn_1.sentence_count(), 1)
    self.assertEqual(self.tkn_2.sentence_count(), 2)

  def test_word_position(self):
    self.assertEqual(self.tkn_1.get_position('sentences'), 5)
    self.assertEqual(self.tkn_2.get_position('also'), 8)

if __name__ == '__main__':
  unittest.main()
