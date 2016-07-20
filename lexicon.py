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
      "relationships": ['respect'],
      "people": ['man', 'men', 'woman', 'women', 'human', 'life', 'people', 'everyone'],
      "grammar": ['sentence', 'sentences'],
      "preference": ['love', 'loves'],
      "goal": ['challenge', 'task', 'goal'],
      "transportation": ['landing', 'journey'],
      "sociological": ['history', 'civilization', 'race'],
      "ideological": ['good'],
      "time": ['today', 'day']
    },
    "behavior":
    {
      "aggressive": ['impel', 'arguments', 'stopped', 'judgemental'],
      "passive": ['encounter', 'let'],
      "mentoring": [],
      "inquisitive": ['exploration', 'arguments', 'different'],
      "transaction": [],
      "explanatory": ['represents'],
      "planning": ['proceeding', 'task', 'goal', 'assumptions'],
      "social": ['respect', 'meet']
    }
  }
]
