def square_root_bisection(number: int | float, tolerance: float = 0.001, max_iterations: int = 100) -> float | None:
    
    def _f(num):
        return num*num - number
    
    if number < 0: raise ValueError('Square root of negative number is not defined in real numbers')
    if number in (0, 1):
        print(f'The square root of {number} is {number}')
        return number
    if max_iterations <= 0:
        raise ValueError('Iterations must be greater than 0.')
    if tolerance <= 0 or tolerance >= 1:
        raise ValueError('Tolerance must be between 0 and 1')
    
    if number < 1:
        high = 1
    else:
        high = number
    low = 0
 
    for _ in range(max_iterations):
        mid = (high + low) / 2
        val_f_mid = _f(mid)

        if val_f_mid == 0 or (high - low) <= tolerance:
            print(f'The square root of {number} is approximately {mid}')
            return mid
        elif val_f_mid > 0:
            high = mid
        else:
            low = mid
        
    
    print(f'Failed to converge within {max_iterations} iterations')
    return None

    
square_root_bisection(2, 0.1)

    # n = sqrt(y)
    # n^2 = y


    # sqrt(n) = y
    # sqrt(n) - y = 0
    # f(x) = 0
    # f(x) = sqrt(n) - y