##54.	Write a program that demonstrates plotting the Fibonacci sequence with PyLab.

import matplotlib.pyplot as plt

fib = [0,1]
for _ in range(2,11):
    fib.append(fib[-1]+fib[-2])

plt.plot(fib,marker='o')
plt.show()