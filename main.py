def print_game(game_cells):
    border = '-' * 9
    print(border)
    game_rows = [game_cells[i:i+3] for i in range(0, 7, 3)]
    for i in range(3):
        print('| ' + ' '.join(game_rows[i]) + ' |')
    print(border)


def check_game(game_cells):
    row_pos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    game_rows = [''.join(cells[i] for i in pos) for pos in row_pos]
    if abs(game_cells.count('X') - game_cells.count('O')) > 1:
        return 'Impossible'
    if 'XXX' in game_rows and 'OOO' in game_rows:
        return 'Impossible'
    if 'XXX' in game_rows:
        return 'X wins'
    if 'OOO' in game_rows:
        return 'O wins'
    if ' ' not in cells:
        return 'Draw'
    return 'Game not finished'


def user_move(game_cells, game_player):
    while True:
        try:
            x, y = map(int, input('Enter the coordinates: ').split())
        except ValueError:
            print('You should enter numbers!')
        else:
            if not (1 <= x <= 3 and 1 <= y <= 3):
                print('Coordinates should be from 1 to 3!')
            elif game_cells[3 * (x - 1) + y - 1] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                game_cells[3 * (x - 1) + y - 1] = game_player
                return game_cells


cells = [' ' for _ in range(9)]
player = 'X'
while True:
    print_game(cells)
    cells = user_move(cells, player)
    state = check_game(cells)
    if state in ('X wins', 'O wins', 'Draw'):
        print_game(cells)
        print(state)
        break
    player = 'O' if player == 'X' else 'X'
