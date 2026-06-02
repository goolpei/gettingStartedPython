name = ""
while True: 
    name = input("Enter your name: ")

    if name == "" or name == "exit":  
        print("Goodbye!")
        break

    print("Hello " + name)

    
