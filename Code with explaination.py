# To use random feature without writing more code.
import random
# To set the Symbols, numbers and letters going to be used in it.
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
# Taking input from the user that how many passwords do he/she wants to generate 
number = input('Number of Passwords:- ')
# For converting the no of passwords user wants to generate into int.
number = int(number)
# To set the length of the password
length = input('Length of the Password:- ')
# For converting the length entered by user into int.
length = int(length)

# This all is for letting the random feature to generate the password.
for p in range (number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
 #Printing the final password generated.
    print(password)