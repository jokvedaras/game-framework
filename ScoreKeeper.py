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
        for player in players:
            listitem = ScoreKeeperListItem.ScoreKeeperListItem(player)
            if not self.check_player(listitem):
                self.leaderboard.append(listitem)

        self.make_winner(winner)


    def check_player(self, player):
        """
        checks each player in leaderboard to see if they are
        already counted for.
        :param player -- item to check against known players
        :return:true if player is already on the list, false otherwise

        """
        check = False

        for p in self.leaderboard:
            if p.get_player() == player.get_player():
                check = True

        return check


    def make_winner(self, winner):
        """
        finds the reference to the player and increments his score
        :param winner who won match
        """

        for i in range(len(self.leaderboard)):
            #if player is i.get_player():
            #   i.update_score()
            if winner is self.leaderboard[i].get_player():
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


    def print_leaderboard(self):

        player_list = []

        for player in self.leaderboard:
            player_list.append(player.get_player().get_name())

        print(len(self.matchhistory))
        print(len(self.leaderboard))
        return player_list

    def print_scores(self):

        score_list = []

        for player in self.leaderboard:
            score_list.append(player.get_score())

        return score_list


    def print_final_stats(self):
        player_list = []
        score_list = []
        for player in self.leaderboard:
            player_list.append(player.get_player().get_name())
            score_list.append(player.get_score())
        print("Total number of matches played:")
        print(len(self.matchhistory))
        print("Number of players that participated")
        print(len(self.leaderboard))
        print(player_list)
        print(score_list)

        templeaderboard = player_list.copy()
        tempscores = score_list.copy()

        print("The top three are:")
        for i in range(0, 3):
            print(templeaderboard[tempscores.index(max(tempscores))])
            templeaderboard.remove(templeaderboard[tempscores.index(max(tempscores))])
            tempscores.remove(tempscores[tempscores.index(max(tempscores))])
