__author__ = 'jeffrey creighton & anand patel'
# Purpose: data structure for tracking match history


class ScoreKeeperHistoryItem:
    """
    data structure to maintain a record of all matches
    and their outcomes
    """
    def __init__(self, player1, player2, winner, score1, score2):

        self.player1 = player1
        self.player2 = player2
        self.winner = winner
        self.score1 = score1
        self.score2 = score2