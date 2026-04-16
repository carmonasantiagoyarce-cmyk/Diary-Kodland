import  random
def gestor(long):
    caracteres =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    cantidad_caracteres = long
    almacenar_contrasena = ""
    for i in range(cantidad_caracteres):
        almacenar_contrasena += random.choice(caracteres)
    return (almacenar_contrasena)

FinalResult=None


while True:
    try:
        GetContrasena=int(input("Ingresa un numero de caracteres para tu contraseña"))
        FinalResult=GetContrasena
        break
    except ValueError:
        print("Por favor ingrese un numero")
        

FinalContraseña=gestor(FinalResult)

print(f"Esta es tu nueva contraseña {FinalContraseña}")