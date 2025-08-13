

def who_won(game_board: list):
    player1_count = 0
    player2_count = 0
    for i in game_board:
        if i == 0:
            continue
        elif i == 1:
            player1_count += 1
        elif i == 2:
            player2_count += 1
    if player1_count > player2_count:
        return 1
    elif player2_count > player1_count:
        return 2
    elif player2_count == player1_count:
        return 0

game_board = [0,0,0,1,1,1,0,0,2,2,2,2]
result = who_won(game_board)
print(result)
