

def play_turn(game_board: list, col: int, row: int, piece: str):
    if game_board[row][col] == "":
        game_board[row][col] = piece
        return True
    else:
        return False
    
            
        
game_board = [["","",""], ["","",""], ["","",""]]
print(play_turn(game_board, 2, 0, 'X'))
print(play_turn(game_board, 2, 0, 'o'))
print(play_turn(game_board, 1, 1, 'o'))
print(game_board)