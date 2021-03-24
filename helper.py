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