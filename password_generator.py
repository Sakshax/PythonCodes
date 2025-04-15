import random
"""
This script generates a random password using a combination of letters, digits, and punctuation.

Functions:
    generate_password(length=12):
        Generates a random password of the specified length.
        The password is created using a mix of uppercase letters, lowercase letters, digits, and special characters.

        Parameters:
            length (int): The desired length of the password. Defaults to 12.

        Returns:
            str: A randomly generated password.

Usage:
    Run the script to generate and print a random password of the default length (12 characters).
    You can modify the `length` parameter in the `generate_password` function call to customize the password length.
"""
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password())
