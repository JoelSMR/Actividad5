# Pide al usuario que ingrese un número y lo convierte a un tipo de dato numérico (float)
numero = float(input("Ingresa un número: "))

# Comprobamos la condición
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")