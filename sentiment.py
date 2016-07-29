from pos_words import *
from neg_words import *
from bespoken import *
from behavior import *

class Sentiment:
  """Contains methods for Sentiment Class
  Import:
  ----------------
  pos_words.py
  neg_words.py
  bespken.py

  Methods:
  -----------------
  run_all_sentiment
  calculate_Word_count
  calculate_multipliers
  process_sentences
  calculate_sentence

  """

  def __init__(self, phrase):
    """
    Initialization

    Method arguments:
    -----------------
    phrase(string) -- phrase passed in


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
    # if not phrase:
    #   phrase = self.get_phrase()
    self.behavior = Behavior(phrase)
    # self.behavior_dict = [['aggressive', 'inquisitive'], ['mentoring'], ['social'], ['planning']]
    self.behavior.find_behaviors()
    self.behavior_dict = self.behavior.sentence_behavior_list
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)
    self.sentence_list = self.tokenizer.filter_punctuation()
    passed_word_count = self.tokenizer.word_count()

  def run_all_sentiment(self):
    """Runs all required methods to calculate sentiment

    Method arguments:
    -----------------
    N/A

    """
    self.process_sentences()
    self.calculate_multipliers()
    self.calculate_sentence()



  def calculate_word_count(self, words_to_analyze_list): ##FEEDBACK## - The other modules describe what the inputs each method takes are. Listing the output is also good, but knowing what input it takes is useful in knowing how to use the method.
    """Calculate positive, negative and neutral word count per sentence.

    Method arguments:
    -----------------
    words_to_analyze_list(string) - positive words found in phrase within pos_words.py file

    Returns: positive_count, negative_count, neutral_count

    """
    positive_count = 0
    negative_count = 0
    neutral_count = 0

  #for loop - finds words counts
    for word in words_to_analyze_list:
      if word in pos_words:
        positive_count +=1
        continue ##FEEDBACK## - No need to continue
      elif word in neg_words:
        negative_count +=1
        continue ##FEEDBACK## - No need to continue
      else:
        neutral_count +=1

    return positive_count, negative_count, neutral_count


  def calculate_multipliers(self):
    """Calculate list of Behavior multipliers.

    Method arguments:
    N/A

    Returns: multipliers_list

    """
    multipliers_list = []

  #for loop - takes passed in behaviors * value in behavior_dict
    for behavior_list in self.behavior_dict:
      multiplier = 0
      for behavior in behavior_list:
        multiplier += self.weighted_values_dict[behavior]
      multipliers_list.append(multiplier)
    return multipliers_list

  def process_sentences(self):
    """Builds sentence lists and reports pos, neg, neutral word counts by sentence

    Method arguments:
    N/A

    Returns: sentence_count

    """
    self.sentence_count = []

  # for loop - finds pos, neg, neutral words in each sentence
    for sentence in self.sentence_list:
      new_sentence_list = []
      positive_count, negative_count, neutral_count = self.calculate_word_count(sentence)
      new_sentence_list.append(positive_count)
      new_sentence_list.append(negative_count)
      new_sentence_list.append(neutral_count)
      self.sentence_count.append(new_sentence_list)
    return self.sentence_count


  def calculate_sentence(self):
    """Takes totals pos, neg, neutral words by behavior multiplier


    Method arguments:
    N/A

    Returns: Final Sentiment Report

    """
    final_total = []
    phrase_totals = []
    sentiment_percentages = []
    phrase_totals_added = 0
    number_of_sentences = self.tokenizer.sentence_count() # showing 4
    final_multipliers_list = self.calculate_multipliers() # showing [6, 2, 3, 2]

  #for loop - for all sentences take all pos, neg, neutral counts * multiplier
    for x in range(0, number_of_sentences): ##FEEDBACK## - For ranges starting at 0, you don't need the 0
      total = []
      for value in self.sentence_count[x]: # for this value in each
        total.append(value * final_multipliers_list[x])
      final_total.append(total)

  #for loop - use above numbers, append sentiment
    for number in range(0, 3): ##FEEDBACK## - For ranges starting at 0, you don't need the 0
      sentiment = 0
      for final_value in final_total:
        sentiment += final_value[number]
      phrase_totals.append(sentiment)

  #for loop - use sentiment totals and divide them all by phrase total words
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

