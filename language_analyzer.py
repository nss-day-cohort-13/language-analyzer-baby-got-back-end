from bespoken import *
from sentiment import *
from behavior import *
from domain import *

class LanguageAnalyzer:

  def __init__(self, phrase):

    # self.sentiment_module = Sentiment(phrase)
    # self.behavior_module = Behavior(phrase)
    self.domain_module = Domain(phrase)

  def lang_run_all(self):
    # self.sentiment_module.run_all_sentiment()
    # self.behavior_module.run_all_behavior()
    self.domain_module.run_all_domain()
