
__author__ = 'joe kvedaras'

"""RPYC player class to be run on the client machine to connect to the
server and play games akin to rock paper scissors"""

import rpyc
import RPSGame
from Display import *



#import your specific files that pertain to the game
#Add library path of players
import sys
sys.path.append("/Users/jokvedaras/git/game-framework/Players")
from CDJKPlayer import *
from BEPCPlayer import *
from DWPMPlayer import *


class RPYCPlayerService:

    def __init__(self, connection):
        self._connection = connection


    def register_player(self, player):
        self._connection.root.register_player(player)



if __name__ == "__main__" :
    #Connect to game server, register player, and play the game.
    """Connect to server"""
#    ip_address = str(input("Enter IP: "))
#    port_number = int(input("Enter Port Number: "))
#    c = rpyc.connect(ip_address, port_number)
    c = rpyc.connect("localhost",12345, config = {"allow_public_attrs" : True})
    player = CDJKPlayer()
    player2 = BEPCPlayer()
    player3 = DWPMPlayer()



    rps = RPSGame.RPSGame()
    #Set up tournament
    c.root.set_game(rps)
    c.root.set_display(Display())

    #register 2 players
    print("Registered player 1")
    c.root.register_player(player)
    print("Registered player 2")
    c.root.register_player(player2)
    c.root.register_player(player3)

    print("Running Server")
    c.root.run()

    c.close()

#    player_service = RPYCPlayerService(c,player)
#    player_service.register_player()


