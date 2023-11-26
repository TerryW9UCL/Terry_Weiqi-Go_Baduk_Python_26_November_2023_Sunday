def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()

def place_stone(board, player, row, col):
    if board[row][col] != '.':
        print('Invalid move. Position already occupied.')
        return False
    board[row][col] = player
    return True

def check_liberties(board, row, col, player):
    liberties = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        adjacent_row = row + dy
        adjacent_col = col + dx
        if 0 <= adjacent_row < 19 and 0 <= adjacent_col < 19 and board[adjacent_row][adjacent_col] == '.':
            liberties += 1
    return liberties

def capture_stones(board, player):
    captured_stones = []
    for row in range(19):
        for col in range(19):
            if board[row][col] == opponent(player):
                liberties = check_liberties(board, row, col, opponent(player))
                if liberties == 0:
                    board[row][col] = '.'
                    captured_stones.append((row, col))
    return captured_stones

def opponent(player):
    if player == 'B':
        return 'W'
    else:
        return 'B'

def check_ko(board, row, col, player):
    captured_stones = capture_stones(board, player)
    if len(captured_stones) == 1 and captured_stones[0] == (row, col):
        return True
    return False

def check_game_over(board):
    black_stones = 0
    white_stones = 0
    for row in board:
        for cell in row:
            if cell == 'B':
                black_stones += 1
            elif cell == 'W':
                white_stones += 1
    if black_stones == 0 and white_stones == 0:
        return True
    else:
        return False

def play_game():
    board = [['.' for _ in range(19)] for _ in range(19)]
    current_player = 'B'

    while True:
        display_board(board)

        row = int(input('Enter row (0-18): '))
        col = int(input('Enter column (0-18): '))

        if not place_stone(board, current_player, row, col):
            continue

        captured_stones = capture_stones(board, current_player)
        if check_ko(board, row, col, current_player):
            print('Ko move. Stone cannot be placed.')
            board[row][col] = '.'
            continue

        if check_game_over(board):
            print('Game over!')
            break

        current_player = opponent(current_player)

if __name__ == '__main__':
    play_game()