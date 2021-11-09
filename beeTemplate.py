from abc import ABC, abstractmethod

class spellingBee(ABC):
    def __init__(self):
        # didnt use this yet
        self.target_word = ''
        self.rankings = {}
        # didn't use this yet either, but can check that words are not submitted twice
        self.list_of_submitted_words = []
        # didn't use this yet either but can fill with dictionary maybe to improve speed
        self.words = {}

    def choose_word(self):
        pass

    def process_word(self, word_in):
        pass

    def validate_word(self, word_in):
        pass

    def scoreWord(self, word_in):
        pass

    def record_stats(self, word_score):
        pass

    def getRankings(self, totalscore):
        pass