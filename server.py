from concurrent import futures
import logging

import sys
import nytBee

import object_factory

#this worked to get the proto file creating the bee_pb2 files
#but issues still with importing modules
sys.path.append('')

import grpc
import bee_pb2
import bee_pb2_grpc


class BeeServer(bee_pb2_grpc.BeeServerServicer):

    def __init__(self):
        #hardcoded to just create a ntyBee for the moment.
        self.bee_type = "nytBee"
        #following can be used to create other games on the fly
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder('nytBee', nytBee.nytBeeBuilder())

    def StartBee(self, request, context):
        print("in start Bee")
        # create and get the singleton instance
        self.bee = self.factory.create('nytBee')
        self.bee = self.bee.get_instance()
        # word is chosen in the nytBee class and letters shuffled there.
        mixedup_word = nytBee.nytBee.choose_word(self.bee)
        # send the word to the client
        return bee_pb2.StartReply(message=mixedup_word)

    def SubmitWord(self, request, context):
        print("in submit word")
        # check word submitted by client and get a result
        # I should create another parameter for message too to be returned to client
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
