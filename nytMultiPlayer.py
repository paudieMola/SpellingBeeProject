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
        self.gameID = uuid.uuid4()
        self.createMessage = (str(self.gameID))
        self.wordsUsed = []

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
        elif (len(wordIn)) > 3:
            self.comment = comments.get(2)
        elif self.complett not in wordIn:
            self.comment = comments.get(3)
        else:
            wordscore = self.scoreWord(wordIn)
            self.wordsUsed.append(wordIn)
            currentScore = self.players.values(playerID)
            currentScore += wordscore
            self.players[playerID] = currentScore
            self.comment = self.Rankings[self.getRankings(currentScore)]
        return wordscore

        # if (len(wordIn)) > 3 & wordIn not in self.wordsUsed:
        #     if self.complett in wordIn:
        #         if self.validate_word(wordIn):
        #             result = self.scoreWord(wordIn)
        #             self.wordsUsed.append(self, wordIn)
        #             self.totalscore += result
        #             self.comment = self.Rankings[self.getRankings(self.totalscore)]
        #     else:
        #         self.comment = ("Word must contain the letter: ", self.complett)
        # else:
        #         self.comment = ("Words must contain 4 letters")
        # return self.totalscore






    #
    # def validate_word(self, word_in):
    #     with open("words_dictionary.json", "r") as words_file:
    #         word_dict = json.load(words_file)
    #         if word_in in word_dict:
    #             return True
    #         else:
    #             return False
    #
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
        return index

# used to build object
class nytMPBeeBuilder:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return nytMPBee()
