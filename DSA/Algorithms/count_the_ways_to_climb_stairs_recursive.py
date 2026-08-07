# fibonacci sequence 

def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb_stairs(n - 1) + climb_stairs(n - 2)

print(climb_stairs(10))