alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = (input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift_amount) % len(alphabet)  # Wrap around using modulus
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char  # Add the character unchanged if it's not in the alphabet
    return encrypted_text

if direction == 'encode':
    result = encrypt(original_text=text, shift_amount=shift)
    print(f"Encoded message: {result}")
else:
    print("Decoding functionality not implemented yet.")
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

