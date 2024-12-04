#17.Program to sum all even numbers from 1 to 100 
total = sum(number for number in range (1,101) if number % 2 == 0)
print (f"The sum of all even numbers from 1 to 100 is : {total}")