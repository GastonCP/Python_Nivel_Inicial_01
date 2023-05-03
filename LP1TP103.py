# 3- Crear un programa que solicite un número al usuario y determine si es positivo,
# negativo o cero.

numero = int(input("Ingrese un numero -> "))
if(numero == 0):
    print("ud ingreso el numero cero.")
elif (numero >0 ):
    print ("ud ingreso un valor mayor a cero.")
else:
    print ("ud ingreso un numero menor a cero.")