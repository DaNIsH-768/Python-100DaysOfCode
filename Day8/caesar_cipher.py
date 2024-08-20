def encrypt(word, shift):
    encoded_word = ""
    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for char in word.lower():
        if char.isalnum():
            old_index = chars.index(char)
            new_index = old_index + shift

            if new_index >= len(chars):
                new_index = new_index - len(chars)

            encoded_word += chars[new_index]
        else:
            encoded_word += char

    print(encoded_word)


def decrypt(word, shift):
    decoded_word = ""
    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for char in word.lower():
        if char.isalnum():
            old_index = chars.index(char)
            new_index = old_index - shift

            if new_index <= 0:
                new_index = len(chars) + new_index

            decoded_word += chars[new_index]
        else:
            decoded_word += char

    print(decoded_word)


print("Welcome to Caeser Cipher Decipher!!!")

while True:
    enc_dec = input("\nType 'encrypt' or 'decrypt' to start: ")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift: "))

    if enc_dec == "encrypt":
        encrypt(message, shift)
    elif enc_dec == "decrypt":
        decrypt(message, shift)
    else:
        print("Invalid Input")
        break

    yes_no = input("\nDo you want to try again 'yes' or 'no': ")
    if yes_no == "no":
        break

