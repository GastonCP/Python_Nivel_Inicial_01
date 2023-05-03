# 2- Crear un programa que solicite la edad del usuario y determine si es mayor o
# menor de edad.

edad = int(input("Ingrese la edad del usuario -> "))
if(edad > 0) :
    if (edad >= 18) :
        print ("el usuario es mayor de edad.")
    else :
        print ("el usuario es menor de edad.")
else :
    print ("edad ingresada no valida.")