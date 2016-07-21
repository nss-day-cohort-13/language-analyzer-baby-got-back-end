from lexicon import *
from bespoken import *

class DomainModule:

  def __init__(self, phrase):
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)

    self.dom_parsed = self.tokenizer.filter_punctuation()
    self.keyword_list = list()
    self.domain_list = list()
    self.full_report = dict()

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

  def calculate_full_report(self):
    percentage_report = list()
    total_domains = set()
    for sentence_report in self.phrase_report:
      dom_count = 0
      partial_report = dict()
      for domain, value in sentence_report.items():
        total_domains.add(domain)
        dom_count += value
      for domain, value in sentence_report.items():
        partial_report[domain] = format(value / dom_count)
      percentage_report.append(partial_report)
    for domain in total_domains:
      self.full_report[domain] = 0
      for partial in percentage_report:
        try:
          self.full_report[domain] += float(partial[domain])
        except:
          pass
      self.full_report[domain] /= len(self.phrase_report)
      self.full_report[domain] = format(self.full_report[domain], '.2f')
