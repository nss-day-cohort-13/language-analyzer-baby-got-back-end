from lexicon import *
from bespoken import *

class DomainModule:

  def __init__(self, phrase):
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)

    self.dom_parsed = self.tokenizer.separate_into_sentences()

  def find_keywords(self):
    self.keyword_list = list()
    for li in self.dom_parsed:
      sentence_list = list()
      for word in li:
        for domain, keys in lexicon[0]['domain'].items():
          for keyword in keys:
            if word == keyword:
              sentence_list.append(word)
      self.keyword_list.append(sentence_list)

  def find_domains(self):
    pass

  def create_report(self):
    pass
