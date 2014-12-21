from Players import CDJKPlayer

__author__ = 'jokvedaras'

"""RPYC player class to be run on the client machine to connect to the
server and play games akin to rock paper scissors"""

import rpyc

#import your specific files that pertain to the game
from Players import CDJKPlayer

class RPYCPlayerService(rpyc.Service):

    def on_connect(self):
        """Called when connection is established"""
        print("Connected to server")

    def on_disconnect(self):
        """Called when connection is terminated"""
        print("Disconnected from server")

    def __init__(self):
        """Will create a player variable which will be none at startup"""
        self.player = None

    def exposed_get_name(self,player):
        """Return the name of the player"""
        return player.get_name()

    def exposed_play(self,player):
        """Calls player to "play" or make a move"""
        return player.play()


    def exposed_notify(self,message):
        """Notifies a player with the servers message"""
        self.player.notify(message)

    def exposed_get_player(self):
        #use the particular player on computer
        self.player= CDJKPlayer()
        return

    def exposed_start_player_service(self):
        return None

#Start the local server to communicated with the game server
if __name__ == "__main__" :
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(RPYCPlayerService,port=12345,protocol_config={'allow_public_attrs':True})
    server.start()