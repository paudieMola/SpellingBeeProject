import json
import random
import threading

from beeTemplate import spellingBee
import pangrams


class nytBee(spellingBee):
    __instance = None

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
        self.middle_letter = None
        self.totalscore = 0
        self.Rankings = {1: "Meh!", 2: "Alright like!", 3: "Savage!", 4: "Massive!", 5: "Medazza!"}

    def choose_word(self):
        with open("pangrams.json", "r") as pangram_file:
            pangram_dict = json.load(pangram_file)
            rand_num = random.randint(0, len(pangram_dict))
            chosen_word = list(pangram_dict.keys())[rand_num]
        chosen_list = []
        chosen_list[:0] = chosen_word
        print(chosen_list)
        middle_spot = int(round(len(chosen_list)/2))
        random.shuffle(chosen_list)
        self.middle_letter = chosen_list[middle_spot]
        middle_letter = '[' + self.middle_letter + ']'
        chosen_list[middle_spot] = middle_letter
        mixedup_word = str(chosen_list)
        return mixedup_word

    def process_word(self, word_in):
        self.comment = ''
        if (len(word_in)) > 3:
            if self.middle_letter in word_in:
                if self.validate_word(word_in):
                    result = self.scoreWord(word_in)
                    #print("Score: ", result)
                    self.totalscore += result
                    self.comment = self.Rankings[self.getRankings(self.totalscore)]
            else:
                self.comment = ("Word must contain the letter: ", self.middle_letter)
        else:
                self.comment = ("Words must contain 4 letters")
        return self.totalscore

    def validate_word(self, word_in):
        with open("words_dictionary.json", "r") as words_file:
            word_dict = json.load(words_file)
            if word_in in word_dict:
                return True
            else:
                print("Word invalid in dict")
                return False

    def scoreWord(self, word_in):
        word_score = len(word_in)
        if pangrams.is_pangram(word_in):
            print("That is a pangram")
            word_score += 7
        return word_score

    def record_stats(self, word_score):
        pass

    def getRankings(self, totalscore):
        if totalscore < 15:
            rank = 1
        elif totalscore < 20:
            rank = 2
        elif totalscore < 30:
            rank = 3
        elif totalscore < 40:
            rank = 4
        else:
            rank = 5
        return rank


class nytBeeBuilder:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return nytBee()
