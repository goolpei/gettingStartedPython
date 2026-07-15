def set_age(age):
    if age < 0:
        # Intentionally crashing the program with a specific explanation
        raise ValueError("Age cannot be negative!")
    
    print(f"Age successfully set to {age}")

# This will run fine
set_age(25)

# This will halt the program and print a traceback with our message
set_age(-5)