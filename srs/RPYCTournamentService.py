__author__ = 'joe kvedaras'

"""Using RPYC to implement distributed playing on the game-framework"""

import rpyc
from TournamentService import *

#TODO: Set up a server with rpyc and call methods in TournamentService


class RPYCTournamentService(rpyc.Service):

    def on_connect(self):
        """Called when connection is established"""
        print("Connected to server")

    def on_disconnect(self):
        """Called when connection is terminated"""
        print("Disconnected from server")

    def __init__(self):
        """Will create a player variable which will be none at startup"""
#        self.player = None
        self.tournament_service = TournamentService

    def exposed_register_player(self, player):
        """Add a remote player to the tournament"""
        self.tournament_service.register_player(player)

    def exposed_set_game(self, game):
        """set the game of the current tournament"""
        self.tournament_service.set_game(game)

    def exposed_set_tournament(self, tournament):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        self.tournament_service.set_tournament(tournament)

    def exposed_set_display(self, display):
        """set the current display type of the tournament"""
        self.tournament_service.set_display(display)

    def exposed_run(self, password):
        """Run the current tournament setup"""
        self.tournament_service.run()


#Start the game server
if __name__ == "__main__" :
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(RPYCTournamentService,port=12345,protocol_config={'allow_public_attrs':True})
    server.start()
