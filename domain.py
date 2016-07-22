from lexicon import *
from bespoken import *

class Domain:

  def __init__(self, phrase):
    '''When this class is instantiated, it...
      1) gets an instance of a tokenizer
      2) parses the phrase passed in
      3) separates that phrase into sentences
          and
      4) filters the punctuation from the phrase

      self.keyword_list - a list that stores domain keywords found in each sentence by sentence
      self.domain_list - a list that stores the domains represented in each sentence by sentence
      self.full_report - a dictionary that has each domain represented in the entire phrase as a single key,
                         and its total percentage in the phrase as the value
      Arguments:
      -----------------
      phrase - The phrase being analyzed, passed in when instantiated by the top-level
               language analysis module.
    '''
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)

    self.dom_parsed = self.tokenizer.filter_punctuation()
    self.keyword_list = list()
    self.domain_list = list()
    self.full_report = dict()

  def find_keywords_and_domains(self):
    '''Loops over each word in each sentence in the phrase being analyzed
       and populates self.domain_list and self.keyword_list with matched
       domains and domain keywords respectively.

       Method arguments:
       -----------------
       n/a
    '''
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
    '''Populates self.phrase_report with lists of single
       reports for each sentence in the phrase being analyzed.

       Method arguments:
       -----------------
       n/a
    '''
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
    '''Using self.phrase_report, this function creates a final report of
       analysis of the full phrase in a dictionary where each key represents
       a domain present in the phrase and its value is the domain's overall
       percentage in the full phrase. Full report is saved in self.full_report.

       Method arguments:
       -----------------
       n/a
    '''
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

  def print_report(self):
    '''Renders self.full_report as a readable report when the program runs

       Method arguments:
       -----------------
       n/a
    '''
    print(' ')
    print('---------- DOMAIN ANALYSIS RESULTS ----------')
    print(' ')
    for key, value in self.full_report.items():
      print('  {0}: {1}'.format(key.capitalize(), value))
    print(' ')

  def run_all_domain(self):
    '''Calls all methods on this class needed to create a report
       of the domain analysis of a phrase

       Method arguments:
       -----------------
       n/a
    '''
    self.find_keywords_and_domains()
    self.create_phrase_report()
    self.calculate_full_report()
    self.print_report()
