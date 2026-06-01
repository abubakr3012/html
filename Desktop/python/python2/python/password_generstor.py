import random
import string


def generate_password(length, use_letters, use_digits, use_symbols):
    chars = ""

    if use_letters:
        chars += string.ascii_letters

    if use_digits:
        chars += string.digits

    if use_symbols:
        chars += string.punctuation

    if chars == "":
        return "Error: No character types selected."

    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password


def main():
    print("=== Password Generator ===")

    length = int(input("Enter password length: "))

    letters = input("Include letters? (y/n): ")
    digits = input("Include digits? (y/n): ")
    symbols = input("Include symbols? (y/n): ")

    use_letters = letters.lower() == "y"
    use_digits = digits.lower() == "y"
    use_symbols = symbols.lower() == "y"

    password = generate_password(length, use_letters, use_digits, use_symbols)

    print("\nGenerated password:", password)


main()