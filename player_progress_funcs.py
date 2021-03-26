import helper

def create_players_progress_dict(names_list):
    progress_dict = {}
    for name in names_list:
        progress_dict[name] = {}
    return progress_dict
def display_active_player(name):
    print("It is %s's turn." % name)
def iterate_active_player_index(i,players_len):
    i +=1
    if i>=players_len:
        i=0
    return i
def update_player_progress_dict(progress_dict, white_pieces):
    white_pieces_list = list(white_pieces.keys())
    for white_piece in white_pieces_list:
        progress_dict[white_piece] = white_pieces[white_piece]
    return progress_dict