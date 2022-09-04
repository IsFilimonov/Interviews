def is_solved(board):
    # 8 win combinations indexes, xy i c [0,2]:
    # 00,01,02  10,11,12    20,21,22    rows
    # 00,10,20  01,11,21    02,12,22    columns
    # 00,11,22  02,11,20                diagonals

    # diagonal: 00,11,22
    diag = [board[i][i] for i in range(3)]
    # transpose matrix
    t_board = [list(i) for i in zip(*board)]
    # transpose diagonal: 02,11,20
    t_diag = [t_board[i][i] for i in range(3)]

    # all win combinations
    arr = board + t_board + [diag] + [t_diag]

    for a,b,c in arr:
        d = "".join(map(str,[a,b,c]))

        if d == '111':
            return 1
        elif d == '222':
            return 2

    if 0 not in [board[i][j] for i in range(3) for j in range(3)]:
        return 0

    return -1