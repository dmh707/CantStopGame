import helper
from round import *

def add_new_white_pieces_loop(new_white_pieces, white_pieces):
    for i in new_white_pieces:
        if i not in white_pieces:
            white_pieces[i] = 1
        else:
            iterate_white_piece(i,white_pieces)
    return white_pieces
def iterate_white_piece(num,white_pieces):
    assert num in white_pieces
    white_pieces[num] +=1
    return white_pieces
def select_one_new_white_pieces(new_white_pieces):
    print("You only have 1 white piece left. Which sum would you like to use?")
    helper.print_unnumbered_list(new_white_pieces)
    selection = int(input("Select an integer? "))
    while True:
        if int(selection) in new_white_pieces:
            return [selection]
        selection = int(input(selection + " is not recognised. Please select an acceptable number: "))

def handle_new_white_pieces(spots_left,new_white_pieces,white_pieces):
    new_len = len(new_white_pieces)
    if spots_left == 0:
        return white_pieces
    if spots_left == 1 and new_len == 2 and new_white_pieces[0] != new_white_pieces[1]:
        new_white_pieces = select_one_new_white_pieces(new_white_pieces)
    return add_new_white_pieces_loop(new_white_pieces, white_pieces)

def add_white_pieces(white_pieces,selection):
    max_white_pieces = 3
    spots_left = max_white_pieces - len(white_pieces)
    new_white_pieces = []
    for i in selection:
        if i in white_pieces:
            white_pieces[i] +=1
        else:
            new_white_pieces.append(i)
    white_pieces = handle_new_white_pieces(spots_left,new_white_pieces,white_pieces)
    return white_pieces
def bombed():
    print("OH NO! You bombed!")
    print("Your progress from this turn will be erased.")
    return False
def roll_again():
    return helper.yes_no_question("Would you like to roll again?")
def display_white_pieces(white_pieces):
    print("The progress of your white pieces are as follows:")
    cols = list(white_pieces.keys())
    cols.sort()
    for col in cols:
        progress = white_pieces[col]
        print("You have achieved place %r in column %r." % (progress,col))
def run_turn():
    white_pieces = {}
    
    while True:
        if white_pieces:
            display_white_pieces(white_pieces)
        selection = run_round(white_pieces)
        if not selection:
            return bombed()
        print("You have selected ",end='')
        print(selection)
        white_pieces = add_white_pieces(white_pieces,selection)
        display_white_pieces(white_pieces)
        if len(white_pieces)==3:
            if not roll_again():
                return white_pieces
        helper.end_section()
        

if __name__ == "__main__":
    
    run_turn()