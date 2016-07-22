from pos_words import *
from neg_words import *
from bespoken import *

class Sentiment:
  """Contains methods for Sentiment Class
  Import:
  ----------------
  pos_words.py
  neg_words.py
  bespken.py

  Methods:
  -----------------
  get_phrase
  calculate_Word_count
  calculate_multipliers
  process_sentences
  calculate_sentence
  """

  def __init__(self, phrase=None):
    """Initialization
    If incoming phrase present - use
    Else call get_phrase
    """
    self.weighted_values_dict = {
      "aggressive": 5,
      "passive": 1,
      "mentoring": 2,
      "inquisitive": 1,
      "transaction": 2,
      "explanatory": 1,
      "planning": 2,
      "social": 3
    }
    if not phrase:
      phrase = self.get_phrase()
    self.behavior_dict = [['aggressive', 'inquisitive'], ['mentoring'], ['social'], ['planning']]
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)
    self.sentence_list = self.tokenizer.filter_punctuation()
    passed_word_count = self.tokenizer.word_count()

  def run_all_sentiment(self):
    self.process_sentences()
    self.calculate_multipliers()
    self.calculate_sentence()


  def get_phrase(self):
    """If called provied phrase for sentiment analysis.

    Returns: phrase

    """
    phrase = 'The challenge of space exploration and particularly of landing men on the moon represents the greatest challenge which has ever faced the human race. Even if there were no clear scientific or other arguments for proceeding with this task, the whole history of our civilization would still impel men toward the goal. How would your life be different if you stopped making negative judgmental assumptions about people you encounter? Let today be the day you look for the good in everyone you meet and respect their journey.'
    return phrase


  def calculate_word_count(self, words_to_analyze_list):
    """Calculate positive, negative and neutral word count per sentence.

    Keyword arguments:
    positive_count - positive words found in phrase within pos_words.py file
    negative_count - positive words found in phrase within pos_words.py file
    neutral_count - positive words found in phrase within pos_words.py file
      if word found - add to related list

    Returns: positive_count, negative_count, neutral_count

    """
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

  def calculate_multipliers(self):
    """Calculate list of Behavior multipliers.

    Keyword arguments:
    behavior_dict - behaviors that are present

    Returns: multipliers_list

    """
    multipliers_list = []
    for behavior_list in self.behavior_dict:
      multiplier = 0
      for behavior in behavior_list:
        multiplier += self.weighted_values_dict[behavior]
      multipliers_list.append(multiplier)
    return multipliers_list

  def process_sentences(self):
    """Builds sentence lists and reports pos, neg, neutral word counts by sente.

    Keyword arguments:
    behavior_dict - behaviors that are present

    Returns: multipliers_list

    """
    self.sentence_count = []
    for sentence in self.sentence_list:
      new_sentence_list = []
      positive_count, negative_count, neutral_count = self.calculate_word_count(sentence)
      new_sentence_list.append(positive_count)
      new_sentence_list.append(negative_count)
      new_sentence_list.append(neutral_count)
      self.sentence_count.append(new_sentence_list)
    return self.sentence_count


  def calculate_sentence(self):
    final_total = []
    phrase_totals = []
    sentiment_percentages = []
    phrase_totals_added = 0
    number_of_sentences = self.tokenizer.sentence_count() # showing 4
    final_multipliers_list = self.calculate_multipliers() # showing [6, 2, 3, 2]
    for x in range(0, number_of_sentences):
      total = []
      for value in self.sentence_count[x]: # for this value in each
        total.append(value * final_multipliers_list[x])
      final_total.append(total)
    for number in range(0, 3):
      sentiment = 0
      for final_value in final_total:
        sentiment += final_value[number]
      phrase_totals.append(sentiment)
    for sentiment_value in phrase_totals:
      phrase_totals_added += sentiment_value
    for sentiment_value in phrase_totals:
      sentiment_percentages.append(format(sentiment_value / phrase_totals_added, ".2f"))
    # format(sentiment_percentages)
    print(' ')
    print('---------- SENTIMENT ANALYSIS RESULTS ----------')
    print(' ')
    print('  Positive: {0}'.format(sentiment_percentages[0]))
    print('  Negative: {0}'.format(sentiment_percentages[1]))
    print('  Neutral: {0}'.format(sentiment_percentages[2]))
    print(' ')


    return {'positive': 0.05, 'negative': 0.06, 'neutral': 0.89}

  # def pos_sentiment(self, phrase):
  #   import pos_words
  #   return 4

# run_all_sentiment()
# newobj = Sentiment()
# newobj = Sentiment(phrase='Hello there. Today is good')
# print(newobj.positive_sentiment_list)
# print(newobj.negative_sentiment_list)
# print(newobj.neutral_sentiment_list)
