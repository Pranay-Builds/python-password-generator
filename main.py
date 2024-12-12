# Python Password Generate Program
import random

def generate_password(keep_numbers, keep_special_chars, length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if keep_numbers:
        characters += "0123456789"
    if keep_special_chars:
        characters += "~`!@#$%^&*()_+'./?"

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    running = True
    while running:
        generate_password_prompt = input("Do you want to generate a password? (y / n): ").strip().lower()
        if generate_password_prompt == "n":
            print("Exiting program.")
            print("Thanks for joining!")
            running = False
            continue

        keep_numbers = input("Include numbers in the password? (y / n): ").strip().lower() == "y"
        
        keep_special_chars = input("Include special characters in the password? (y / n): ").strip().lower() == "y"

        while True:
            try:
                length = int(input("Enter the length of the password (minimum 8): "))
                if length >= 8:
                    break
                else:
                    print("Password length must be at least 8.")
            except ValueError:
                print("Please enter a valid number.")

        password = generate_password(keep_numbers, keep_special_chars, length)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
