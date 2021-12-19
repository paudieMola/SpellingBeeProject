from __future__ import print_function

import logging

import grpc
#import sys

import server

#sys.path.append('')
import bee_pb2
import bee_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:50051')
    stub = bee_pb2_grpc.BeeServerStub(channel)

    print('Choose game: ')
    #print('1 : New York Times Spelling Bee')
    print('1 : Start New York Times  Spelling Bee')
    print('2 : Join Existing Spelling Bee with gameID')

    beeType = int(input(''))

    createResponse = stub.CreateBee(bee_pb2.CreateRequest(beeType=beeType))
    gameID = createResponse.message
    #playerID = 0
    print(createResponse.message)

    # Seperate out into 3 options here to get name from 1st player

    #Take this out if I cant get it debugged.
    # if beeType == 1:
    #     startResponse = startBee(stub)
    #     print('Letters: ' + startResponse.message)
    if beeType == 1:
        #I dont need to return letters here as will when player joins game
        startBee(stub)
        # joinReply will return letters as message
        player0Response = stub.JoinBee(bee_pb2.JoinRequest(gameID=gameID))
        playerID = player0Response.playerID
        print('Player ID ' + str(playerID))
        #print('Letters: ' + player0Response.joinMessage)
    else:
        joinResponse = joinBee(stub)
        playerID = joinResponse.playerID
        while joinResponse.joinMessage == 'Something went wrong. Please try again':
            print(joinResponse.joinMessage)
            joinBee(stub)
        print('Player ID ' + str(playerID))
        print('Letters: ' + joinResponse.joinMessage)

    #game loop for all players
    wordIn = ''
    while wordIn != 'exitgame':
        wordIn = input('Enter word:')
        response = stub.SubmitWord(bee_pb2.SubmitWordRequest(wordIn=wordIn, playerID=playerID))
        print("Word Score: ", response.result, response.comment, "Player total: ", response.currentScore)
    print('Game Over')

def joinBee(stub):
    gameID = input('Enter the Game ID: ')
    #response will return letters
    #this gives you back the letters and player ID
    JoinResponse = stub.JoinBee(bee_pb2.JoinRequest(gameID=gameID))
    return JoinResponse

def startBee(stub):
# this start method is only for single or first player.
    response = stub.StartBee(bee_pb2.StartRequest())
    print('Give this code to allow another to enter this game')
    print('Enter exitgame to exit. You must use the bracketed letter [ ]')
    print('Letters: ' + response.message)
    return response

if __name__ == '__main__':
    logging.basicConfig()
    run()
