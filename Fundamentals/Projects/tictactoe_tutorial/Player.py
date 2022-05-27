import math 
import random 

class Player:
    def __init__(self,letter):
#init is a constructor for the Player class
        self.letter = letter
#self refers to the current instance of the class



class ComputerPlayer(Player):
#inheritance from the Player class
    def __init__(self, letter):
        super().__init__(letter)
#super allows for multiple inheritances from different superclasses

    def get_move(self, game): #computer picks a random move
        square = random.choice(game.available_moves()) #from the games available moves
        return square


class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game): #we want to loop till player picks a valid move
        valid_square = False #false while player hasn't picked a valid square
        val = None #this is the value of the player's square

        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8): \n") #ask the player to input their move

            try: 
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #code only reaches this point if both conditions (val and available moves) are fulfilled
            except ValueError: #error message
                print('Invalid square. Try again')

        return val


class GeniusPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves()) == 9: #at the beginning of the game, when it's your turn, choose a random square to play
            square = random.choice(game.available_moves())
        else: 
            square = self.minimax(game,self.letter)['position'] #recursively call the function till the most optimal choice has been selected and then call it from the dictionary returned from the function as position
        return square

    def minimax(self, state, player):
        max_player = self.letter #you wanna maximize yurself
        other_player = 'X' if player is 'O' else 'O' #and minimize the other player

        if state.current_winner() == other_player: #calculate the next player's chance of winning via the minimax function
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player 
            #only maximise if other player is you 
             else -1 * (state.num_empty_squares() + 1)} #minimax formula
        elif not state.num_empty_squares(): #no empty squares remaining
            return {'position': None, 'score': 0} #so return null as there was no moves

            #create your dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #set score at its lowest value as we wish to maximize
        else:
            best = {'position': None, 'score' : math.inf} # and vice versa

        for possible_move in state.available_moves():
            #make a move 
            state.make_move(player, possible_move)
            #recursively call minimax function to simulate a game
            simulated_score = self.minimax(state, other_player) #call other player to simulate their game too
            #undo your move
            state.board[possible_move] = ' '
            state.current_winner = None
            simulated_score['position'] = possible_move #update the simulated score position before passing it on as the best method possible
            #upgrade your dictionaries
            if player == max_player: #if this is the player we are trying to maximize 
                if simulated_score['score'] > best['score']: #then we have to make sure we have the best score for them
                    best = simulated_score #once we are sure, we then replace the current best score with the new best score
                elif simulated_score < best['score']: #and vice versa for the opponent
                    best = simulated_score
        return best #return the best score and position to play


           

