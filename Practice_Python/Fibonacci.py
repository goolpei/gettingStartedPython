def fib_iterative(n): # nth fibonacci number
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_iterative(10))