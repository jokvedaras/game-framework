#################################################
# 
# RPSPlayer designed to work with RPSFramework
# Created by Matt Martorana + Justin Read
#
#################################################
import Player
import Message

class MMJRPlayer(Player.Player): # took ,Observer out
    #global name
    #global rock
    #global scissors
    #global paper
    #global listOfMoves
    def __init__(self):
        Player.Player.__init__(self)
        self.name = "MattMJustinR"
        self.rock = 0
        self.scissors = 1
        self.paper = 2
        self.listOfMoves=[2]
    #c = rpyc.connect(serverAddress, 12345)

    def notify(self, message):
        #if (message[0] == Message.MatchStart)
            
        if (message.is_round_end_message()):
            players = message.get_players();
            if ((players[0] == self) or (players[1] == self)): # if we are player 1, we want player 2's move
                moves, result  = message.get_info();
                if (players[0] == self):
                    self.listOfMoves.append(moves[1])
                else:
                    self.listOfMoves.append(moves[0]) #otherwise get other move

        if (message.is_match_start_message()):
            players = message.get_players();
            
            if (players[0] == self or players[1] == self):
                self.listOfMoves = [1] # the default value is to throw scissors
    def play(self):
        return my_rps_play_strategy.play(self.listOfMoves)

    def set_history(self,listPastMoves):
        self.listOfMoves = listPastMoves

    def get_name(self):
        return "MMJRPlayer"

class my_rps_play_strategy(object):


    @staticmethod
    def play(listMoves):
        result = 0
        rock = 0
        scissors = 1
        paper = 2
        for i in range(len(listMoves)):
            result = result + (listMoves[i])
        result = result % 3
        return result
    
#def main():
    
#    player = MMJRPlayer()
#    player.set_history (['rock','scissors', 'paper', 'rock'])
#    print(player.play())

#if  __name__ =='__main__':
#    main()
