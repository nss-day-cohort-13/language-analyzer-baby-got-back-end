from bespoken import *

class DomainModule:

  def __init__(self, phrase):
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)

    self.dom_parsed = self.tokenizer.filter_punctuation()

  def find_keywords(self):
    pass

  def find_domains(self):
    pass

  def create_report(self):
    pass
