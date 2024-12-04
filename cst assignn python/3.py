#3. Program for a calculator
operation = input("Choose operation(+,-,*,/):")
a= float(input("Enter the first number :"))
b = float (input("Enter the second number:"))
if operation == '+':
    print(f"{a} + {b} = {a+b}")

elif operation == '-':
    print(f"{a} - {b} = {a-b}")

elif operation == '*' :
    print(f"{a}*{b} = {a*b}")
elif operation == '/':
      if b != 0 :
          print(f"{a} / {b} = {a/b}")
else:
    print("Error: Divison not possible")
    
     
