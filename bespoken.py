import re
import string

class Bespokenize:
    def parse_phrase(self, phrase):
        phrase = phrase.lower()
        self.parsed = re.findall(r"[\w']+|[.,!?;]", phrase)
        return self.parsed

    def seperate_into_sentences(self):
        end_punctuation = [".", "?", "!"]
        current_sentence = []
        sentences_list = []

        for item in self.parsed:
            current_sentence.append(item)

            if item in end_punctuation:
                sentences_list.append(current_sentence)
                current_sentence = []

        return sentences_list

    def filter_punctuation(self):
        sentences_list = self.seperate_into_sentences()
        punctuation = string.punctuation
        filtered_sentences_list = []

        for sentence in sentences_list:
            filtered_sentence = []
            for item in sentence:
                if item not in punctuation:
                    filtered_sentence.append(item)
            filtered_sentences_list.append(filtered_sentence)
        return filtered_sentences_list


    def word_count(self):
        sentences = self.filter_punctuation()
        total_word_count = 0
        for sentence in sentences:
            total_word_count += len(sentence)

        return total_word_count

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
        sentences = self.filter_punctuation()
        filtered_phrase = []

        for sentence in sentences:
            filtered_phrase += sentence

        return filtered_phrase.index(word) + 1
