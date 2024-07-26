import random
import string

def Password_Generator(length):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    # Create a pool of characters: lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one of each type of character
    password = [
        random.choice(string.digits),
        random.choice(string.digits),
        random.choice(string.ascii_uppercase),
        random.choice(string.punctuation),
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.punctuation),
        random.choice(string.ascii_lowercase)
    ]

    # Fill the rest of the password length with random choices from the character pool
    password += random.choices(characters, k=length-8)

    # Shuffle the resulting list to ensure randomness
    random.shuffle(password)

    # Convert the list back to a string and return it
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length for the password: "))
    password = Password_Generator(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
