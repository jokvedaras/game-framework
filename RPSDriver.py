__author__ = 'Tony'

from TournamentService import *
from RPSGame import *
from Display import *
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


# Produces a list of players submitted
def create_players():
    return [BEPCPlayer(), CDJKPlayer(), DWPMPlayer(),MyPlayer(),GSACPlayer(),MMJRPlayer(),PBATPlayer(),
            VMPlayer(), SHJPPlayer(), JCAPPlayer()]

# Create a tournament service that will set the tournament accordingly, register the players to the tournament
# and run the instance of Tournament
class RPSDriver(TournamentService):

    def __init__(self):
        TournamentService.__init__(self)

    def register_players(self, player_list):
        for player in player_list:
            self.register_player(player)

if __name__ == "__main__":
    driver = RPSDriver()
    players = create_players()
    rps = RPSGame()
    driver.register_players(players)
    driver.set_game(rps)
    driver.set_display(Display())
    driver.run()










