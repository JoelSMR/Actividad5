# Pide al usuario que ingrese una nota y la convierte a un tipo de dato numérico (entero)
nota = int(input("Ingresa la nota (0-100): "))

# Comprobamos el rango de la nota para asignar una calificación
if 90 <= nota <= 100:
    print("Calificación: A")
elif 80 <= nota <= 89:
    print("Calificación: B")
elif 70 <= nota <= 79:
    print("Calificación: C")
elif 60 <= nota <= 69:
    print("Calificación: D")
else:
    print("Calificación: F")