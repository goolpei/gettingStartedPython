#done
main_string = input("Enter main string S: ")
target_string = input("Enter target string T: ")

index_f = -1
index_i = 0
for char in target_string:
    if char not in main_string: 
        index_f = -1
        break
    elif char in main_string:
        if main_string.index(char, index_i) > index_f:
            index_f = main_string.index(char, index_i)
            index_i = index_f + 1
            
print(f"Result: {index_f}")
        