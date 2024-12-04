##76.	Implement a user authentication system with classes and file storage.

import os

class UserAuth:
    def __init__(self,filename="76.txt"):
        self.filename = filename

    def register(self, username, password):
        with open(self.filename, "a") as file:
            file.write(f"{username},{password}\n")
        print("User registered successfully.")

    def authenticate(self, username, password):
        if not os.path.exists(self.filename):
            print("No users found.")
            return False
        with open(self.filename, "r") as file:
            for line in file:
                stored_user , stored_pass = line.strip().split(',')
                if stored_user == username and stored_pass == password:
                    print("Authentication successful.")
                    return True
        print("Invalid credentials.")
        return False

# Example usage
auth_system = UserAuth()
auth_system.register("user1", "password123")
auth_system.authenticate("user1", "password123")