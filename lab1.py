from typing import Dict


def encrypt(message: str, message_key: int, upper_alphabet) -> str:
    encrypted_message = message.replace(" ", "")
    encrypted_code = []

    if message_key > 26 or message_key < 0:
        raise ValueError("The key must be from 1 to 25")

    encrypted_message = encrypted_message.upper()

    for c in encrypted_message:
        try:
            encrypted_code.append((upper_alphabet.index(c) + message_key) % 26)
        except ValueError:
            raise ValueError("The message must contain only letters and spaces")

    encrypted_message = ""
    for i in encrypted_code:
        encrypted_message += upper_alphabet[i]

    return encrypted_message


# Caesar cipher encryption implementation with keyword
def encrypt_caesar(message: str, message_key: int, keyword=None) -> dict:
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if keyword is None:
        return {
            "message": message,
            "encrypted_message": encrypt(message, message_key, upper_alphabet),
            "key": message_key,
            "keyword": None,
            "alphabet": upper_alphabet
        }

    else:
        if any(char.isdigit() or char == " " for char in keyword):
            raise ValueError("The keyword must contain only letters")

        sanitized_keyword = ""
        for char in keyword:
            if char not in sanitized_keyword:
                sanitized_keyword += char

        keyword_alphabet = sanitized_keyword.upper()
        for char in upper_alphabet:
            if char not in keyword_alphabet:
                keyword_alphabet += char

        return {
            "message": message,
            "encrypted_message": encrypt(message, message_key, keyword_alphabet),
            "key": message_key,
            "keyword": keyword,
            "alphabet": keyword_alphabet
        }


# Caesar cipher decryption implementation
def decrypt(encrypted_message: str, message_key: int, upper_alphabet) -> str:
    message = ""
    for c in encrypted_message.upper():
        try:
            message += upper_alphabet[(upper_alphabet.index(c) - message_key) % 26]
        except ValueError:
            raise ValueError("The message must contain only letters")

    return message


# Caesar cipher decryption implementation with keyword
def decrypt_caesar(encrypted_message: str, message_key: int, keyword=None) -> dict:
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if keyword is None:
        return {
            "encrypted_message": encrypted_message,
            "message": decrypt(encrypted_message, message_key, upper_alphabet),
            "key": message_key,
            "keyword": None,
            "alphabet": upper_alphabet
        }

    else:
        if any(char.isdigit() or char == " " for char in keyword):
            raise ValueError("The keyword must contain only letters")

        sanitized_keyword = ""
        for char in keyword:
            if char not in sanitized_keyword:
                sanitized_keyword += char

        keyword_alphabet = sanitized_keyword.upper()
        for char in upper_alphabet:
            if char not in keyword_alphabet:
                keyword_alphabet += char

        return {
            "encrypted_message": encrypted_message,
            "message": decrypt(encrypted_message, message_key, keyword_alphabet),
            "key": message_key,
            "keyword": keyword,
            "alphabet": keyword_alphabet
        }

def main():
    while True:
        print("What do you want to do?\nE - encrypt\nD - decrypt\nQ - quit", end=" ")
        mode = input().upper()
        print()

        if mode == "E":
            print("The message to encrypt:", end=" ")
            message = input()

            while True:
                try:
                    print("Encryption key:", end=" ")
                    key = int(input())
                    break
                except ValueError:
                    print("Sorry, the key must be an integer")

            print("Keyword (optional):", end=" ")
            keyword = input()

            try:
                output = encrypt_caesar(message, key, keyword)
            except ValueError as e:
                print("Error:", e)
            else:
                print("Alphabet:", output["alphabet"])
                print("Encrypted message:", output["encrypted_message"])
                print("Key:", output["key"])
                print("Keyword:", output["keyword"])

            print()

        elif mode == "D":
            print("The message to decrypt:", end=" ")
            message = input()

            while True:
                print("Decryption key:", end=" ")

                try:
                    key = int(input())
                    break
                except ValueError:
                    print("Sorry, the key must be an integer")

            print("Keyword (optional):", end=" ")
            keyword = input()

            try:
                output = decrypt_caesar(message, key, keyword)
            except ValueError as e:
                print("Error:", e)
            else:
                print("Alphabet:", output["alphabet"])
                print("Decrypted message:", output["message"])
                print("Key:", output["key"])
                print("Keyword:", output["keyword"])

            print()

        elif mode == "Q":
            break

        else:
            print("Unknown mode", end="\n\n")


main()
