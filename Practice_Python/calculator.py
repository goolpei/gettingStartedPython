

while True:
    
    input_first_num = input("Input First Num : ")
    try:
        num1 = float(input_first_num)
    except ValueError:
        print("Please enter a valid number.")
        continue

    operator = input("Input Operator (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:
        print("Please enter a valid operation (+, -, *, /).")
        continue
        
    input_second_num = input("Input Second Num: ")
    try:
        num2 = float(input_second_num)
    except ValueError:
        print("Please enter a valid number.")
        continue


    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Undefined"
        else:
            result = num1 / num2


    print(num1, operator, num2, "=", result )
    input_choice = input("Do you want to continue? (Y/N): ")
    if input_choice == 'Y' or input_choice == 'y':
        continue
    else:
        break
    

print("Calculator Stopped")