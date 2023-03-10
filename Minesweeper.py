import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        #Parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        #Create Board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        #Dug locations
        self.dug = set()
    
    #New board based on dim_size and num_bombs
    def make_new_board(self):
        #Generate Board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #Plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) #Return randint N (a <= N <= b)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == "*":
                #If already is bomb, keep going
                continue

            board[row][col] = "*" #Plant bomb
            bombs_planted += 1

        return board
    #Gives the board a grid (0, 0; 0, 1 and so on)
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    #If already bomb, skip
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
    #Check neighboring bombs
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    #Original location
                    continue
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1
        return num_neighboring_bombs
    #Dig at given location
    def dig(self, row, col):
        #No bomb = True, Bomb = Flase
        self.dug.add((row, col)) #Keep track that we dug here

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue #No need to dig where you've already dug
                self.dig(r, c)
        #If inital dig didn't hit a bomb, so shouldn't this
        return True
    #Return a string that shows the board
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        #Put this in a str
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
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

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    safe = True 
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        #if it's valid, we dig
        safe = board.dig(row, col)
        if not safe: #If dug a bomb
            break #(game over)

    if safe:
        print("Well done!")
    else:
        print("Sucks to suck doesn't it...")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

play()




