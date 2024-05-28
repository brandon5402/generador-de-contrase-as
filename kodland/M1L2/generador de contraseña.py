import random
print('Password manager')
passwords = {}
while True:
    print('1-ver todas las contraseñas guardadas \n 2-agregar contraseña \n 3-modificar contraseña')

    def random_password():
        passw = ''
        x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        len_passw = int(input('ingrese el tamaño de la contraseña'))
        for i in range(len_passw):
            passw += random.choice(x)
        
        passwords[name] = passw





    name = input('nombre del servicio')
    passwop = input('¿aleatorio? y/n: ')
    if passwop == 'y':
        global passw
        random_password()

    elif passwop == 'f':
        passw = input('digite la contraseña a guardar')
        passwords[name] = passw

    print(passwords)









        
