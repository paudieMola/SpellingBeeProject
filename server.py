import json
from concurrent import futures
import logging
import sys

import app
import nytBee

import object_factory
from beeTemplate import spellingBee

sys.path.append('')

import grpc
import bee_pb2
import bee_pb2_grpc


class BeeServer(bee_pb2_grpc.BeeServerServicer):

    def __init__(self):
        self.bee_type = "nytBee"
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder('nytBee', nytBee.nytBeeBuilder())
        #self.bee = self.factory.create('nytBee')
        #self.bee = self.bee.get_instance()

    def StartBee(self, request, context):
        #first I was going to choose the word in here
        #chosen_word = pangrams.getChosenWord()
        #print(chosen_word)
        mixedup_word = ""
        # with open("pangrams.json", "r") as pangram_file:
        #     pangram_dict = json.load(pangram_file)
        #     rand_num = random.randint(0, len(pangram_dict))
        #     chosen_word = list(pangram_dict.keys())[rand_num]
        # chosen_list = []
        # chosen_list[:0] = chosen_word
        # print(chosen_list)
        # middle_spot = int(round(len(chosen_list)/2))
        # random.shuffle(chosen_list)
        # middle_letter = chosen_list[middle_spot]
        # middle_letter = '[' + middle_letter + ']'
        # chosen_list[middle_spot] = middle_letter
        #for letter in half_chosen:
            #mixedup_word = letter + ' '
        #mixedup_word.join('[ '+ middle_letter +' ] ')
        #for letter in last_chosen:
            #mixedup_word.join(letter + '')
        #print(mixedup_word)
        print("in start Bee")
        self.bee = self.factory.create('nytBee')
        self.bee = self.bee.get_instance()
        mixedup_word = nytBee.nytBee.choose_word(self.bee)
        return bee_pb2.StartReply(message=mixedup_word)

    def SubmitWord(self, request, context):
        print("in submit word")
        #result = self.bee.process_word(request.wordIn)
        result = self.bee.process_word(request.wordIn)
        print('submit word ', result)
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
