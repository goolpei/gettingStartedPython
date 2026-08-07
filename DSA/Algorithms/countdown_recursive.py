def countdown_loop(n):
    while n > 0:
        print(n)
        n -= 1

    print('Blastoff!')

def countdown_recursive(n):
    if n == 0:
        print('Blastoff!')
        return
    print(n)
    countdown_recursive(n-1)

#countdown_loop(5)
countdown_recursive(5)