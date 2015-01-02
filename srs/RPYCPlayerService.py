
__author__ = 'joe kvedaras'

"""RPYC player class to be run on the client machine to connect to the
server and play games akin to rock paper scissors"""

import rpyc

#import your specific files that pertain to the game
from Players import CDJKPlayer




class RPYCPlayerService:

    def __init__(self, connection, player):
        self._player = player
        self._connection = connection


    def register_player(self):
        self._connection.register_player(self._player)



if __name__ == "__main__" :
    #Connect to game server, register player, and play the game.
    """Connect to server"""
    ip_address = str(input("Enter IP: "))
    port_number = int(input("Enter Port Number: "))
    c = rpyc.connect(ip_address, port_number)
    player = CDJKPlayer()
    player_service = RPYCPlayerService(c,player)