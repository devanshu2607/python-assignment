##67.	Create a program to generate random passwords with specified complexity.

import random 
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits +string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

print(generate_password(6))