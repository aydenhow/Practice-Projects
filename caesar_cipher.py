# caesar_cipher.py #
# Program to encode and decode using Caesar cipher. Also has code to decode for unknown shift value.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode():
    text = str(input("Enter text to encode: ")).upper()
    shifts = int(input("Enter the desired shift value: "))
    encoded = ""
    for letter in text:
        if letter in alphabet:
            encoded += alphabet[(alphabet.find(letter) + shifts) % 26]
        else:
            encoded += letter

    print("Encoded text: " + str(encoded).capitalize())

def try_decode():
    for i in range(1,26):
        text = ""
        for letter in encoded:
            if letter in alphabet:
                text += alphabet[(alphabet.find(letter) - i) % 26]
            else:
                text += letter
        print(f"{i} shifts: {text.capitalize()}")
    shifts = input("Correct shift value: ")
    text = ""
    for letter in encoded:
        if letter in alphabet:
            text += alphabet[(alphabet.find(letter) - int(shifts)) % 26]
        else:
            text += letter
    print("Decoded text: " + str(text).capitalize())

def decode():
    encoded = str(input("Enter text to decode: ")).upper()
    shifts = input("Enter the shift value or ? to run the codebreaker: ")
    if shifts == '?':
        for i in range(1, 26):
            text = ""
            for letter in encoded:
                if letter in alphabet:
                    text += alphabet[(alphabet.find(letter) - i) % 26]
                else:
                    text += letter
            print(f"{i} shifts: {text.capitalize()}")
        shifts = input("\nCorrect shift value: ")
    text = ""
    for letter in encoded:
        if letter in alphabet:
            text += alphabet[(alphabet.find(letter) - int(shifts)) % 26]
        else:
            text += letter
    print("Decoded text: " + str(text).capitalize())


print("Welcome to the Caesar Cipher program!")
command = str(input("Please type E to encode or D to decode: ")).upper()
if command == 'E':
    encode()
elif command == 'D':
    decode()
else:
    print("Invalid command entered!")
