import random
import time
import pdb

choices = {
    1 : 'Rock',
    2 : 'Paper',
    3 : 'Scissors'
}
results = {
    (1, 2) : 'You lose.',
    (2, 1) : 'You win!',
    (1, 3) : 'You win!',
    (3, 1) : 'You lose.',
    (2, 3) : 'You lose.',
    (3, 2) : 'You win!'

}

while(True):
    print("----Rock Paper Scissors Game----")
    print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")

    user_input = input("Enter choice number: ")
    if user_input == '4': break
    if user_input not in ['1', '2', '3']:
        print("Please enter valid choice.")
        continue

    user_choice = int(user_input)
    #pdb.set_trace()


    device_choice = random.randint(1, 3)
    choice_pair = (user_choice, device_choice)

    print("Computer chooses", end='')
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    time.sleep(0.5)

    print(' ' + choices[device_choice] + '!')
    print(f'You chose {choices[user_choice]}!')
    if user_choice == device_choice: print("Draw")
    else:
        print(results[choice_pair])
    
    print('-' * 32)

print("See ya!")
