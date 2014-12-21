__author__ = 'jeffrey creighton & anand patel'
import random
import Player
import Message


class JCAPPlayer(Player.Player):
    def __init__(self):
        self.name = "JCAP"
        self.moves = [0, 0, 0]
        self.pre_smart = 3
        self.decrementing = 45


    # Decide to make a smart or random move and
    # return  the final decision
    def choose(self):
        if self.pre_smart > 0:
            choice = self.explore()
            self.pre_smart = - 1
        else:
            if random.randint(1, 100) < self.decrementing:
                choice = self.explore()
            else:
                choice = self.exploit()
            # to always have at least  a 5% random selection rate
            if self.decrementing > 5:
                self.decrementing = - 1
        return choice


    # Make a random move
    def explore(self):
        return random.randint(0, 2)


    # Make an educated guess
    def exploit(self):
        # If values are all tied for 'goodness' make a random move
        if self.moves[0] == self.moves[1] and self.moves[0] == self.moves[2]:
            return self.explore()
        else:
            # Otherwise make the move with the best goodness
            return self.moves.index(max(self.moves))


    # Return instance variable 'name'
    def get_name(self):
        return self.name

    # Set instance variable 'name'
    def set_name(self, playername):
        self.name = playername

    # Get messages of previous moves or alert of new game
    def notify(self, message):
        # If new match, reset variables from previous match
        if message.is_match_end_message():
            self.reset()
        # If end of game, collect opponents' move
        elif message.is_round_end_message():
            players = message.get_players()
            result = message.get_info()[0]
            if players[0] == self.get_name():
                self.moves[int(result[0])] = self.moves[int(result[0])] + 1
            elif players[1] == self.get_name():
                self.moves[int(result[1])] = self.moves[int(result[1])] + 1
        else:
            pass

    #reset variables for new match
    def reset(self):
        self.moves = [0, 0, 0]
        self.pre_smart = 3
        self.decrementing = 25

    # Returns either 0, 1, or 2
    def play(self):
        return self.choose()
