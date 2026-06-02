
def getSumSquares(nth_sum, step):

    dict_square = [x * x for x in range(1, nth_sum + 1)]
    return sum(dict_square[:nth_sum + 1:step])

print(getSumSquares(333000, 2))