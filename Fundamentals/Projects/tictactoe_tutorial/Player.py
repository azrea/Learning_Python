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