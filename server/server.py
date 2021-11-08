from concurrent import futures
import logging
import sys
sys.path.append('..')


import grpc

import bee_pb2
import bee_pb2_grpc


class BeeServer(bee_pb2_grpc.BeeServerServicer):

    def StartBee(self, request, context):
        #do I put in here to call method in NYTBee object to get the chosen word?
        chosen_word = 'T E A [U] R A B'
        return bee_pb2.StartReply(message=chosen_word)

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
