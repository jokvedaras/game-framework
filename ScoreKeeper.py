__author__ = 'jeffrey creighton & anand patel'
# Purpose: to collect and store scores from all players and matches
import ScoreKeeperHistoryItem
import ScoreKeeperListItem


class ScoreKeeper(object):
    """
    Consisting of two lists, will track all players and their scores
        as well as each match and their outcomes.
    """
    leaderboard = []
    matchhistory = []

    def __init__(self):
        self.leaderboard = []
        self.matchhistory = []


    def update_tournament(self, players, winner, scores):
        """
        :param players: list of players
        :param winner: winner of match
        :param scores: list of scores
        """
        #creates the history item based on the match details
        historyitem = ScoreKeeperHistoryItem.ScoreKeeperHistoryItem(players, winner, scores)

        #adds the history item to matchhistory[]
        self.matchhistory.append(historyitem)

        #creates the listitems for both players and checks to see if they are on the leaderboard
        #if not present on the leader board, they are appended
        for i in range(len(players)):
            listitem = ScoreKeeperListItem.ScoreKeeperListItem(players[i])
            if self.check_player(listitem):
                self.leaderboard.append(listitem)

            #checks the winner and awards a point to that player
            if(players[i] is winner):
                self.make_winner(players[i])
            #in the event of a tie, no points awarded
            else:
                pass


    def check_player(self, player):
        """
        checks each player in leaderboard to see if they are
        already counted for.
        :param player -- item to check against known players
        :return:true if player is already on the list, false otherwise

        """
        check = True
        for i in range(len(self.leaderboard)):
            if self.leaderboard[i].get_player() == player.get_player():
                check = False
            else:
                check = True
        return check


    def make_winner(self, player):
        """
        finds the reference to the player and increments his score
        :param player who won match
        """
        for i in range(len(self.leaderboard)):
            #if player is i.get_player():
            #   i.update_score()
            if player is self.leaderboard[i].get_player():
                self.leaderboard[i].update_score()

    def get_leaderboard(self):
        """
        :return: the leaderboard
        """
        return self.leaderboard

    def get_matchhistory(self):
        """
        :return: the match history
        """
        return self.matchhistory

    def get_final_three(self):
        """
        :return: Top three scoring players of the Tournament
        """
        player_list =[]
        player_list.append(self.leaderboard[0].get_player().get_name())
        player_list.append(self.leaderboard[1].get_player().get_name())
        player_list.append(self.leaderboard[2].get_player().get_name())

        return player_list