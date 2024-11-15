# Function to convert the input string into a 9x9 grid
def string_to_board(input_str):
    board = []
    for i in range(0, 81, 9):  # Split the string into rows of length 9
        row = list(
            map(int, input_str[i : i + 9])
        )  # Convert each character to an integer
        board.append(row)
    return board


# Function to check if placing num at grid[row][col] is valid
def is_valid(board, row, col, num):
    # Check if the number exists in the current row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number exists in the current column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number exists in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


# Function to solve the Sudoku using backtracking
def solve_sudoku(board):
    # Find the next empty cell (marked by 0)
    empty_cell = find_empty_cell(board)

    # If no empty cell is found, the Sudoku is solved
    if not empty_cell:
        return True

    row, col = empty_cell

    # Try digits 1-9 for the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            # Recursively try to solve the next cell
            if solve_sudoku(board):
                return True
            # Backtrack if the choice doesn't lead to a solution
            board[row][col] = 0

    return False  # If no number can fit, return False


# Function to find the next empty cell (returning (row, col))
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


# Function to print
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))


# Main program
if __name__ == "__main__":
    input_str = input("Enter the Sudoku puzzle as a single string (81 digits): ")

    if len(input_str) < 81:
        input_str += "0" * (81 - len(input_str))
    elif len(input_str) > 81:
        input_str = input_str[:81]

    sudoku_board = string_to_board(input_str)

    # Print the original Sudoku puzzle
    print("Original Sudoku Puzzle:")
    print_board(sudoku_board)

    # Solving the Sudoku
    if solve_sudoku(sudoku_board):
        print("Solved Sudoku:")
        print_board(sudoku_board)
    else:
        print("No solution exists!")


# Test case : 530070000600195000098000060800060003400803001700020006060000280000419000000080079
# output:

# Original Sudoku Puzzle:
# 5 3 0 0 7 0 0 0 0
# 6 0 0 1 9 5 0 0 0
# 0 9 8 0 0 0 0 6 0
# 8 0 0 0 6 0 0 0 3
# 4 0 0 8 0 3 0 0 1
# 7 0 0 0 2 0 0 0 6
# 0 6 0 0 0 0 2 8 0
# 0 0 0 4 1 9 0 0 0
# 0 0 0 0 8 0 0 7 9

# Solved Sudoku:
# 5 3 4 6 7 8 9 1 2
# 6 7 2 1 9 5 3 4 8
# 1 9 8 3 4 2 5 6 7
# 8 5 9 7 6 1 4 2 3
# 4 2 6 8 5 3 7 9 1
# 7 1 3 9 2 4 8 5 6
# 9 6 1 5 3 7 2 8 4
# 2 8 7 4 1 9 6 3 5
# 3 4 5 2 8 6 1 7 9