def greatestCommonDivisor(dividend, divisor):
    remainder = dividend % divisor
    if remainder == 0: return divisor
    while remainder > 0: 
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor
    return divisor

def greatestCommonDivisor2(dividend, divisor):
    while divisor:
        dividend, divisor = divisor, dividend % divisor
    return dividend

def greatestCommonDivisor3(dividend, divisor):
    return dividend if divisor == 0 else greatestCommonDivisor(divisor, dividend % divisor)


print(greatestCommonDivisor(219, 45))