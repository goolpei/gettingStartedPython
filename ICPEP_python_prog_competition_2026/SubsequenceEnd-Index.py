def isSubsequence(m, t):
    
    
    i_main = 0
    j_target = 0
    target_length = len(t)
    main_length = len(m)
    
    while(j_target < target_length and i_main < main_length ):
        if m[i_main] == t[j_target]:
            if j_target == target_length -1:
                return i_main
        
            j_target += 1
            
        i_main += 1
    
    
    return -1
    
            
    
    

main_string = input("Enter main string S: ")
target_string = input("Enter target string T: ")


result = isSubsequence(main_string, target_string)
print(f"Result: {result}")