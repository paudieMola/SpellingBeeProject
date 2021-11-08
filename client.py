from __future__ import print_function

import logging

import grpc
import bee_pb2
import bee_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051', )
    stub = bee_pb2_grpc.BeeServerStub(channel)
    response = stub.StartBee(bee_pb2.StartRequest())
    print("Word: " + response.message)
    response = stub.SubmitWord(bee_pb2.SubmitWordRequest(wordIn='HUURNTH'))
    print("Result: " + str(response.result))

if __name__ == '__main__':
    logging.basicConfig()
    run()