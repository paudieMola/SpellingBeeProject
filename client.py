from __future__ import print_function

import logging

import grpc
import sys

import server

sys.path.append('')
import bee_pb2
import bee_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = bee_pb2_grpc.BeeServerStub(channel)

    print('Choose game: ')
    print('1 : New York Times Spelling Bee')
    print('2 : New York Times Multiplayer Spelling Bee')
    print('3 : Enter game ID to join Spelling Bee')

    beeType = int(input(''))

    response = stub.CreateBee(bee_pb2.CreateRequest(beeType=beeType))
    print(response.message)
    # response has message to include game id if mp

    # this start method is only for single or first player.
    # response = stub.StartBee(bee_pb2.StartRequest())
    # print('Enter exitgame to exit. You must use the bracketed letter')
    # print('Letters: ' + response.message)
    # loop while game is running
    if beeType != 3:
        response = startBee(stub)
        print('Letters: ' + response.message)
    else:
        response = joinBee(stub)

    wordIn = ''
    while wordIn != 'exitgame':
        wordIn = input('Enter word:')
        response = stub.SubmitWord(bee_pb2.SubmitWordRequest(wordIn=wordIn))
        print("Score: ", response.result)

    # def startBee():
    # # this start method is only for single or first player.
    #     response = stub.StartBee(bee_pb2.StartRequest())
    #     print('Enter exitgame to exit. You must use the bracketed letter')
    #     return response
    #     #print('Letters: ' + response.message)

def joinBee(stub):
    response = stub.JoinBee(bee_pb2.JoinRequest())
    print('Enter the Game ID: ')

def startBee(stub):
# this start method is only for single or first player.
    response = stub.StartBee(bee_pb2.StartRequest())
    print('Enter exitgame to exit. You must use the bracketed letter')
    return response

# def runNYTMP():
#     channel = grpc.insecure_channel('127.0.0.1:50051')
#     stub = bee_pb2_grpc.BeeServerStub(channel)
#
#     # start the game and
#     name = input('Enter your Name: ')
#     response = stub.StartBee(bee_pb2.StartMPRequest(message=name))
#     print('Welcome ' + name + 'Use GameID to allow second player to join this game.')
#     print(' Letters: ' + response.letters)
#
#     # loop while game is running
#     wordIn = ''
#     while wordIn != 'exitgame':
#         wordIn = input('Enter word:')
#         response = stub.SubmitWord(bee_pb2.SubmitWordRequest(wordIn=wordIn))
#         print("Score: ", response.result)

if __name__ == '__main__':
    logging.basicConfig()
    # while gameChoice < 1 | gameChoice > 2:
    #     print('Choose game: ')
    #     print('1 : New York Times Spelling Bee')
    #     print('2 : New York Times Multiplayer Spelling Bee')
    #     gameChoice = int(input(''))
    run()
