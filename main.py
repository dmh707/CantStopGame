import helper
import pregame
import board
import turn
import player_progress_funcs


        
        

def main ():
    players_names_list = ['Mary','Sarah']
    #board_dict = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
    #players_names_list = pregame.get_players_names()
    board_dict = board.get_board_dict()
    players_progress_dict = player_progress_funcs.create_players_progress_dict(players_names_list)
    players_progress_dict = {'Mary': {2: 1, 8: 2, 7: 12}, 'Sarah': {5: 1, 7: 1, 10: 1}}
    players_len = len(players_names_list)
    i = 0
    while True:
        active_player=players_names_list[i]
        player_progress_funcs.display_active_player(active_player)
        i = player_progress_funcs.iterate_active_player_index(i,players_len)
        #white_pieces = {6: 7, 10: 1, 7: 4}
        
        player_progress_dict = players_progress_dict[active_player]
        
        white_pieces = turn.run_turn(player_progress_dict)
        if white_pieces:
            player_progress_dict = player_progress_funcs.update_player_progress_dict(player_progress_dict, white_pieces)
            players_progress_dict[active_player] = player_progress_dict
        board.display_board(board_dict,players_progress_dict)
        
        
    
if __name__ == "__main__":
    main()