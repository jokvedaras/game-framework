__author__ = 'jeffrey creighton & anand patel'
# Purpose: data structure for tracking tournament leaders and
# act as a roster of all players


class ScoreKeeperListItem:
    """
    keeps record of each player and their associated
    number of wins, can access all of the data fields
    """
    def __init__(self, player):
        self.player = player
        self.score = 0

    def update_score(self):
        """
        :increment the variable score
        : to signify a win for the player
        """
        self.score += 1


    def get_score(self):
        """
        :return: number of wins associated with this player
        """
        return self.score

    def get_player(self):
        """
        :return: the instance of player it is tracking
        """
        return self.player