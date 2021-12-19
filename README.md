Spelling Bee Game

created by Helen Daly
R00142752

Soft 8023 Semester 1 2021

Assignment 2 Readme
I have extended the functionality of the original nytBee class to create a 
nytMultiplayer class. 
This allows players to play as a single player or allow other players
to join when the code is entered and authenticated. The code is a uuid
created for each game on the server. 
The multi player game keeps track of the scores of all the players, it 
will allow any number of players and words used by any player cannot
be reused. I have also updated the messages the user receives to include
the error if a word cannot be accepted for scoring, or if it is a pangram.

Assignment 1 Readme
Pattern 1
Singleton:
I have used the singleton pattern to create a spelling Bee game (nytBee). 
This ensures that there is only one instance of the game that can be accessed
from anywhere by the static method get_instance. 
I have created this in the server class and I am currently only creating the
nytBee game, but this can be changed to take in a game parameter to create other
types of games. 


Pattern 2
Template:
The nytBee also inherits from a template (beeTemplate) which can be used to create 
other types of games in future, but I'm only creating a nytBee for the moment. 
I have also used a generic object factory which can be used in further 
development to create different games as required.  

Encapsulation
I have created packages to encapsulate code, however as discussed in the lab,
my Pycharm is preventing me from importing modules in the usual way. 
To get around this I have just put all the modules in the root and this at least allows
me to run the project. If I can get this issue corrected I will be moving the 
modules into their respective folders. 

I have only an int result returning to client for the moment, if I can have time to add a comment
to the response I will , which will include rankings 

