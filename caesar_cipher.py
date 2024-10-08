from art import logo
print(logo)
# Define the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26  # Handle wraparound
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % 26  # Handle wraparound
            new_letter = alphabet[new_position]
            plain_text += new_letter
        else:
            plain_text += char
    return plain_text

def caesar(plain_text, shift_amount, direction):
    if direction == "encode":
        cipher_text = encrypt(plain_text, shift_amount)
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        plain_text = decrypt(plain_text, shift_amount)
        print(f"The decoded text is {plain_text}")
    else:
        print("Invalid direction. Please choose 'encode' or 'decode'.")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(plain_text=text, shift_amount=shift, direction=direction)
    result = input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye")
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


















#
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encode text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         postion = alphabet.index(letter)
#         new_postion = postion - shift_amount
#         plain_text += alphabet[new_postion]
#     print(f"The decode text is {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
#
#
#






# encrypt(plain_text=text, shift_amount=shift)



    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.