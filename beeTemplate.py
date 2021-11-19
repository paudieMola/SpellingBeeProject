import uuid
from abc import ABC, abstractmethod

class spellingBee(ABC):
    def __init__(self):
        # didnt use this yet
        self.target_word = ''
        self.rankings = {}
        # didn't use this yet either, but can check that words are not submitted twice
        #self.wordsAndScores = {} this is going to be in the player class really
        # didn't use this yet either but can fill with dictionary maybe to improve speed
        self.players = []
        self.gameID = 0
        self.Rankings = {1: "Meh!", 2: "Alright like!", 3: "Savage!", 4: "Massive!", 5: "Medazza!"}
        self.winning_player_index = -1
        self.last_player_index = -1

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

    def register_player(self, username):
        if username not in self.players:
            index = len(self.players)
            self.players.append(username)
            return index
        else:
            return -1

    def getMatchID(self):
        self.gameID = uuid.uuid4()
        return self.gameID