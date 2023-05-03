# 8- Crear un programa que solicite una cadena de texto al usuario y determine si la
# cadena es un palíndromo.

texto = str(input("Ingrese una cadena de texto -> "))
texto1 = texto.lower().replace(" ","")
texto2 = texto1[::-1]
if(texto1 == texto2):
    print("SI es palindromo.")
else:
    print("NO es palindromo.")