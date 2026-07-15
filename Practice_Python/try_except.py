
try:
    num = int(input('Enter a number: '))
    x = 10/num
except (ZeroDivisionError, ValueError) as e:
    print(f'Error occured : {e}')
else:
    print(f'10 / {num} = {x}')
finally:
    print('Yoho')