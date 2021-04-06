import helper
from board import get_board_dict



def add_new_white_pieces_loop(new_white_pieces, white_pieces):
    new_wp_list = list(new_white_pieces.keys())
    for i in new_wp_list:
        #this if statement handles if there is double of an integer
        if i not in white_pieces:
            pos = new_white_pieces[i]
            white_pieces[i] = pos
        else:
            white_pieces = iterate_white_piece(i,white_pieces)
    return white_pieces
def iterate_white_piece(col,white_pieces):
    assert num in white_pieces
    white_pieces[col] +=1
    return white_pieces
def select_one_new_white_pieces(new_white_pieces):
    print("You only have 1 white piece left. Which sum would you like to use?")
    helper.print_unnumbered_list(new_white_pieces)
    selection = int(input("Select an integer: "))
    while True:
        if int(selection) in new_white_pieces:
            return [selection]
        selection = int(input(str(selection) + " is not recognised. Please select an acceptable number: "))

def handle_new_white_pieces(spots_left,new_white_pieces,white_pieces):
    new_wp_list = list(new_white_pieces.keys())
    new_len = len(new_white_pieces)
    if spots_left == 0:
        return white_pieces
    if spots_left == 1 and new_len == 2 and new_wp_list[0] != new_wp_list[1]:
        new_wp_list = select_one_new_white_pieces(new_wp_list)
        new_white_pieces = {new_wp_list[0]:new_white_pieces[new_wp_list[0]]}
    return add_new_white_pieces_loop(new_white_pieces, white_pieces)

def get_progress_for_col(progress,col):
    return progress[col][0]
    
def add_white_pieces(white_pieces,selection,progress):
    max_white_pieces = 3
    spots_left = max_white_pieces - len(white_pieces)
    new_white_pieces = {}
    double_nums = False
    if len(selection)==2:
        if selection[0] == selection[1]:
            double_nums = True
    for i in selection:
        if i in white_pieces:
            white_pieces[i] +=1
        else:
            prog_for_col = get_progress_for_col(progress,i)
            print(i)
            print(prog_for_col)
            move_piece = 1
            if double_nums:
                move_piece = 2
            new_white_pieces[i] = prog_for_col + move_piece
    white_pieces = handle_new_white_pieces(spots_left,new_white_pieces,white_pieces)
    return white_pieces
def display_white_pieces(white_pieces):
    print("The progress of your white pieces are as follows:")
    cols = list(white_pieces.keys())
    cols.sort()
    #get the max progress in here, once columns are sorted out
    for col in cols:
        progress = white_pieces[col]
        print("You have achieved place %r in column %r." % (progress+1,col))