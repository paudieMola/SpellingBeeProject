import json
from concurrent import futures
import logging
import sys
sys.path.append('..')

import app as app
import wordStore

import grpc
import random
import bee_pb2
import bee_pb2_grpc

class BeeServer(bee_pb2_grpc.BeeServerServicer):

    def StartBee(self, request, context):
        #do I put in here to call method in NYTBee object to get the chosen word?
        #chosen_word = pangrams.getChosenWord()
        #print(chosen_word)
        mixedup_word = ""
        with open("pangrams.json", "r") as pangram_file:
            pangram_dict = json.load(pangram_file)
            rand_num = random.randint(0, len(pangram_dict))
            chosen_word = list(pangram_dict.keys())[rand_num]
        chosen_list = []
        chosen_list[:0] = chosen_word
        print(chosen_list)
        middle_spot = int(round(len(chosen_list)/2))
        random.shuffle(chosen_list)
        middle_letter = chosen_list[middle_spot]
        middle_letter = '[' + middle_letter + ']'
        chosen_list[middle_spot] = middle_letter
        #for letter in half_chosen:
            #mixedup_word = letter + ' '
        #mixedup_word.join('[ '+ middle_letter +' ] ')
        #for letter in last_chosen:
            #mixedup_word.join(letter + '')
        #print(mixedup_word)
        #nytbee = app.nytBee
        #nytbee.mid_letter = middle_letter
        mixedup_word = str(chosen_list)
        return bee_pb2.StartReply(message=mixedup_word)

    def SubmitWord(self, request, context):
        result = 4
        return bee_pb2.SubmitWordReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bee_pb2_grpc.add_BeeServerServicer_to_server(BeeServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
