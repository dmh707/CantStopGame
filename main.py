import helper
import pregame
import random

def roll():
    num_of_dice = 4
    sides_of_dice = 6
    dice = []
    for i in range(num_of_dice):
        dice.append(random.randint(1,sides_of_dice))
    return dice

def get_combos(dice):
    combos = []
    total = sum(dice)
    first_die = dice[0]
    for i in range(1,len(dice)):
        option = first_die + dice[i]
        combos.append([option, total - option])
    print("This roll yeilds the following sums:", end=" ")
    print(combos)
    return combos

def select_combos(combos):
    pass

def run_turn():
    dice = roll()
    combos = get_combos(dice)
    combo_selection = select_combo(combos)

def main ():
    players_names_list = ['Mary','Sarah','Eli','Samuel']
    board_dict = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
    #players_names_list = pregame.get_players_names()
    #board_dict = pregame.get_board_dict()
    turn = run_turn()
main()