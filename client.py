from __future__ import print_function

import logging

import grpc
import sys
sys.path.append('')
import bee_pb2
import bee_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = bee_pb2_grpc.BeeServerStub(channel)

    # start the game and
    response = stub.StartBee(bee_pb2.StartRequest())
    print('Enter exitgame to exit. You must use the bracketed letter')
    print('Letters: ' + response.message)
    # loop while game is running
    wordIn = ''
    while wordIn != 'exitgame':
        wordIn = input('Enter word:')
        response = stub.SubmitWord(bee_pb2.SubmitWordRequest(wordIn=wordIn))
        print("Score: ", response.result)


if __name__ == '__main__':
    logging.basicConfig()
    gameChoice = -1
    while gameChoice != 1:
        print('Choose game: ')
        print('1 : New York Times Spelling Bee')
        gameChoice = int(input(''))
    run()