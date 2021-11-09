from abc import ABC, abstractmethod

class spellingBee(ABC):
    def __init__(self):
        self.target_word = ''
        self.rankings = {}
        self.list_of_submits = []
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