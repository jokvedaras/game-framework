__author__ = 'jeffrey creighton & anand patel'
# Purpose: data structure for tracking match history


class ScoreKeeperHistoryItem:

    def __init__(self, players, winner, scores):
        """
        data structure to maintain a record of all matches
            and their outcomes
        :param players: list of players participated
        :param winner: player who won
        :param scores: resulting scores
        :return:
        """
        self.players = players
        self.winner = winner
        self.scores = scores