import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Random Password Generator!\n")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters= ""
for letter in range(0 , len(letters) - 1):
    password_letters = "".join(random.sample(letters , nr_letters))

password_numbers = ""
for number in range (0 , len(numbers) - 1) :
    password_numbers = "".join(random.sample(numbers , nr_numbers))

password_symbols = ""
for symbol in range(0 , len(symbols) - 1):
    password_symbols = "".join(random.sample(symbols , nr_symbols))

simple_lvl_password = password_letters + password_numbers + password_symbols  #Create a passwprd with with the elements in order
hard_lvl_password = "".join(random.sample(simple_lvl_password , len(simple_lvl_password)))  #Creates a random password with emenents in random order
print(f"Hard Level Password - Your new password is : {hard_lvl_password}")
