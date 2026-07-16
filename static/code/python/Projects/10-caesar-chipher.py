"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

from typing import Callable

from helpers import ask, clear, header


def encrypt(msg: str, key: int = 17) -> str:

    if not msg:
        raise ValueError("Message Can't be empty!")

    encrypted_msg = ""

    for letter in msg:
        if not letter.isalpha():
            encrypted_msg += letter
        else:
            base: str = "a" if letter.islower() else "A"
            shifted = (ord(letter) - ord(base) + key) % 26 + ord(base)
            encrypted_msg += chr(shifted)

    return encrypted_msg


def decrypt(msg: str, key: int) -> str:
    return encrypt(msg, -key)


def should_btwn() -> Callable:
    def validator(x) -> str | bool:
        return "Please enter a number between 1 and 26." if not (0 < x <= 26) else True

    return validator


def main() -> None:
    while True:
        clear()
        header("Secure Message Generator")

        action = ask(
            "Select An Option",
            options={
                "encrypt": "Encrypt A Message",
                "decrypt": "Decypt A Message",
                "exit": "Exit App",
            },
        )

        clear()
        match action:
            case "encrypt":
                header("Encrypt A Message")

                msg: str = ask("Enter Your Message", allow_empty=False)
                key: int = ask(
                    "\nEnter a passcode (1-26)",
                    response_type=int,
                    validator=should_btwn(),
                )

                clear()
                header("Your Encrypted Message")
                print(encrypt(msg, key))

            case "decrypt":
                header("Decrypt A Message")

                msg = ask("Enter Encrypted Message", allow_empty=False)
                key = ask(
                    "\nEnter pass code (1-26)",
                    response_type=int,
                    validator=should_btwn(),
                )

                clear()
                header("Your Decrypted Message")
                print(decrypt(msg, key))

            case "exit":
                break

        ask("\n\nPress Any Key to Return To Main Menu...", press_any_key=True)


if __name__ == "__main__":
    main()
