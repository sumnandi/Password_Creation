#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
# Running the For loop from 0 to lenth of (nr_letters-1)
# With each loop putting a random string from letters list and adding it to password.
# randint() function chooses a random number between 0 to length of (letters list -1)
# Doing the same thing for symbols as well as numbers
for i in range(0,int(nr_letters)):
  password+=letters[random.randint(0,len(letters)-1)]

for i in range(0,int(nr_symbols)):
  password+=symbols[random.randint(0,len(symbols)-1)]

for i in range(0,int(nr_numbers)):
  password+=numbers[random.randint(0,len(numbers)-1)]

print(f"Moderate Level Password Suggestion: {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password=""

# Taking the password String and running a for loop from 1 to length of password
# In each loop choosing a random index using the randint function
# The value of the random index is then inserted into the hard_password

for i in password:
  hard_password+=password[random.randint(0,len(password)-1)]
print(f"Hard Level Password Suggestion: {hard_password}")
