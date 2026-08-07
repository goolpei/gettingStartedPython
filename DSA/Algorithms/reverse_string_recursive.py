def reverse_string(s: str) -> str:
    if not s or len(s) == 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string(' jbh f'))
    