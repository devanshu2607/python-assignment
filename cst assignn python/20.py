#20. Program to list all prime numbers upto specified limit.

def is_prime(n):

    if n < 2:
     return False
    
    for i in range(2, n):
       if n % i ==0:
            return False 
       return True

limit = int(input("Enter the upper limit :"))

print("Prime numbers up to",limit,":")
for num in range(2,limit + 1):
    if is_prime(num):
        print(num,end= " ")