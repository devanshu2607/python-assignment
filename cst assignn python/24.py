#24.Program to demonstrate the use of global variables.

counter = 0

def increment():
    global counter 
    counter += 1
    print(f"Counter incremented to {counter}")

def reset():
    global counter 
    counter = 0
    print("Counter rest to 0")

print(f"Initial counter value : {counter}") 
increment()
increment()
reset()
increment()       