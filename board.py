import helper
def get_board_dict():
    '''
    min_col = 2
    max_col = 12
    dif_btwn_cols = 2
    start_val = 3
    
    board_dict={}
    peak = 7
    for i in range(min_col,max_col+1):
        if i<=peak:
            val = dif_btwn_cols*i-1
        else:
            b = start_val + (dif_btwn_cols*max_col)
            val = (-dif_btwn_cols)*i + b
        board_dict[i] = val
    return board_dict
    '''
    return {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
    

def if_progress_col_place_empty(col,place,progress):
    if col not in progress:
        progress[col] = {}
    if place not in progress[col]:
        progress[col][place] = []
    return progress
def format_one_player_progress_col_first(name,entry):
    player_progress = {}
    for col in entry.keys():
        place = entry[col]
        player_progress = if_progress_col_place_empty(col,place,player_progress)
        player_progress[col][place] = name
    return player_progress

def format_all_progress_col_first(col, col_progress, all_progress):
    for place in col_progress:
        name = col_progress[place]
        all_progress = if_progress_col_place_empty(col,place,all_progress)

        all_progress[col][place].append(name)

    return all_progress

def add_entry_to_player_progress_col_first(player_progress,all_progress):
    for col in player_progress.keys():
        all_progress = format_all_progress_col_first(col, player_progress[col], all_progress)
    return all_progress
def format_player_progress_col_first(progress):
    new_progress = {}
    for name in progress.keys():
        player_progress = format_one_player_progress_col_first(name,progress[name])
        new_progress = add_entry_to_player_progress_col_first(player_progress,new_progress)
    return new_progress

def get_progress_str(progress):
    output = ''
    places_list = list(progress.keys())
    places_list.sort()
    for place in places_list:
        place_num = place +1
        place_str = "Pos " + str(place_num) + ": "
        names_list = progress[place]
        for name in names_list:
            name = name.upper()
            place_str += name +', '
        place_str = place_str[:-2] +'. '
        output +=place_str
    return output

def col_to_string(col_max, progress, col):
    empty_space_str = '. '
    spaces_list = []
    for i in range(col_max):
        spaces_list.append(empty_space_str)
    spaces_list[-1] = col
    for i in progress.keys():
        char = helper.first_char(progress[i][0])
        spaces_list[i] = char + ' '
    output = str(col) + '   '
    if len(str(col))==1:
        output += ' '
    for i in spaces_list:
        output +=str(i)
    print(output, end='   ')
    
    if progress:
        progress_str = get_progress_str(progress)
        print(progress_str,end='')
    print('')
        
    
    

def display_board(board_dict,progress):
    cols_progress = format_player_progress_col_first(progress)
    helper.end_section()
    
    print("The board")
    for col in board_dict.keys():
        col_max = board_dict[col]
        col_progress = {}
        if col in cols_progress:
            col_progress = cols_progress[col]
        col_to_string(col_max,col_progress,col)
    helper.end_section()
    