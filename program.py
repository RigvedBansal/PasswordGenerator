import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'abcdefghijklmnopqrstuvwxyx'.upper()
numbers = '0123456789'
symbols = '!@#$%^&,./_;[]'

all = symbols + numbers + lower + upper
length = int(input("How many characters do you want the password to be? "))
password = ''.join(random.sample(all, length))
print(password)
