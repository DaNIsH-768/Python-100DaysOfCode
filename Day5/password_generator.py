import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator.")
n_letters = int(input("Enter number of letters you would like in your password: "))
n_numbers = int(input("How many numbers would you like? "))
n_characters = int(input("How many special characters would you like? "))

password = ""
password_list = []

for i in range(0, n_letters):
    password_list.append(random.choice(letters))

for i in range(0, n_numbers):
    password_list.append(random.choice(numbers))

for i in range(0, n_characters):
    password_list.append(random.choice(characters))

for i in range(0, len(password_list)):
    char = random.choice(password_list)
    password += char
    password_list.remove(char)

print("Your new Password is:", password)