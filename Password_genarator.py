import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '&', '*', '%']

print("Wellcome to the password genarator")
in_letters = int(input("How many letters would you like in your password : \n"))
in_symbols = int(input("How many symbols would you like : \n"))
in_numbers = int(input("How many numbers would you like : \n"))

password_list = []
for char in range(1, in_letters +1):
  password_list.append(random.choice(letters))

for char in range(1, in_symbols +1):
  password_list.append(random.choice(symbols))

for char in range (1, in_numbers +1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)   

password =""

for char in password_list:
  password+= char

print(f"Your Password is : {password}")
