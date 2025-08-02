# Pide al usuario que ingrese un año y lo convierte a un tipo de dato numérico (entero)
año = int(input("Ingresa un año: "))

# Comprobamos las condiciones para un año bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")