collection = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! \'()$%&\""

def encrypt(text):
    if not text: return text

    res = []
    for i, c in enumerate(text):
        if c not in collection: raise Exception
        if (i + 1) % 2 == 0:
            res.append(text[i].upper())
        else:
            res.append(text[i])

    res2 = [collection[-collection.index(res[0]) - 1]]
    i = 0  
    j = i + 1
    
    while j < len(res):
        c1, c2 = res[i], res[j]
        indx1, indx2 = collection.index(c1), collection.index(c2)
        if indx1 - indx2 < 0:
            indx = (indx1 - indx2) + 77
        else:
            indx = indx1 - indx2
        resultant = collection[indx]
        res2.append(resultant)
        i += 1
        j += 1
    return ''.join(res)

def decrypt(encrypted_text):
    if not encrypted_text: return encrypted_text
    

te = 'Do the kata "Kobayashi-Maru-Test!" Endless fun and excitement when finding a solution!'
tx = 'DO ThE KaTa "KoBaYaShI-MaRu-TEsT!" EnDlEsS FuN AnD ExCiTeMeNt wHeN FiNdInG A SoLuTiOn!'
my = "$-Wy,dM79H'i'-vn0C&I.ZT2,Jw5vPlZc H;qkrhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"
tr = "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"
print(collection.index('"'))
print(collection.index('K'))
print(collection.index('-'))
print(collection.index('o'))
print(collection[76 - 10])
print(collection)