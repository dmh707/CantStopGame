import helper


def get_board_dict():
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

def get_player_name():
    return input("Player Name: ")
def display_players_list(names_list):
    print('The players are: ')
    for i in range(len(names_list)):
        name = names_list[i]
        print(str(i) + '. ' + name)
def add_new_player_bool():
    return helper.yes_no_question("Add new player?")
def remove_player_bool():
    return helper.yes_no_question("Remove a player?")
def remove_player(names_list):
    display_players_list(names_list)
    num = int(input("Select the number of the player to remove: "))
    if num < len(names_list):
        names_list.pop(0)
    return names_list

def add_players_loop(names_list):
    add_name_bool = True
    while add_name_bool:
        names_list.append(get_player_name())
        add_name_bool = add_new_player_bool()
    return names_list

def remove_players_loop(names_list):
    remove_name_bool = True
    while remove_name_bool:
        names_list=remove_player(names_list)
        remove_name_bool = remove_player_bool()
    return names_list
def get_players_names():
    names_list = []
    names_list = add_players_loop(names_list)
    
    display_players_list(names_list)
    all_correct_bool = helper.yes_no_question('Is this correct?')
    while not all_correct_bool:
        if add_new_player_bool():
            names_list = add_players_loop(names_list)
        if remove_player_bool():
            remove_player(names_list)
        display_players_list(names_list)
        all_correct_bool = helper.yes_no_question('Is this correct?')
    helper.end_section()