n = 1234
guess = int(input("Enter your guess: "))

while guess != n:
    if guess > n:
        print("Too high")
    else:
        print("Too low")

        
    
    guess = int(input("Enter your guess: "))
    

print("Correct!")