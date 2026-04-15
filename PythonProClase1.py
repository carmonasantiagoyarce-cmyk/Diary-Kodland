import  random
def gestor(long):
    caracteres =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    cantidad_caracteres = long
    almacenar_contrasena = ""
    for i in range(cantidad_caracteres):
        almacenar_contrasena += random.choice(caracteres)
    return (almacenar_contrasena)