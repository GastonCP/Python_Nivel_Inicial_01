# 6- Crear un programa que solicite una cadena de texto al usuario y determine si
# contiene la letra "a".

texto = str(input("Ingrese una cadena de texto -> "))
texto = texto.lower()
if("a" in texto):
    print("contiene a.")
else:
    print ("no contiene a.")