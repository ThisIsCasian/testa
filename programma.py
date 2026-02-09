import random
elementi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
l = int(input("Dammi la lunghezza della password: "))
password = ""

for i in range(l):
    password += random.choice(elementi)

print(password)
