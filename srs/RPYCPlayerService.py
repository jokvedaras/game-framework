
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
from BEPCPlayer import *
from CDJKPlayer import *
from DWPMPlayer import *
from GRTCPlayer import *
from GSACPlayer import *
from MMJRPlayer import *
from PBATPlayer import *
from VMPlayer import *
from SHJPPlayer import *
from JCAPPlayer import *


class RPYCPlayerService:

    def __init__(self, connection_root):
        self.connection_root = connection_root


    def register_player(self, player):
        self._connection.root.register_player(player)

    # Produces a list of players submitted
    def create_players(self):
        #,GSACPlayer() This player needs to be fixed
        return [BEPCPlayer(), CDJKPlayer(), DWPMPlayer(),MyPlayer(),MMJRPlayer(),PBATPlayer(),
            VMPlayer(), SHJPPlayer(), JCAPPlayer()]


    def create_player(self, player):
        """register your specific player"""
        self.connection_root.register_player(player)

    def register_players(self, player_list):
        for player in player_list:
            self.connection_root.register_player(player)

    def set_up_game(self, game, display):
        self.connection_root.set_game(game)
        self.connection_root.set_display(display)

    def run(self):
        self.connection_root.run()

if __name__ == "__main__" :
    #Connect to game server, register player, and play the game.
    """Connect to server"""
#    ip_address = str(input("Enter IP: "))
#    port_number = int(input("Enter Port Number: "))
#    c = rpyc.connect(ip_address, port_number)
    conn = rpyc.connect("localhost",12345, config = {"allow_public_attrs" : True})
    c = conn.root

    game_service = RPYCPlayerService(c)
    rps = RPSGame.RPSGame()
    display = Display()
    player = CDJKPlayer()


    game_service.set_up_game(rps, display)
    #register all players for testing
    game_service.register_players(game_service.create_players())
    game_service.run()

    conn.close()



