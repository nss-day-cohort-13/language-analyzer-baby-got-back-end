from bespoken import *
from lexicon import *
from collections import Counter

class Behavior:
    '''
    Contains methods for predicting the behavior of a provided statement

    Methods:
    -----------------
    __init__
    find_behaviors
    find_weighted_behavior_values
    generate_phrase_behavior_report
    print_report
    run_all_behavior
    '''

  def __init__(self, phrase):
    '''
    On instantiation, this class gains:
    - Tokenizer
    - User phrase parsed by spaces
    - User parsed-phrase re-parsed to be separated into sentences
    - Class-wide list named sentence_behavior_list
    - Class-wide list named behavior_percentage_weighted
    '''
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)
    self.sentences = self.tokenizer.separate_into_sentences()
    self.sentence_behavior_list = list()
    self.behavior_percentage_weighted = list()

  def find_behaviors(self):
    '''
    Loops through the words in each sentence in the phrase to find matches to the lexicon for behavior keywords

    Arguments
    ----------
    None
    '''
    # loops through each sentence list in self.sentences
    # -creates new list for sentence_behaviors and adds it as value to sentence_behavior_list
    for sentence in self.sentences:
      self.sentence_behaviors = list()
      self.sentence_behavior_list.append(self.sentence_behaviors)
      # loops through each word in the current sentence
      for word in sentence:
        # loops through each item in behavior dictionary in lexicon
        for behavior, keys in lexicon[0]["behavior"].items():
          # loops through list values of each behavior for current word to locate a match
          for keyword in keys:
            # If match is located to value, key is appended to sentence_behaviors list
            if word == keyword:
              self.sentence_behaviors.append(behavior)
    # Returns full sentence_behavior_list
    return self.sentence_behavior_list

  def find_weighted_behavior_value(self):
    '''
    Loops through the sentence behaviors lists in the phrase list to count the number of times a behavior appears and assigns a percentage value

    Arguments
    ----------
    None
    '''
    # Creates behavior_count list to contain behavior_instance_count list for each sentence in phrase
    self.behavior_count = list()
    # Loops through each sentence_behaviors list in sentence_behavior_list to count multiple instances of a recorded behavior
    for self.sentence_behaviors in self.sentence_behavior_list:
      # Adds count object (dictionary) to behavior_instance_count
      self.behavior_instance_count = {behavior:self.sentence_behaviors.count(behavior) for behavior in self.sentence_behaviors}
      # Adds behavior_instance_count to behavior_count list
      self.behavior_count.append(self.behavior_instance_count)

    # Once the behavior_count list has been populated, we loop back through that list to turn the instance counts into percentages
    for self.behavior_instance_count in self.behavior_count:
      # For each behavior_instance count in behavior_count, create new dict for behavior_percent and add it to behavior_percentage_weighted
      self.behavior_percent = dict()
      self.behavior_percentage_weighted.append(self.behavior_percent)
      # For each key/value pair in behavior_instance_count, run equation to get percentage value
      for behavior, value in self.behavior_instance_count.items():
        raw_percent = value / sum(self.behavior_instance_count.values())
        # Percentages are made to appear rounded to two decimal places
        percent = float("{0:.2f}".format(raw_percent))
        # Percentages are added as values in key/value pairs to behavior_percent dictionary
        self.behavior_percent[behavior] = percent

  def generate_phrase_behavior_report(self):
    '''
    Averages the behavior percentages per sentence into an overall report for the phrase

    Arguments
    ----------
    None
    '''

    # Gets the sum total of sentence percentage values
    self.sentence_count_sum = 0
    for self.behavior_percent in self.behavior_percentage_weighted:
      self.sentence_count_sum += sum(self.behavior_percent.values())

    # New list to hold averaged behavior percentages, appends sentence behavior dictionaries prior to getting overall average
    self.phrase_averaged_behaviors = list()
    # For each sentence in phrase, create a new dict for percent averages weighted against the whole phrase and append to list
    for self.behavior_percent in self.behavior_percentage_weighted:
      self.sentence_averaged_behaviors = dict()
      self.phrase_averaged_behaviors.append(self.sentence_averaged_behaviors)
      # Calculates new percentage avergae per sentence against phrase total value, makes it appear rounded to two decimal places
      for behavior, value in self.behavior_percent.items():
        raw_weighted_value = value / self.sentence_count_sum
        rounded_value = float("{0:.2f}".format(raw_weighted_value))
        # appends new key/value pair to sentence averaged behavior
        self.sentence_averaged_behaviors[behavior] = rounded_value

    # Adds all of the dictionaries in phrase_averaged_behaviors together in a single dictionary, sums the value of any repeated keys
    self.raw_report = sum((Counter(self.sentence_averaged_behaviors) for self.sentence_averaged_behaviors in self.phrase_averaged_behaviors),Counter())

    # Make the values appear rounded to two decimal places
    self.report = dict()
    for behavior, value in self.raw_report.items():
      rounded_final = float("{0:.2f}".format(value))
      self.report[behavior] = rounded_final

    # Returns report information and final dictionary of percentage values
    return self.report

  def print_report(self):
    '''
    Prints report in group-agreed upon stylized manner

    Arguments
    ----------
    None
    '''

    print(' ')
    print('---------- BEHAVIOR ANALYSIS RESULTS ----------')
    print(' ')
    for key, value in self.report.items():
      print('  {0}: {1}'.format(key.capitalize(), value))
    print(' ')

  def run_all_behavior(self):
    '''
    Runs all methods in class in order for Language Analyzer

    Arguments
    ----------
    None
    '''

    self.find_behaviors()
    self.find_weighted_behavior_value()
    self.generate_phrase_behavior_report()
    self.print_report()

