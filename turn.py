import helper
import the_round
import white_pieces_funcs
from board import get_board_dict


def bombed():
    print("OH NO! You bombed!")
    print("Your progress from this turn will be erased.")
    helper.enter_to_cont()
    return False
def roll_again():
    return helper.yes_no_question("Would you like to roll again?")

def get_player_progress_with_max(progress):
    board_dict = get_board_dict()
    new_progress = {}
    for k,v in board_dict.items():
        position = -1
        if k in progress:
            position = progress[k]
        new_progress[k] = [position,v]
    return new_progress
def update_player_progress_with_max(progress,white_pieces):
    for col,pos in white_pieces.items():
        progress[col][0] = pos
    return progress

def run_turn(progress_dict={}):
    white_pieces = {}
    player_progress_with_max = get_player_progress_with_max(progress_dict)
    while True:
        if white_pieces:
            white_pieces_funcs.display_white_pieces(white_pieces)
        selection = the_round.run_round(white_pieces,player_progress_with_max)
        if not selection:
            return bombed()
        print("You have selected ",end='')
        print(selection)
        white_pieces = white_pieces_funcs.add_white_pieces(white_pieces,selection,player_progress_with_max)
        white_pieces_funcs.display_white_pieces(white_pieces)
        if len(white_pieces)==3:
            if not roll_again():
                helper.end_section()
                return white_pieces
        else:
            helper.enter_to_cont()
        player_progress_with_max = update_player_progress_with_max(player_progress_with_max,white_pieces)
        
        

if __name__ == "__main__":
    
    run_turn()