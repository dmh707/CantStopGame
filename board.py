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
    # returns {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
    return board_dict