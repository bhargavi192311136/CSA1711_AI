def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            solve_n_queens(n, row+1, board+[col])

solve_n_queens(8)
