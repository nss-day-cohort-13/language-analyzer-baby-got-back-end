from lexicon import *
from bespoken import *

class DomainModule:

  def __init__(self, phrase):
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)

    self.dom_parsed = self.tokenizer.separate_into_sentences()
    self.keyword_list = list()
    self.domain_list = list()

  def find_keywords_and_domains(self):
    for li in self.dom_parsed:
      sentence_keywords = list()
      sentence_domains = list()
      for word in li:
        for domain, keys in lexicon[0]['domain'].items():
          for keyword in keys:
            if word == keyword:
              sentence_keywords.append(word)
              sentence_domains.append(domain)
      self.keyword_list.append(sentence_keywords)
      self.domain_list.append(sentence_domains)

  def find_domains(self):
    pass


  def create_report(self):
    pass
