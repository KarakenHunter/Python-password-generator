import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

number = input('Number of Passwords:- ')
number = int(number)

length = input('Length of the Password:- ')
length = int(length)

for p in range (number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)