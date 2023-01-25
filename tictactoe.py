board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('---------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('---------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def make_move(player, row, col):
    if row > 2 or col > 2:
        print("Invalid move!")
        return
    if board[row][col] != ' ':
        print("That space is already occupied!")
        return
    board[row][col] = player

def has_won(player):
    # check rows
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # check cols
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def main():
    player = 'X'
    while True:
        draw_board()
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        make_move(player, row, col)
        if has_won(player):
            print(player + " has won!")
            break
        player = 'O' if player == 'X' else 'X'

main()
