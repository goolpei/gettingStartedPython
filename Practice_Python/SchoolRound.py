def school_round(x, round_to=1):
    # 1. Handle negative numbers by working with the absolute value
    sign = 1 if x >= 0 else -1
    abs_x = abs(x)
    
    # 2. Calculate the offset (exactly half of what we are rounding to)
    offset = round_to / 2
    
    # 3. Perform the shift, integer divide, and scale back
    # We use float division '/' and then cast to int to prevent floating-point bugs
    rounded_abs = int((abs_x + offset) / round_to) * round_to
    
    # 4. Put the positive or negative sign back
    return rounded_abs * sign

def school_round_ten(x):
    # Add 5, integer-divide by 10, then multiply by 10
    return int((x + 5) // 10) * 10