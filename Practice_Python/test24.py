
# print(dir(10))
print((10).to_bytes)

def greet():
    return "Hello!"

# Treat the function like an object: assign an attribute to it!
greet.language = "English"

print(greet())           # Output: Hello!
print(greet.language)    # Output: English