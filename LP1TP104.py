# 4- Crear un programa que solicite dos números al usuario y determine cuál es el
# mayor.

numero1 = int(input("Ingrese un numero 1 -> "))
numero2 = int(input("Ingrese un numero 2 -> "))
if(numero1 > numero2):
    print ("el mayor es el primer numero ingresado (", numero1, ")." )
else:
    print ("el mayor es el segundo numero ingresado (", numero2, ")." )
