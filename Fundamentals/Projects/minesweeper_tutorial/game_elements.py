import random
class Board: 
    def __init__(self, board_size, num_bombs):
        self.board_size = board_size
        self.num_bombs = num_bombs
        self.dug = set()
        self.board = self.make_new_board()
        self.assign_values_to_board()
    
    def make_new_board(self):
        #create a new board based on the board size and the number of bombs
        board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)] #creates a 2d board with rows and columns

        #plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs: #unknown when loop will end
            bomb_location = random.randint(0, self.board_size ** 2 -1)
            row = bomb_location // self.board_size
            col = bomb_location % self.board_size
            if board[row][col] == '*': #bomb planted already
                continue #so skip it
            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.board_size): #loop through the rows
            for c in range(self.board_size): #loop through every column on each row
                if self.board[r][c] == '*': #if the cell is a bomb 
                    continue #then skip it
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)

    def get_num_neighbouring_bombs(self,row,col):
        num_of_neighbouring_bombs = 0

        for r in range(max(0,row - 1), min(self.board_size - 1,(row + 1)) + 1): #max and min is used to ensure that our values don't go out of bounds
            for c in range(max(0,col - 1), min(self.board_size - 1,(col + 1))+1): #cycle through the entire 3x3 array around our square
                if r == row and c == col: #we dont want to count our own square 
                    continue
                if self.board[r][c] == '*': 
                    num_of_neighbouring_bombs += 1
        return num_of_neighbouring_bombs

    def dig(self, row, col):


        self.dug.add((row,col))

        if self.board[row][col] == '*':
            return False # to set up loss condition
        elif self.board[row][col] > 0: #once there is a neighbouring bomb stop recursion
            return True

        for r in range(max(0,row -1),min(self.board_size - 1,(row + 1)) + 1):
            for c in range(max(0,col - 1),min(self.board_size - 1,(col + 1)) + 1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c) #recursively digging till there is a neighbouring bomb


        return True

    def __str__(self):
        visible_board = [[None for _ in range (self.board_size)] for _ in range (self.board_size)]
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.board_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.board_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.board_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
