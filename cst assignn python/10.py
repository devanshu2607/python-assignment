#10. Program for a login system 
stored_username = "user123"
stored_password = "pass123"

username = input("Enter your username :")
password = input("Enter your password :")

if username == stored_username and password == stored_password :
    print("Login successfully! WELCOME!")
else:
    print("Invalid username or password! Please try again.")    
