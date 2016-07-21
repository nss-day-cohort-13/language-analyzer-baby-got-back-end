from pos_words import *
from neg_words import *
from bespoken import *

class Sentiment:

  weighted_values_dict = {
    "aggressive": 1.1,
    "passive": 1,
    "mentoring": 0.7,
    "inquisitive": 0.3,
    "transaction": 0.6,
    "explanatory": 0.2,
    "planning": 0.8,
    "social": 0.9
  }

  def __init__(self, phrase=None):
    if not phrase:
      phrase = self.get_phrase()
    self.tokenizer = Bespokenize()
    print(phrase)
    self.tokenizer.parse_phrase(phrase)
    self.sentence_list = self.tokenizer.filter_punctuation()
    print(self.sentence_list)
    self.sentence_count = []
    # self.behavior = Behavior(phrase)
    # self.positive_sentiment_list = []
    # self.negative_sentiment_list = []
    # self.neutral_sentiment_list =[]

  def get_phrase(self):
    phrase = 'The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal. How would your life be different if you stopped making negative judgmental assumptions about people you encounter? Let today be the day you look for the good in everyone you meet and respect their journey.'
    return phrase


  def calculate_word_count(self, words_to_analyze_list):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for word in words_to_analyze_list:
      if word in pos_words:
        positive_count +=1
        continue
      elif word in neg_words:
        negative_count +=1
        continue
      else:
        neutral_count +=1

    return positive_count, negative_count, neutral_count

  def process_sentences(self):
    for sentence in self.sentence_list:
      new_sentence_list = []
      positive_count, negative_count, neutral_count = self.calculate_word_count(sentence)
      new_sentence_list.append(positive_count)
      new_sentence_list.append(negative_count)
      new_sentence_list.append(neutral_count)
      # print(new_sentence_list)
      self.sentence_count.append(new_sentence_list)
    print(self.sentence_count)



  def calculate_positive_percent(self, phrase):
    pass

  def calculate_negative_percent(self, phrase):
    pass

  def calculate_sentence(self, phrase):
    pass

  def pos_sentiment(self, phrase):
    import pos_words
    return 4

newobj = Sentiment()
# newobj = Sentiment(phrase='Hello there. Today is good')
# print(newobj.positive_sentiment_list)
# print(newobj.negative_sentiment_list)
# print(newobj.neutral_sentiment_list)
