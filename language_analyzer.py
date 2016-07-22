from bespoken import *
from sentiment import *
from behavior import *
from domain import *

class LanguageAnalyzer:

  def __init__(self, phrase):
    '''When instantiated, this module instantiates all of the
       discrete language analysis modules

       Arguments:
       ----------
       phrase - the phrase to be analyzed; passed down for processing
                in each discrete analysis module
    '''
    self.sentiment_module = Sentiment(phrase)
    # self.behavior_module = Behavior(phrase)
    self.domain_module = Domain(phrase)

  def lang_run_all(self):
    '''Runs all of the 'run_all' functions in each module

    Method arguments:
    -----------------
    n/as
    '''
    self.sentiment_module.run_all_sentiment()
    # self.behavior_module.run_all_behavior()
    self.domain_module.run_all_domain()
