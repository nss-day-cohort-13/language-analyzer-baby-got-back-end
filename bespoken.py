import re
import string

class Bespokenize:
    def parse_phrase(self, phrase):
        phrase = phrase.lower()
        self.parsed = re.findall(r"[\w']+|[.,!?;]", phrase)
        return self.parsed

    def filter_punctuation(self):
        punctuation = string.punctuation
        filtered_phrase = []

        for item in self.parsed:
            if item not in punctuation:
                filtered_phrase.append(item)

        return filtered_phrase

    def separate_into_sentences(self):
        end_punctuation = [".", "?", "!"]
        current_sentence = []
        sentences_list = []

        for item in self.parsed:
            current_sentence.append(item)

            if item in end_punctuation:
                sentences_list.append(current_sentence)
                current_sentence = []

        return sentences_list

    def word_count(self):
        words = self.filter_punctuation()
        return len(words)

    def alphanum_characters(self):
        alphanums_used = set()

        for item in self.parsed:
            for char in item:
                if char.isalnum():
                     alphanums_used.add(char)
        alphanums_used = list(alphanums_used)
        alphanums_used = sorted(alphanums_used)
        return ''.join(char for char in alphanums_used)

    def sentence_count(self):
        sentences = self.seperate_into_sentences()
        return len(sentences)

    def get_position(self, word):
        filtered_phrase = self.filter_punctuation()
        return filtered_phrase.index(word) + 1
