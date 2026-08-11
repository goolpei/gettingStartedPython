# implemented using depth-first search algorithm
# stack
def dfs_n_queens(n):
    # should return a list of solutions

    if n < 1: return []
    
    col = set()
    pos_dia = set()
    neg_dia = set()

    def square_is_clear(row, column):
        return False if (column in col) or (row + column in pos_dia) or (row - column in neg_dia) else True

    solutions = []
    board_solutions = []
    board = [['.'] * n for _ in range(n)]

    r, c = 0, 0
    stack = []

    while True:


        found_valid_col = False
        while c < n:
            if square_is_clear(r, c):
                found_valid_col = True
                break
            c += 1

        if found_valid_col:
            stack.append((r, c))
            board[r][c] = 'Q'

            col.add(c)
            pos_dia.add(r + c)
            neg_dia.add(r - c)

            if len(stack) == n:
                sol = [x for _, x in stack]
                solutions.append(sol)
                board_solutions.append([row[:] for row in board])

                last_r, last_c = stack.pop()
                board[last_r][last_c] = '.'

                col.remove(last_c)
                pos_dia.remove(last_r + last_c)
                neg_dia.remove(last_r - last_c)

                r = last_r
                c = last_c + 1
            else:
                r += 1
                c = 0

        else:
            if not stack:
                break

            prev_r, prev_c = stack.pop()
            board[prev_r][prev_c] = '.'
            col.remove(prev_c)
            pos_dia.remove(prev_r + prev_c)
            neg_dia.remove(prev_r - prev_c)

            r = prev_r
            c = prev_c + 1


    # for b in board_solutions:
    #     for row in b:
    #         print(' '.join(row))
    #     print('\n')


    return solutions

        


    

dfs_n_queens(4)

