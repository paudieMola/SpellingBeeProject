from concurrent import futures
import logging

import sys
import nytBee
import nytMultiPlayer

import object_factory

#this worked to get the proto file creating the bee_pb2 files
#but issues still with importing modules
#from nytMultiPlayer import nytMPBee

sys.path.append('')

import grpc
import bee_pb2
import bee_pb2_grpc


class BeeServer(bee_pb2_grpc.BeeServerServicer):

    def __init__(self):
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder(1, nytMultiPlayer.nytMPBeeBuilder())


    def StartBee(self, request, context):
        print("in start Bee")
        # word is chosen in the nytBee class and letters shuffled there.
        mixedup_word = self.bee.choose_word()
        # send the word to the client
        return bee_pb2.StartReply(message=mixedup_word)

    def SubmitWord(self, request, context):
        print("in submit word")
        print(request.wordIn)
        result, comment, currentScore = self.bee.process_word(request.wordIn, request.playerID)
        print('submit word ', result)
        return bee_pb2.SubmitWordReply(result=result, comment=comment, currentScore=currentScore)

    # creates a new bee for first player or gets the instance if its a later player
    def CreateBee(self, request, context):
        print('in create bee')
        if request.beeType != 2:
            self.beeType = self.factory.create(request.beeType)
            self.bee = self.beeType.get_instance()
            message = self.bee.createMessage
        else:
            self.bee = self.beeType.get_instance()
            self.bee.createMessage = 'Enter game ID to join.'
            message = self.bee.createMessage
        return bee_pb2.CreateReply(message=message)

    # so that other players can join the bee already created.
    def JoinBee(self, request, context):
        self.bee = self.beeType.get_instance()
        playerID = self.bee.register_player()

        if self.bee.gameID == request.gameID:
            joinMessage = self.bee.mixedupWord
        else:
            joinMessage = 'Something went wrong. Please try again'
        return bee_pb2.JoinReply(joinMessage=joinMessage, playerID=playerID)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bee_pb2_grpc.add_BeeServerServicer_to_server(BeeServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
