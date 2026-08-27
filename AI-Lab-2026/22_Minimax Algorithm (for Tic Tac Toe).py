def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner=="X": return 1
    if winner=="O": return -1
    if " " not in board: return 0

    if is_max:
        best = -999
        for i in range(9):
            if board[i]==" ":
                board[i]="X"
                best = max(best, minimax(board, depth+1, False))
                board[i]=" "
        return best
    else:
        best = 999
        for i in range(9):
            if board[i]==" ":
                board[i]="O"
                best = min(best, minimax(board, depth+1, True))
                board[i]=" "
        return best
