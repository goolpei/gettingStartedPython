# implemented using depth-first search algorithm
# stack
def dfs_n_queens(n):
    # should return a list of solutions
    if n < 1: return []

    # we need a set of column, diagonal, and anti-diagonal to indicate that it is taken / occupied by a queen's range
    # no need to indicate row since 

    occupied_col = set()
    occupied_dia = set() # dia and anti-dia

    solutions = []
    stack = []

    while stack:
        


