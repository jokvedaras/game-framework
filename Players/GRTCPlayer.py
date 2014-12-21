__author__ = 'Greg Richards'
__author__ = 'Tara Critteden'
from random import randint
import Player
import Message
import RPSPlayerExample


class MyPlayer(Player.Player):

    def __init__(self):
        """
        :param self: this player class
        """
        Player.Player.__init__(self)    # calls superclass constructor
        self.reset()

    def play(self):
        return RpsPlayingStrategy.play(self.opponents_moves)

    def reset(self):
        self.opponents_moves = []

    def get_name(self):
        """
        :param self: this player class
        :return name: name of this player
        """
        return "Greg & Tara"

    def notify(self, msg):

        # We use notifications to store opponent's moves in past rounds
        # Process match-start and round-end messages
        # At the start of the match, clear opponent moves history since a new match has started
        # At the end of a round, append move to opponent's move history. Move history is used
        # to compute the next move played.
        if msg.is_match_start_message():
            players = msg.get_players()
            if players[0] == self or players[1] == self:
                self.reset()
        elif msg.is_round_end_message():
            players = msg.get_players()
            # Check if this message is for me and only then proceed
            if (players[0] == self) or (players[1] == self):
                # In this case, (by convention) the info is a tuple of the moves made and result
                # e.g. ((1, 0), (1,0)) which means player 1 played paper (1), the player 2 played
                # rock(0) and the result was that player 1 won (got 1 point) and player 2 lost (got 0 point)

                moves, result = msg.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if players[0] == self:
                    opponent = 1
                else:
                    opponent = 0

                # Update opponent's past moves history
                self.opponents_moves.append(moves[opponent])


# An implementation of a simple rps playing strategy
class RpsPlayingStrategy(object):

    @staticmethod
    def play(opponents_moves):
        """
        # Implements some way of predicting what the opponent might do next
        # and play accordingly.
                :return next_move: the move that we are going to make
        """

        rand = randint(1, 100)
        ##generate a random number so that we can make certain moves certain percentages of the time
        if len(opponents_moves) == 0:   # if this is going to be the first move made
            if 1 <= rand <= 40:
                next_move = 0
            elif 41 <= rand <= 65:
                next_move = 1
            else:
                next_move = 2
        elif len(opponents_moves) == 1:     # only one move was made by each player
            if opponents_moves[0] == 0:
                if rand < 20:
                    next_move = 0
                elif 20 <= rand < 66:
                    next_move = 1
                else:
                    next_move = 2
            elif opponents_moves[0] == 1:
                if rand < 20:
                    next_move = 1
                elif 20 <= rand < 66:
                    next_move = 2
                else:
                    next_move = 0
            else:
                if rand < 20:
                    next_move = 2
                elif 20 <= rand < 66:
                    next_move = 0
                else:
                    next_move = 1
        else:   # more than one move was made by each player
            rock_count = 0
            paper_count = 0
            scissors_count = 0
            x = 1
            while x < len(opponents_moves):    # only take the opponents moves into account
                if opponents_moves[x] == 0:
                    rock_count += 1
                elif opponents_moves[x] == 1:
                    paper_count += 1
                else:
                    scissors_count += 1
                x += 2
            if rock_count >= 2:
                next_move = 2
            elif paper_count >= 2:
                next_move = 0
            elif scissors_count >= 2:
                next_move = 1
            else:
                if rand <= 30:
                    next_move = 2
                elif 30 < rand <= 66:
                    next_move = 1
                else:
                    next_move = 0
        return next_move

# Test driver
# Run by typing "python3 RpsPlayerExample.py"

if __name__ == "__main__":
    player = RPSPlayerExample()
    opponent = MyPlayer()
    players = [opponent, player]
    fake_moves = (1, 2)
    fake_result = (0, 1)
    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players, fake_moves, fake_result))
