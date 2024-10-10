# nato_converter.py #

nato_alphabet = {"A":"Alpha","B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel",
            "I":"India","J":"Juliet","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa",
            "Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray",
            "Y":"Yankee","Z":"Zulu" }

morse = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....",
            "I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.",
            "Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
            "Y":"-.--","Z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....",
         "6":"-....", "7":"--...", "8":"---..", "9": "----.", "0":"-----"}

def convert_to_nato():
    start = True
    while start is True:
        text = str(input("Enter text to convert: ")).upper()
        letters = list(text)
        for index in range(len(letters)):
            if letters[index] in nato_alphabet:
                letters[index] = nato_alphabet[letters[index]]
        converted = ""
        for item in letters:
            converted += " " + str(item)
        print("Converted text: " + converted)
        again = input("Would you like to enter more text? (Y or N): ").upper()
        if again == 'N':
            start = False
            print("Exiting application...")
        else:
            continue

def convert_to_morse():
    start = True
    while start is True:
        text = str(input("Enter text to convert: ")).upper()
        letters = list(text)
        for index in range(len(letters)):
            if letters[index] in morse:
                letters[index] = morse[letters[index]]
        converted = ""
        for item in letters:
            converted += " " + str(item)
        print("Converted text: " + converted)
        again = input("Would you like to enter more text? (Y or N): ").upper()
        if again == 'N':
            start = False
            print("Exiting application...")
        else:
            continue

def convert_from_nato():
    start = True
    while start is True:
        text = str(input("Enter text to convert: "))
        letters = text.split(" ")
        for index in range(len(letters)):
            if letters[index] in nato_alphabet.values():
                letters[index] = list(nato_alphabet.keys())[list(nato_alphabet.values()).index(letters[index])]
        converted = ""
        for item in letters:
            converted += str(item)
        print("Converted text: " + converted.capitalize())
        again = input("Would you like to enter more text? (Y or N): ").upper()
        if again == 'N':
            start = False
            print("Exiting application...")
        else:
            continue

def convert_from_morse():
    start = True
    while start is True:
        text = str(input("Enter text to convert: "))
        letters = text.split(" ")
        for index in range(len(letters)):
            if letters[index] in morse.values():
                letters[index] = list(morse.keys())[list(morse.values()).index(letters[index])]
        converted = ""
        for item in letters:
            converted += str(item)
        print("Converted text: " + converted.capitalize())
        again = input("Would you like to enter more text? (Y or N): ").upper()
        if again == 'N':
            start = False
            print("Exiting application...")
        else:
            continue

language = str(input("Convert to NATO (N)  or Morse Code (M)?: ")).upper()
code = str(input("Encode (E) or Decode (D): ")).upper()
if language == 'N' and code == 'E':
    convert_to_nato()
elif language == 'N' and code == 'D':
    convert_from_nato()
elif language == 'M' and code == 'E':
    convert_to_morse()
elif language == 'M' and code == 'D':
    convert_from_morse()
else:
    print("Invalid command entered!")
