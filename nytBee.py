import json
import random
import threading

from beeTemplate import spellingBee
import pangrams


class nytBee(spellingBee):
    __instance = None

    #singleton pattern to ensure only one instance of the game is in play
    @staticmethod
    def get_instance():
        if nytBee.__instance is None:
            with threading.Lock():
                if nytBee.__instance is None:
                    nytBee()
        return nytBee.__instance

    def __init__(self):
        super().__init__()
        if nytBee.__instance is not None:
            raise Exception("This is a singleton")
        else:
            nytBee.__instance = self
        self.complett = None
        self.totalscore = 0


    def choose_word(self):
        with open("pangrams.json", "r") as pangram_file:
            pangram_dict = json.load(pangram_file)
            rand_num = random.randint(0, len(pangram_dict))
            self.target_word = list(pangram_dict.keys())[rand_num]
        #changed code in assignment 2 to return a set here

        letterset = set(self.target_word)
        wordset = str(letterset)
        half1 = wordset[0:2]
        self.complett = wordset[2]
        half2 = wordset[4:]
        self.completter = '[' + self.complett + ']'
        mixedupWord = half1 + self.completter + half2
        print(mixedupWord)
        return mixedupWord

    def process_word(self, wordIn):
        #will add comment to response to client
        self.comment = ''
        if (len(wordIn)) > 3:
            if self.complett in wordIn:
                if self.validate_word(wordIn):
                    result = self.scoreWord(wordIn)
                    self.totalscore += result
                    self.comment = self.Rankings[self.getRankings(self.totalscore)]
            else:
                self.comment = ("Word must contain the letter: ", self.complett)
        else:
                self.comment = ("Words must contain 4 letters")
        return self.totalscore

    def validate_word(self, word_in):
        with open("words_dictionary.json", "r") as words_file:
            word_dict = json.load(words_file)
            if word_in in word_dict:
                return True
            else:
                return False

    def scoreWord(self, word_in):
        word_score = len(word_in)
        if pangrams.is_pangram(word_in):
            # I'll return this as a comment instead
            print("That is a pangram")
            word_score += 7
        return word_score

    def record_stats(self, word_score):
        pass

    def getRankings(self, totalscore):
        if self.totalscore < 15:
            rank = 1
        elif self.totalscore < 20:
            rank = 2
        elif self.totalscore < 30:
            rank = 3
        elif self.totalscore < 40:
            rank = 4
        else:
            rank = 5
        return rank

# used to build object
class nytBeeBuilder:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return nytBee()
