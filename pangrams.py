import json
from random import randint

pangrams = {}

# method to check if its a pangram and gets higher score
def is_pangram(word_in):
    if len(set(word_in)) == 7 and 's' not in word_in:
        return True
    else:
        return False

# I havent used this in this program but I might use in future
# def createPangramFile():
#     with open("wordStore/words_dictionary.json") as json_file:
#         words = json.load(json_file)
#
#         for word in words:
#             if is_pangram(word):
#                 pangrams[word] = ""
#
#     with open("wordStore/pangrams.json", "w") as pangram_file:
#         json.dump(pangrams, pangram_file)

# used my own method in nytBee class but based on this, thanks Larkin
def getChosenWord():
    with open("wordStore/pangrams.json", "r") as pangram_file:
        pangram_dict = json.load(pangram_file)
        rand_num = randint(0, len(pangram_dict))
        random_pangram = list(pangram_dict.keys())[rand_num]
        print(random_pangram)
    return random_pangram