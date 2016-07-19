from pos_words import *
from neg_words import *

lexicon = [
  {
    "sentiment":
    {
      "positive": pos_words,
      "negative": neg_words
    },
    "domain":
    {
      "financial": [],
      "behavioral": [],
      "scientific": ['space', 'exploration', 'moon', 'scientific', 'arguments'],
      "educational": [],
      "politics": [],
      "relationships": [],
      "people": ['man', 'men', 'woman', 'women', 'human'],
      "grammar": ['sentence', 'sentences'],
      "preference": ['love', 'loves'],
      "goal": ['challenge', 'task', 'goal'],
      "transportation": ['landing'],
      "sociological": ['history', 'civilization', 'race']
    },
    "behavior":
    {
      "aggressive": ['impel'],
      "passive": [],
      "mentoring": [],
      "inquisitive": ['exploration', 'arguments'],
      "transaction": [],
      "explanatory": ['represents'],
      "planning": ['proceeding', 'task', 'goal']
    }
  }
]
