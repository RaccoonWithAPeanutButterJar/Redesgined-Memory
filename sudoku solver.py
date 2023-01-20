def find_next_empty(puzzle):
    #find the next row, col on the puzzle that is empty = -1
    #return row, col tuple (or (None, None) if there is none)
    
    # indices go from 0-8
    for r in range(9):
        for c in range(9): #range(9) is 0,1,2....8
            if puzzle[r][c] == -1:
                return r, c
    return None, None #if no empty (-1) spaces left

def is_valid(puzzle, guess, row, col):
    #figures out if guess is valid
    #returns True if so, otherwise False

    #start with row check
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #column check
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #THE SQAURE CHECK
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    #if we make it here then the guess is valid
    return True



def solve_sudoku(puzzle):
    # solve using backtracking
    # puzzle = list of lists, each inner list is a row in the sudoku
    # return wether solution exists

    #step 1: choose where to start
    row, col = find_next_empty(puzzle)

    # step 1.1: if nothing's left, then we're done, bcs only allowed valid inputs
    if row is None:
        return True

    #step 2: if there is a place where to put a guess, then make a guess (1-9)
    for guess in range(1, 10): #range(1, 10) is 1,2,3....9
        #step 3: check if this guess is valid
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if valid, then place
            puzzle[row][col] = guess
            #step 4: now recurse using the new puzzle field
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid OR if guess doesn't solve then backtrack
        puzzle[row][col] = -1 #reset the guess

    #step 6: if no numbers work, then puzzle = unsolvable
    return False
