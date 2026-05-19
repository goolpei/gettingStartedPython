def calc_word_val(w):
    l = 'abcdefghijklmnopqrstuvwxyz'
    scores = {y:x for x, y in enumerate(l, start=1)}
    val = 0
    for char in w:
        val += scores[char]
    return val
        

def high(phrase):
    phrase = list(phrase.split())
    max_val = calc_word_val(phrase[0])
    res = phrase[0]
    for word in phrase:
        if calc_word_val(word) == max_val:
            res = res
        elif calc_word_val(word) > max_val:
            max_val = calc_word_val(word)
            res = word
        
    return res
        
print(high("man i need a taxi up to ubud"))