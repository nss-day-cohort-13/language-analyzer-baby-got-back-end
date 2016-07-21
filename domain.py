from lexicon import *
from bespoken import *

class DomainModule:

  def __init__(self, phrase):
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)

    self.dom_parsed = self.tokenizer.filter_punctuation()
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

  def create_phrase_report(self):
    self.phrase_report = list()
    for sentence in self.domain_list:
      sentence_report = dict()
      for keyword in sentence:
        if keyword in sentence_report.keys():
          sentence_report[keyword] += 1
        else:
          sentence_report[keyword] = 1
      sentence_report[sentence[0]] += 1
      sentence_report[sentence[len(sentence) - 1]] += 1
      self.phrase_report.append(sentence_report)

  def calculate_print_report(self):
    pass
