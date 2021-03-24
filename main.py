
def yes_no_question(string):
    answer =  input(string + " (Y or N) ")
    answer.lower()
    yes = ['y','yes','yeah']
    no = ['n','no','nope']
    while True:
        if answer in yes:
            return True
        if answer in no:
            return False
        answer= input('Please select Y or N ')

def end_section():
    print('\n\n')

def get_player_name():
    return input("Player Name: ")
def display_players_list(names_list):
    print('The players are: ')
    for i in range(len(names_list)):
        name = names_list[i]
        print(str(i) + '. ' + name)
def add_new_player_bool():
    return yes_no_question("Add new player?")
def remove_player_bool():
    return yes_no_question("Remove a player?")
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
    all_correct_bool = yes_no_question('Is this correct?')
    while not all_correct_bool:
        if add_new_player_bool():
            names_list = add_players_loop(names_list)
        if remove_player_bool():
            remove_player(names_list)
        display_players_list(names_list)
        all_correct_bool = yes_no_question('Is this correct?')
        
        
def main ():
    players_names_list = get_players_names()
main()