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
    print('2 : Start New York Times Multiplayer Spelling Bee')
    print('3 : Join Existing Multiplayer Spelling Bee with gameID')

    beeType = int(input(''))

    createResponse = stub.CreateBee(bee_pb2.CreateRequest(beeType=beeType))
    gameID = createResponse.message
    playerID = 0
    print(createResponse.message)
    # response has message to include game id if mp

    # this start method is only for single or first player.
    # response = stub.StartBee(bee_pb2.StartRequest())
    # print('Enter exitgame to exit. You must use the bracketed letter')
    # print('Letters: ' + response.message)
    # loop while game is running


    # Seperate out into 3 options here to get name from 1st player

    if beeType == 1:
        startResponse = startBee(stub)
        print('Letters: ' + startResponse.message)
    elif beeType == 2:
        #I dont need to return letters here as will when player joins game
        startBee(stub)
        #print('Letters: ' + response.message)
        # joinReply will return letters as message
        player0Response = stub.JoinBee(bee_pb2.JoinRequest(gameID=gameID))
        print('Letters: ' + player0Response.joinMessage)
    else:
        joinResponse = joinBee(stub)
        print('Letters: ' + joinResponse.joinMessage)

    #game loop for all players
    wordIn = ''
    while wordIn != 'exitgame':
        wordIn = input('Enter word:')
        response = stub.SubmitWord(bee_pb2.SubmitWordRequest(wordIn=wordIn, playerID=playerID))
        print("Score: ", response.result)
    print('Game Over')

def joinBee(stub):
    #can remove this to a gui after.
    gameID = input('Enter the Game ID: ')
    #name = input('Enter your Name: ')
    #response will return letters
    #this gives you back the letters and player ID
    JoinResponse = stub.JoinBee(bee_pb2.JoinRequest(gameID=gameID))
    return JoinResponse

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
    run()
