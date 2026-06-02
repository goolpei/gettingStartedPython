def find_average(numbers):
    
    total = 0
    
    if len(numbers) == 0:
        return 0
    for n in numbers:
        total = total + n
        
    average = total / len(numbers)
    
    return average 

print (find_average([ 4, 5, 9, 100 ]))


# def find_average(array):
#    if len(array) != 0:
#        return sum(array) / len(array)
#    else:
#        return 0