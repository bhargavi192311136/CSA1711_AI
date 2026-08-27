def print_board(board):
    for i in range(0,9,3):
        print(board[i:i+3])

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]
    return None

def play():
    board = [" "]*9
    turn = "X"
    for _ in range(9):
        print_board(board)
        move = int(input(f"{turn}'s move (0-8): "))
        if board[move]==" ":
            board[move]=turn
            if check_winner(board):
                print_board(board)
                print(turn,"wins!")
                return
            turn = "O" if turn=="X" else "X"
    print("Draw!")

play()
