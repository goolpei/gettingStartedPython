#Calling a function
def greet():
    print("Hello Nayeon, I love you!")

greet()

hello = greet()

#Doesn't store a value, prints "None"
print(hello)

#Printing a function
def love():
    return "You are the love of my life."

#Can store a value
message = love()

print(love())
print(message)