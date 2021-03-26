import helper
from board import get_board_dict

def add_new_white_pieces_loop(new_white_pieces, white_pieces):
    for i in new_white_pieces:
        #this if statement handles if there is double of an integer
        if i not in white_pieces:
            white_pieces[i] = 1
        else:
            white_pieces = iterate_white_piece(i,white_pieces)
    return white_pieces
def iterate_white_piece(num,white_pieces):
    assert num in white_pieces
    white_pieces[num] +=1
    return white_pieces
def select_one_new_white_pieces(new_white_pieces):
    print("You only have 1 white piece left. Which sum would you like to use?")
    helper.print_unnumbered_list(new_white_pieces)
    selection = int(input("Select an integer: "))
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
def display_white_pieces(white_pieces):
    print("The progress of your white pieces are as follows:")
    cols = list(white_pieces.keys())
    cols.sort()
    #get the max progress in here, once columns are sorted out
    for col in cols:
        progress = white_pieces[col]
        print("You have achieved place %r in column %r." % (progress,col))