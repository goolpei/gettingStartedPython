def modify_list(my_list):
    my_list.append(4)  # Modifies the original object in place
    print("Inside function:", my_list)

numbers = [1, 2, 3]
modify_list(numbers)

print("Outside function:", numbers)
# Output: Outside function: [1, 2, 3, 4] -> It changed!