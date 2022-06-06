from game_elements import Board
import re

def play(board_size = 10, num_bombs = 10):
    #Step 1 : create the board and plant the bombs 
    board = Board(board_size,num_bombs)

    # Step 2 : show the user the board and ask where they want to dig

    # Step 3 : if location is a bomb show game over message and end the game
    # Step 3b : if location is not a bomb dig recursively till each square is next to a bomb
    # Step 4 : repeat steps 2 and 3b till all non bomb locations are found
    safe = True #variable to maintain the loop
    while(len(board.dug) < board.board_size ** 2 - num_bombs): #while the number of dug locations is less than the number of free locations on the board
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: ")) #divides the row and column by comma -- the two dashes and s is used to negate whitespace -- the * just says multiple whitespaces can be negated

        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= board.board_size or col < 0 or col >= board.board_size:
            print('Invalid location. Try again') 
            continue # gate check invalid characters

        safe = board.dig(row,col)
        if not safe: 
            break

    if safe: 
        print('You won! Yakitoriiiii!')
    else:
        print('Sorry. Game over!')
        board.dug = [(row,col) for row in range(board.board_size) for col in range(board.board_size)] #show the entire board

        print(board)

if __name__ == '__main__':
    play()
