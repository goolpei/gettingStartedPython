def expanded_form(num):  
    
    res = []
    
    while num > 0:
        pwr = len(str(num)) - 1
        set = num
        num = num % (10 ** pwr)
        set -= num
        res.append(str(set))

    return " + ".join(res)

def expanded_form2(num):
    whole, deci = map(int, str(num).split('.'))
    res = []
    while whole > 0:
        pwr = len(str(whole)) - 1
        temp = whole
        whole = whole % 10**pwr
        temp -= whole
        res.append(str(temp))
        
    while deci > 0:
        
        denom = 1
        
        pw = len(str(deci)) - 1
        tem = deci
        deci = deci % 10**pw
        tem -= deci
        res.append(str(tem)[0] + '/' + str(10 ** pw))
        
        
        
    return res
print(expanded_form(807))
