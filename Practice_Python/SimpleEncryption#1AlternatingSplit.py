def decrypt(encrypted_text, n):
    for _ in range(n):
        left = encrypted_text[:len(encrypted_text)//2]
        right = encrypted_text[len(encrypted_text)//2:]
        encrypted_text = ''
        for i, c in enumerate(right):
            encrypted_text += c
            if i < len(left): encrypted_text += left[i]
    return encrypted_text

def encrypt(text, n):
    for _ in range(n):
        left = ''
        right = ''
        for i, c in enumerate(text):
            if i % 2 != 0: left += c
            else: right += c
        text = left + right
    return text


# def decrypt(s, n):
#     if not s: return s
#     o, l = len(s) // 2, list(s)
#     for _ in range(n):
#         l[1::2], l[::2] = l[:o], l[o:]
#     return ''.join(l)


# def encrypt(s, n):
#     if not s: return s
#     for _ in range(n):
#         s = s[1::2] + s[::2]
#     return s