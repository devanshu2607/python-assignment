#16. Program to generate first 10 numbers of fibonacci series.
n = 10
fib_sequence = [0,1]

for i in range(2,n):
    next_number = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

print("The first 10 fibonacci numbers are :")  
print(fib_sequence)