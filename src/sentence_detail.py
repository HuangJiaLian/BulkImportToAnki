import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class Sentence(object):
    def __init__(self, english_text, chinese_text):
        self.english_text = english_text
        self.chinese_text = chinese_text
        self.uncommon_words = []
        self.translations = {}

    def __str__(self):
        return f'<{self.english_text}, {self.chinese_text}>'

    def extract_uncommon_words(self):
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(self.english_text)
        uncommon_words = [word for word in words if
                          word.lower() not in stop_words and word not in string.punctuation and "’" not in word]
        self.uncommon_words = uncommon_words

    def translate_uncommon_words(self, translator):
        for word in self.uncommon_words:
            if word not in self.translations:
                translation = translator.translate(word)
                self.translations[word] = translation

    def translate(self, translator):
        self.extract_uncommon_words()
        self.translate_uncommon_words(translator)
