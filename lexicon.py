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
      "scientific": [],
      "educational": [],
      "politics": [],
      "relationships": [],
      "people": ['man', 'men', 'woman', 'women'],
      "grammar": ['sentence', 'sentences'],
      "preference": ['love', 'loves']
    },
    "behavior":
    {
      "aggressive": [],
      "passive": [],
      "mentoring": [],
      "inquisitive": [],
      "transaction": []
    }
  }
]
