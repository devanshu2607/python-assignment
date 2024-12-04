#18.Program that prints the multiplication of number entered by the user.

number = int(input("Enter the number for table :"))

print(f"\n Table for {number} : \n")
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")