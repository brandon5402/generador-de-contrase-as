import random
c = ''


x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contra = int(input('ingrese un numero'))
for i in range(contra):
    c += random.choice(x)



print(c)
