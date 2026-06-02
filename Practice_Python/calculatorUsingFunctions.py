def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:

    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    operator = input("Enter operator (+, -, *, /): ")
    if operator not in ['+' ,'-', '*', '/']:
        print("Please enter a valid operation.")
        continue

    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        if num2 == 0:
            result = "Undefined"
        else:
            result = divide(num1, num2)

    print(num1, operator, num2, '=', result)

    choice = input("Do you want to continue? (Y/N): ")
    if choice != 'y' and choice != 'Y':
        break

print("Calculator stopped.")
   