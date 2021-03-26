import helper
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
        option1 = first_die + dice[i]
        option2 = total - option1
        combo = [option1,option2]
        combo.sort()
        combos.append(combo)
    print("This roll yeilds the following sums:", end=" ")
    print(combos)
    combos = helper.remove_duplicates_from_list(combos)
    return combos
def select_combo(combos):
    nums_str = ""
    for i in range(0,len(combos)):
        if i != 0:
            nums_str +=', '
        nums_str += str(i)
    len_str = "(options: "+ nums_str +") "
    print("Which number(s) would you like to play?")
    helper.print_numbered_list(combos)
    selection = []
    i = input("Select the line number of the combo you would like to play: " + len_str)
    while True:
        try:
            return combos[int(i)]
        except:
            i = input(i + ' is not recognised. Please select an acceptable line number. ' + len_str)
def filter_combo_through_white_pieces(combo,wp_keys):
    new_combo = combo
    remove_digits = []
    for digit in combo:
        if digit not in wp_keys:
            remove_digits.append(digit)
    for digit in remove_digits:
        new_combo.remove(digit)
    return new_combo
def filter_combos_through_white_pieces(combos,wp_keys):
    new_combos = []
    for i in range(len(combos)):
        combo = combos[i]
        new_combo = filter_combo_through_white_pieces(combo,wp_keys)
        if new_combo:
            new_combos.append(new_combo)
    return new_combos
def run_round(white_pieces={}):
    wp_keys = white_pieces.keys()
    dice = roll()
    print("You have rolled the following dice: ",end='')
    print(dice)
    combos = get_combos(dice)
    if len(wp_keys)==3:
        combos = filter_combos_through_white_pieces(combos,wp_keys)

    #find a way to process combos for unplayable integers
    #ways it can be unplayable: no more white pieces,
    #column filled,
    #already at top of column
    #handle if bombed
    if not combos:
        return False
    return select_combo(combos)

def dummy():
    print(run_round({7: 3, 8: 1, 6: 3}))
if __name__ == "__main__":
    dummy()
    #print(run_round())