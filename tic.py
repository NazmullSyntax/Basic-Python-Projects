board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]}|{board[i+1]}|{board[i+2]}")

def check_win():
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

player = 'X'
while True:
    print_board()
    pos = int(input(f"Player {player}, choose position (1-9): ")) - 1
    
    if board[pos] == ' ':
        board[pos] = player
        winner = check_win()
        if winner:
            print_board()
            print(f"{winner} wins!")
            break
        if ' ' not in board:
            print_board()
            print("Tie!")
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print("Position taken!")