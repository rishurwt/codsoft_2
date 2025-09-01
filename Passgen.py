import random
import string

def generate_password(length=8, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Password Generator")


length = int(input("Enter password length: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_digits, use_symbols)
print("Your password is:", password)
