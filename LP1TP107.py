# 7- Crear un programa que solicite una cadena de texto al usuario y determine si la
# cadena comienza con la letra "h".

texto = str(input("Ingrese una cadena de texto -> "))
texto = texto.lower()
if(texto[0] == "h"):
    print("Su primera letra es h.")
else:
    print("su primera letra no es h.")
