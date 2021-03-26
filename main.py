import helper
import pregame
import board
import turn


        

def main ():
    players_names_list = ['Mary','Sarah','Eli','Samuel']
    board_dict = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
    #players_names_list = pregame.get_players_names()
    #board_dict = board.get_board_dict()
    white_pieces = turn.run_turn()
    
if __name__ == "__main__":
    main()