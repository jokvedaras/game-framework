 # Greg Suner and Alex Ciarmella
 # Concrete Player Class

import Player
import Message
 
class GSACPlayer(Player.Player):
 
    def __init__(self):
        # Call super class constructor
        Player.Player.__init__(self)
        self.reset()
	
    def play(self):
        return RpsPlayingStrategy.play(self.opponents_moves)
			
    def reset(self):
        self.opponents_moves = []
		
    def get_name(self):
        return self.name
		
    def set_name (self, playername):
        self.name = playername
	
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
                # In this case, (by convention) the info is a tuple of the moves made and result e.g. ((1, 0), 1) which
                # means player 1 played paper (1), the player 2 played rock(0) and the result was that
                # player 1 won

                moves, result = msg.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if players[0] == self:
                    opponent = 1
                else:
                    opponent = 0

                # Update opponent's past moves history
                self.opponents_moves.append(moves[opponent])	
	
class RpsPlayingStrategy(object):
		
		#Decides next move based on opponents past moves
		#Looks for what opponent throws the most and tries to counter it. 0-rock, 1-paper, 2-scissors
		#Takes list of opponents past moves
		def play(pastmoves):
			rock, paper, scissors = 0, 0, 0
			
			for index, move in enumerate(pastmoves):

					if move == 0:
						rock += 1
					elif move == 1:
						paper += 1
					else:
						scissors += 1
			else:
				return 0
			
			#Look for most thrown move and throw counter
			if rock > paper and rock > scissors:
				return 0
			elif paper > rock and paper > scissors:
				return 2
			elif scissors > rock and scissors > paper:
				return 1
			else: #Arbitrary throw if 2 or 3 are thrown evenly
				return 0
				


# Test driver
# Run by typing "python3 GSACPlayer.py"

if __name__ == "__main__":
    player = GSACPlayer()
    opponent = GSACPlayer()
    players = [opponent,player]
    fakeinfo = ((0,1),1)
    fakeresult = 1
    fakemoves = (1,2)

    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print ("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players,fakemoves,fakeresult))