# import json
# import random
import threading
import uuid

# from beeTemplate import spellingBee
import pangrams
from nytBee import nytBee


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
        #will add comment to response to client
        #takes
        self.comment = ''

        comments = {
            1: 'Word used already',
            2: 'Word must contain 4 letters',
            3: 'Word must contain the bracketed letter'
        }

        wordscore = 0
        if wordIn in self.wordsUsed:
            self.comment = comments.get(1)
        elif (len(wordIn)) < 4:
            self.comment = comments.get(2)
        elif self.complett not in wordIn:
            self.comment = comments.get(3)
        else:
            wordscore = self.scoreWord(wordIn)
            self.wordsUsed.append(wordIn)
            self.currentScore = self.players[playerID]
            self.currentScore += wordscore
            self.players[playerID] = self.currentScore
            self.comment = self.Rankings[self.getRankings(self.currentScore)]
        return wordscore

    def scoreWord(self, word_in):
        word_score = len(word_in)
        if pangrams.is_pangram(word_in):
            # I'll return this as a comment instead
            print("That is a pangram")
            word_score += 7
        return word_score

    def record_stats(self, word_score):
        #this will record each players words and scores
        #are guessed words going to be out of bounds.
        pass

    def getRankings(self, currentScore):
        #this will change to apply to the player rather than the game
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
