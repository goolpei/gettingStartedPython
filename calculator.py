

while True:
    input_first_num = (input("Input First Num: "))
    input_second_num = (input("Input Second Num: "))
    operator = input("Input Operator (+, -, *, /, stop): ")
    
    if operator == "stop":
        break
    

    try:
        num1 = float(input_first_num)
        num2 = float(input_second_num)
    except ValueError:
        print("Please enter valid numbers.")
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
    else:
        print("Please use an operator.")
        result = "N/A"

    print(num1, operator, num2, "=", result )

print("Calculator Stopped")