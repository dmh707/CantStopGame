import helper




def get_player_name():
    return input("Player Name: ")
def display_players_list(names_list):
    print('The players are: ')
    helper.print_numbered_list(names_list)
def add_new_player_bool():
    return helper.yes_no_question("Add new player?")
def remove_player_bool():
    return helper.yes_no_question("Remove a player?")
def remove_player(names_list):
    num = int(input("Select the number of the player to remove: "))
    if num < len(names_list):
        names_list.pop(num)
    display_players_list(names_list)
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

def get_names_list():
    names_str = input("Please list the names of the players, separated by commas: ")
    names_list = names_str.split(",")
    for i in range(len(names_list)):
        name = names_list[i]
        if name[0]==' ':
            names_list[i]=name[1:]
    return names_list

def get_players_names():
    names_list = get_names_list()
    
    display_players_list(names_list)
    all_correct_bool = helper.yes_no_question('Is this correct?')
    while not all_correct_bool:
        if remove_player_bool():
            names_list = remove_players_loop(names_list)
        if add_new_player_bool():
            names_list = add_players_loop(names_list)
        display_players_list(names_list)
        all_correct_bool = helper.yes_no_question('Is this correct?')
    helper.end_section()

if __name__ == "__main__":
    get_players_names()