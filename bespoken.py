import re
import string

class Bespokenize:
    """Contains methods for tokenizing a phrase

    Methods:
    -----------------
    parse_phrase
    separate_into_sentences
    filter_punctuation
    word_count
    total_word_count
    alphanum_characters
    sentence_count
    get_position
    """
    def parse_phrase(self, phrase):##FEEDBACK## - Since this needs to happen before any other methods,
                                                # it's a pretty good candidate for sticking in an __init__
                                                # method.  Cuts down on a function call in all the modules
                                                # that use it.
        """Parse a phrase by words and punctuation and store in self.parsed

        Method arguments:
        -----------------
        phrase(string) -- The phrase to be parsed
        """

        phrase = phrase.lower()
        self.parsed = re.findall(r"[\w']+|[.,!?;]", phrase)
        return self.parsed

    def separate_into_sentences(self):
        """Lists sentences present in self.parsed

        Method arguments:
        -----------------
        n/a
        """

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

        """Lists sentences without punctuation from self.parsed

        Method arguments:
        -----------------
        n/a
        """

        sentences_list = self.separate_into_sentences()
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
        """List number of words in each sentence in self.parsed

        Method arguments:
        -----------------
        n/a
        """

        sentences = self.filter_punctuation()
        words_per_sentence = []
        for sentence in sentences:
            words_per_sentence.extend([len(sentence)])

        return words_per_sentence

    def total_word_count(self):
        """List number of words in the entire phrase in self.parsed

        Method arguments:
        -----------------
        n/a
        """
        sentence_word_count = self.word_count()
        total_words = 0

        for count in sentence_word_count:
            total_words += count

        return total_words

    def alphanum_characters(self):
        """Lists all alphanumeric characters used in self.parsed

        Method arguments:
        -----------------
        n/a
        """
        alphanums_used = set()

        for item in self.parsed:
            for char in item:
                if char.isalnum():
                     alphanums_used.add(char)
        alphanums_used = list(alphanums_used)   ##FEEDBACK## - you could one-line this by wrapping the list() in the sorted()
        alphanums_used = sorted(alphanums_used) #-----------/
        return ''.join(char for char in alphanums_used) ##FEEDBACK## - no need for a for loop, you can just join alphanums_used

    def sentence_count(self):
        """Lists number of sentences present in self.parsed

        Method arguments:
        -----------------
        n/a
        """

        sentences = self.separate_into_sentences()
        return len(sentences)

    def get_position(self, word):

        """Lists the position of a word based on all words in self.parsed

        Method arguments:
        -----------------
        word(string) -- The word to get the position of
        """

        sentences = self.filter_punctuation()
        filtered_phrase = []

        for sentence in sentences:
            filtered_phrase += sentence

        return filtered_phrase.index(word) + 1
