# import json
# import random
import threading
import uuid

import pangrams
from nytBee import nytBee

# inherits from ntyBee from assignment 1
class nytMPBee(nytBee):
    __instance = None

    #singleton pattern to ensure only one instance of the game is in play
    @staticmethod
    def get_instance():
        if nytMPBee.__instance is None:
            with threading.Lock():
                if nytMPBee.__instance is None:
                    nytMPBee()
        return nytMPBee.__instance

    def __init__(self):
        super().__init__()
        if nytMPBee.__instance is not None:
            raise Exception("This is a singleton")
        else:
            nytMPBee.__instance = self
        self.complett = None
        self.gameID = str(uuid.uuid4())
        self.createMessage = (self.gameID)
        self.wordsUsed = []
        self.currentScore = 0

    def process_word(self, wordIn, playerID):
        # updated from assignment 1 to add comment to response to client
        self.comment = ''

        comments = {
            1: 'Word used already',
            2: 'Word must contain 4 letters',
            3: 'Word must contain the bracketed letter',
            4: 'Word does not exist',
            5: 'Word does not exist'
        }

        # updated to get the correct comment and to keep track of all players scores.
        # also keeps track of words used so no player can use the again.
        wordscore = 0
        if wordIn in self.wordsUsed:
            self.comment = comments.get(1)
        elif (len(wordIn)) < 4:
            self.comment = comments.get(2)
        elif self.complett not in wordIn:
            self.comment = comments.get(3)
        else:
            if self.validate_word(wordIn):
                wordscore = self.scoreWord(wordIn)
                if pangrams.is_pangram(wordIn):
                    # I'll return this as a comment instead
                    self.comment = comments.get(5)
                    wordscore += 7
                self.wordsUsed.append(wordIn)
                self.currentScore = self.players[playerID]
                self.currentScore += wordscore
                self.players[playerID] = self.currentScore
                self.comment += self.Rankings[self.getRankings(self.currentScore)]
            else:
                self.comment = comments.get(4)
        return wordscore, self.comment, self.currentScore

    def scoreWord(self, word_in):
        #changed to take out panagram check here.
        word_score = len(word_in)
        return word_score

    def record_stats(self, word_score):
        pass

    def getRankings(self, currentScore):
        if currentScore < 10:
            rank = 1
        elif currentScore < 15:
            rank = 2
        elif currentScore < 20:
            rank = 3
        elif currentScore < 25:
            rank = 4
        else:
            rank = 5
        return rank

    def register_player(self):
        index = len(self.players)
        self.players[index] = 0
        return index

# used to build object
class nytMPBeeBuilder:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return nytMPBee()
