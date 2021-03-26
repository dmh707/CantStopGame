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
def enter_to_cont():
    input("Press 'Enter' to continue")
    end_section()

def print_numbered_list(the_list):
    for i in range(len(the_list)):
        print(str(i) + ". " + str(the_list[i]))
        
def print_unnumbered_list(the_list):
    for i in range(len(the_list)):
        print(str(the_list[i]))
        
def remove_duplicates_from_list(the_list):
    new_list = []
    for i in the_list:
        if i not in new_list:
            new_list.append(i)
    return new_list
