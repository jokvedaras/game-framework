__author__ = 'jeffrey creighton & anand patel'
# Purpose: to collect and store scores from all players and matches
import ScoreKeeperHistoryItem
import ScoreKeeperListItem


class ScoreKeeper:
    """
    Consisting of two lists, will track all players and their scores
        as well as each match and their outcomes.
    """
    leaderboard = []
    matchhistory = []

    def __init__(self):
        self.leaderboard = []
        self.matchhistory = []


    def update_tournament(self, p1, p2, w, s1, s2):
        """
        updates the leaderboard and matchhistory lists
        :param p1: player1
        :param p2: player2
        :param w: winner of match
        :param s1: score of player1
        :param s2: score of player2
        :return:

        """
        #creates the history item based on the match details
        historyitem = ScoreKeeperHistoryItem.ScoreKeeperHistoryItem(p1, p2, w, s1, s2)

        #adds the history item to matchhistory[]
        self.matchhistory.append(historyitem)

        #creates the listitems for both players and checks to see if they are on the leaderboard
        #if not present on the leader board, they are appended
        listitema = ScoreKeeperListItem.ScoreKeeperListItem(p1, s1)
        listitemb = ScoreKeeperListItem.ScoreKeeperListItem(p2, s2)
        if self.check_player(listitema):
            self.leaderboard.append(listitema)
        if self.check_player(listitemb):
            self.leaderboard.append(listitemb)

        #checks the winner and awards a point to that player
        if s1 > s2:
            self.make_winner(p1)
        elif s2 > s1:
            self.make_winner(p2)
        #in the event of a tie, no points awarded
        else:
            pass


    def check_player(self, player):
        """
        checks each player in leaderboard to see if they are
        already counted for.
        :param item -- item to check against known players
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
