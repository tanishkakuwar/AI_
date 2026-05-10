print("N-QUEEN PROBLEM USING BACKTRACKING")
# n: size of the board (num of queens)
# board: 1D list storing the column
# row: current row
# col: current column

# Function to print board
def print_board(board, n):

    print("\nSolution:\n")

    for i in range(n):      # 'i' -> ROW
        for j in range(n):  # 'j' -> COLUMN

# "If curr column we are printing (j) matches the column stored in our list for this row (board[i]), then print a Q.
            if board[i] == j:
                print("Q", end=" ")
            else:
                print("_", end=" ")

        print()


# Check if queen placement is safe
def is_safe(board, row, col):

    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Left or right diagonal
        # c1 - c2 == r1 - r2
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve(board, row, n):

    # All queens placed
    if row == n:
        return True

    # Try all columns
    for col in range(n):

        if is_safe(board, row, col):

            board[row] = col

            # Recursive call
            if solve(board, row + 1, n):
                return True

    return False


# -------- MAIN --------

n = int(input("Enter value of N: "))

board = [-1] * n

if solve(board, 0, n):

    print_board(board, n)

else:
    print("Solution does not exist")