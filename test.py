import client
import nytBee

def testChooseWord():
    newBee = nytBee.nytBee
    newBee = newBee.get_instance()
    chosenWord = newBee.choose_word()
    print(chosenWord)
    return chosenWord



def testClient():
    client.run()
    return

testClient()