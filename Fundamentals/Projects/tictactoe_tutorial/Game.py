import time
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # means that for 9 spaces " " should be allocated. _ means a value that isnt neccessary
        self.current_winner = None #keeps track of the current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # the equation is a range between min_number : max_number
            print("| " + " | ".join(row) + " |")
    

    @staticmethod #static as self does not need to be passed down
    def print_board_nums(): #prints an array with the numbers visible
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] #assigns numbers to spots on the array
        for row in number_board:
            print('| ' + " | ".join(row) + " |")

    def available_moves(self): #returns the index of the available moves
        return [i for i, spot in enumerate(self.board) if spot == " "] #this is the method below but in shorthand
        # moves = []
        # for (i,spot) in enumerate(self.board): #enumerate adds a counter as it iterates through the list given
        #     if spot == ' ': #spot is the actual item of the list being enumerated
        #         moves.append(i) #i represents the enumerator counter
        # return moves

    def empty_squares(self):
        return ' ' in self.board #this is supposed to return a True if a blank space is found

    def num_empty_square(self):
        return len(self.available_moves()) # we could also say self.board.count(' ') 

    def make_move(self, square,letter): #this function makes the actual move after a letter is chosen
        if self.board[square] == ' ': #if the space on the board is empty 
            self.board[square] = letter #then we can just make the move
            if self.winner(square,letter): #we can check for the winner here after the move as it is when you normally would win
                self.current_winner = letter

            return True
        else: return False  #else we can return false to show something is wrong

    def winner(self,square,letter): #check for a winner 
        #first we check the row 
        row_ind = square // 3 #this tells the player which row the square that has been changed is in
        row = self.board[row_ind*3 : (row_ind + 1) * 3] #creates an array of every array index in that row
        if all([spot == letter for spot in row]): #if every letter in that row is equal to the letter provided then return true
            return True
        #then the column
        col_ind = square % 3  #column value
        column = [self.board[col_ind+i*3] for i in range(3)] #all indexes in the column
        if all([spot == letter for spot in column]): #checking all values in the column are a single letter
            return True

        #then diagonals
        if square % 2 == 0: #all diagonals are even values 0,2,4,6,8
            diagonal1 = [self.board[i] for i in [0,4,8]] #all array indexes for one diagonal possibility
            if all([spot == letter for spot in diagonal1]): 
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False # if all checks fail then there are no wins so return false
        

    def play(self,game,x_player, o_player):
        game.print_board_nums()

        letter = 'X'

        while game.empty_squares():
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)
            
            if game.make_move(square,letter): #if the move was succesfully made
                print(letter + f' makes a move to square {square}') 
                game.print_board() #print the board so we can see the letter on the board
                print('') #empty line for some spacing

                if game.current_winner:
                    print(letter + ' wins!')
                    return letter
            #after the move we need to alternate players
            letter = 'O' if letter == 'X' else 'X' # switches player: basically the same as a if else statement
            time.sleep(1.5) #adds a tiny pause
        print("it's a tie.") #working on the assumption that for it to come out of the loop and fail the if at the top there was no winner and yet the game still ended