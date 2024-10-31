def next_player(current_player):
    '''(str) --> (str)
    Returns the next player given the current_player.
    '''
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    
    return current_player


def check_valid_move(board, pos):
    '''(dict, int) --> (bool)
    Returns True or False if the position chosen has empty space.
    '''
    if board[pos] == '':
        return True
    else:
        return False


def check_win(board, current_player):
    '''(dict, str) --> (bool)
    Return True if current_player has won the game.
    '''
    if board[1] == current_player and board[2] == current_player and board[3] == current_player:
        return True
    elif board[4] == current_player and board[5] == current_player and board[6] == current_player:
        return True
    elif board[7] == current_player and board[8] == current_player and board[9] == current_player:
        return True
    elif board[1] == current_player and board[4] == current_player and board[7] == current_player:
        return True
    elif board[2] == current_player and board[5] == current_player and board[8] == current_player:
        return True
    elif board[3] == current_player and board[6] == current_player and board[9] == current_player:
        return True
    elif board[1] == current_player and board[5] == current_player and board[9] == current_player:
        return True
    elif board[3] == current_player and board[5] == current_player and board[7] == current_player:
        return True
    else:
        return False


def check_draw(num_moves):
    '''(int) --> (bool)
    Return True or False given the total number of moves played given by num_moves.
    '''
    if num_moves < 9:
        return False
    else:
        return True
