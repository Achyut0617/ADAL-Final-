def print_board(board):
    for row in board:
        line = ""
        for cell in row:
            if cell == 1:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


def is_safe(board, row, col, n):
    # check left in row
    for j in range(col):
        if board[row][j] == 1:
            return False

    # check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueen(board, col, n, solutions):
    if col == n:
        solutions.append([row[:] for row in board])
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueen(board, col + 1, n, solutions)
            board[row][col] = 0  # backtrack


# ---- MAIN ----
n = 4
board = [[0]*n for _ in range(n)]
solutions = []

solve_nqueen(board, 0, n, solutions)

# We print ONLY the first solution = the one you want
print("Required 4-Queen Solution:\n")
print_board(solutions[0])
