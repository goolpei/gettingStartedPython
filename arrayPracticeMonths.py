months = [ "January" , "February" , "March" , "April" , "May" , "June" , "July" , "August", "September", "October", "November", "December" ]

while True:
    num = int(input())
    if num >= 1 and num <=12:
        print(months[num - 1])
    elif num == 0:
        print("Stopped Running")
        break
    else:
        print("Invalid Month Date")