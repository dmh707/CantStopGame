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

def run_turn():
    white_pieces = {}
    
    while True:
        if white_pieces:
            white_pieces_funcs.display_white_pieces(white_pieces)
        selection = the_round.run_round(white_pieces)
        if not selection:
            return bombed()
        print("You have selected ",end='')
        print(selection)
        white_pieces = white_pieces_funcs.add_white_pieces(white_pieces,selection)
        white_pieces_funcs.display_white_pieces(white_pieces)
        if len(white_pieces)==3:
            if not roll_again():
                helper.end_section()
                return white_pieces
        else:
            helper.enter_to_cont()
        
        

if __name__ == "__main__":
    
    run_turn()