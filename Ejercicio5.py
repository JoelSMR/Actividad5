# Pide al usuario que ingrese un número y lo convierte a un tipo de dato numérico (entero)
numero = int(input("Ingresa un número entero: "))

# Comprobamos si el número es par o impar usando el operador módulo (%)
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")