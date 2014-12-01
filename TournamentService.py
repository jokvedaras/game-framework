__author__ = "Joe Kvedaras and Collin Day"
#Set up a tournament with a game and register players
<<<<<<< HEAD
from Tournament.py import *
from AllPlayAll.py import *
=======
from AllPlayAll import *

>>>>>>> 5f124de691f103013c13249681b4e155fa1655ff

class TournamentService:

    def __init__(self):
        #Is tournament service the one to create a new tournament?
<<<<<<< HEAD
        self.tournament
        self.game

=======
        self.tournament = AllPlayAll()
        self.game = None
>>>>>>> 5f124de691f103013c13249681b4e155fa1655ff

    def register_player(self, player):
        """register a player in the current tournament"""
        if self.tournament is None:
            print("Can not add player. Tournament is null")
        else:
            self.tournament.register_player(player)
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> Tried to fix rebase issues

=======
>>>>>>> 5f124de691f103013c13249681b4e155fa1655ff

    def set_game(self, game):
        """set the game of the current tournament"""
        #Tournament initializes with a game and you can not change
        #game type afterwards
        self.game = game

<<<<<<< HEAD
    def set_tournament(self, tournament_type = None):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        if tournament_type is None:
            #AllPlayAll takes registration as a parameter. I don't think they
            #need that there
            self.tournament = AllPlayAll(self.game, None, 1000)
        else:
            self.tournament = tournament_type(self.game, None, 1000)
=======
    def set_tournament(self, tournament):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        self.tournament = tournament

    def set_display(self, display):
        if self.tournament is None:
            print("Tournament is null")
        else:
            self.tournament.attach_display(display)
>>>>>>> 5f124de691f103013c13249681b4e155fa1655ff

    def run(self):
        """Set the game and run the tournament"""
        if self.tournament is None:
            print("Can not run tournament. Tournament is null")
        else:
<<<<<<< HEAD
            self.tournament.run()
=======
            self.tournament.set_game(self.game)
            self.tournament.run()


>>>>>>> 5f124de691f103013c13249681b4e155fa1655ff
