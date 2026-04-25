def pig_it(text):
    text_list = text.split()
    new_text = ''
    for txt in text_list:
        if txt.isalpha():
            s = txt[1::] + txt[0:1] + 'ay'
            new_text += s + ' '
        else:
            new_text += txt + ' '
                    
        
    n = len(new_text) - 1
    final_text = new_text[:n:]
    return final_text


text = "Hello world"
s = pig_it(text)
print(s)

