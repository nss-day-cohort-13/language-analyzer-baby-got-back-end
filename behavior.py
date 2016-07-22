from bespoken import *
from lexicon import *
from collections import Counter

class Behavior:
  def __init__(self, phrase):
    self.tokenizer = Bespokenize()
    self.tokenizer.parse_phrase(phrase)
    self.sentences = self.tokenizer.separate_into_sentences()
    self.sentence_behavior_list = list()
    self.behavior_percentage_weighted = list()

  def find_behaviors(self):
    for sentence in self.sentences:
      self.sentence_behaviors = list()
      self.sentence_behavior_list.append(self.sentence_behaviors)
      for word in sentence:
        for behavior, keys in lexicon[0]["behavior"].items():
          for keyword in keys:
            if word == keyword:
              self.sentence_behaviors.append(behavior)

    return self.sentence_behavior_list

  def find_weighted_behavior_value(self):
    self.behavior_count = list()
    for self.sentence_behaviors in self.sentence_behavior_list:
      self.behavior_instance_count = {behavior:self.sentence_behaviors.count(behavior) for behavior in self.sentence_behaviors}
      self.behavior_count.append(self.behavior_instance_count)

    for self.behavior_instance_count in self.behavior_count:
      self.behavior_percent = dict()
      self.behavior_percentage_weighted.append(self.behavior_percent)
      for behavior, value in self.behavior_instance_count.items():
        raw_percent = value / sum(self.behavior_instance_count.values())
        percent = float("{0:.2f}".format(raw_percent))
        self.behavior_percent[behavior] = percent

  def generate_phrase_behavior_report(self):
    self.sentence_count_sum = 0
    for self.behavior_percent in self.behavior_percentage_weighted:
      self.sentence_count_sum += sum(self.behavior_percent.values())

    self.phrase_averaged_behaviors = list()
    for self.behavior_percent in self.behavior_percentage_weighted:
      self.sentence_averaged_behaviors = dict()
      self.phrase_averaged_behaviors.append(self.sentence_averaged_behaviors)
      for behavior, value in self.behavior_percent.items():
        raw_weighted_value = value / self.sentence_count_sum
        rounded_value = float("{0:.2f}".format(raw_weighted_value))
        self.sentence_averaged_behaviors[behavior] = rounded_value

    self.raw_report = sum((Counter(self.sentence_averaged_behaviors) for self.sentence_averaged_behaviors in self.phrase_averaged_behaviors),Counter())

    self.report = dict()
    for behavior, value in self.raw_report.items():
      rounded_final = float("{0:.2f}".format(value))
      self.report[behavior] = rounded_final

    return self.report

  def print_report(self):
    print(' ')
    print('---------- BEHAVIOR ANALYSIS RESULTS ----------')
    print(' ')
    for key, value in self.report.items():
      print('  {0}: {1}'.format(key.capitalize(), value))
    print(' ')

  def run_all_behavior(self):
    self.find_behaviors()
    self.find_weighted_behavior_value()
    self.generate_phrase_behavior_report()
    self.print_report()

