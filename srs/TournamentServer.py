__author__ = 'joe kvedaras'

"""Handle the communication between our server and the game-framework code"""

from TournamentService import *

#TODO: set a server password so only an admin can start the tournament

class TournamentServer():

    def __init__(self):
        self.tournament = TournamentService()
        self.password = "master"

    def register_player(self, player):
        """Add a remote player to the tournament"""
        self.tournament.register_player(player)

    def set_game(self, game):
        """set the game of the current tournament"""
        self.tournament.set_game(game)

    def set_tournament(self, tournament):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        self.tournament.set_tournament(tournament)

    def set_display(self, display):
        """set the current display type of the tournament"""
        self.tournament.set_display(display)

    def run(self):
        """Run the current tournament setup"""
        self.tournament.run()

    def reset(self):
        """close the current tournament and start a new one"""
        self.tournament = TournamentService()