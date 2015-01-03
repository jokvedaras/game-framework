__author__ = 'joe kvedaras'

"""Using RPYC to implement distributed playing on the game-framework"""

import rpyc
from TournamentServer import *



class RPYCTournamentService(rpyc.Service):

    def on_connect(self):
        """Called when connection is established"""
        print("Connected to server")

    def on_disconnect(self):
        """Called when connection is terminated"""
        print("Disconnected from server")

    def exposed_register_player(self, player):
        """Add a remote player to the tournament"""
        print(player.get_name())
        tournament_service.register_player(player)

    def exposed_set_game(self, game):
        """set the game of the current tournament"""
        tournament_service.set_game(game)

    def exposed_set_tournament(self, tournament):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        tournament_service.set_tournament(tournament)

    def exposed_set_display(self, display):
        """set the current display type of the tournament"""
        tournament_service.set_display(display)

    def exposed_run(self):
        """Run the current tournament setup"""
        tournament_service.run()


#Start the game server
if __name__ == "__main__" :
    from rpyc.utils.server import ThreadedServer
    from threading import Thread

    tournament_service = TournamentServer()


    server = ThreadedServer(RPYCTournamentService, port=12345,protocol_config = {"allow_public_attrs" : True})

    server.start()
"""
    t = Thread(target = server.start)
    t.daemon = True
    t.start()
"""



