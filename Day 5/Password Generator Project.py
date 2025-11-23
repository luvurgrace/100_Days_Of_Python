import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level

password = []

for letter in range(0,nr_letters):
    rand_let = random.choice(letters)
    password.append(rand_let)
for number in range(0, nr_numbers):
    rand_num = random.choice(numbers)
    password.append(rand_num)
for symbol in range(0, nr_symbols):
    rand_sym = random.choice(symbols)
    password.append(rand_sym)
eas_pass = "".join(password)
print(f"Your easy password is: {eas_pass}")
# or for char in password_list:
    # password += char

# Hard Level

shuffled_pass = random.shuffle(password)
string_pass = "".join(password)
print(f"Your strong password is: {string_pass}")

