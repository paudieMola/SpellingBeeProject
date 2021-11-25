import client
import nytBee
import nytMultiPlayer


def testChooseWord():
    newBee = nytBee.nytBee.get_instance()
    chosenWord = newBee.choose_word()
    print(chosenWord)
    return chosenWord

def testClient():
    client.run()
    return

def testProcessWord():
    newBee = nytMultiPlayer.nytMPBee.get_instance()
    newBee.complett = 'a'
    newBee.register_player()
    newBee.register_player()
    print(newBee.process_word('Leave', 0))
    print(newBee.process_word('leave', 1))


testProcessWord()