# Un diccionario es una colección de datos clave:valor. Clave = nombre. Valor = cantidad.
inventario = {
    "manzanas": 100,
    "platanos": 150,
    "naranjas": 75,
    "papas": 83
}

# Esta funcion recorre el diccionario y muestra cada producto con su cantidad.
def mostrar_inventario():
    print("\n--- Inventario Actual ---")
    for producto, cantidad in inventario.items():
        print(f"Producto: {producto.capitalize()}, Cantidad: {cantidad}")
    print("-------------------------\n")

# Esta se dedica de añadir o modificar los productos.
def agregar_o_actualizar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ").lower()
    try:
        cantidad_producto = int(input("Ingrese la cantidad: "))
        if cantidad_producto <= 0:
            print("La cantidad debe ser un número positivo.")
            return

        # Si el producto ya existe, se actualiza la cantidad. Si no, se ingresa ese producto como uno nuevo.
        if nombre_producto in inventario:
            inventario[nombre_producto] += cantidad_producto
            print(f"Se ha actualizado la cantidad de '{nombre_producto}' a {inventario[nombre_producto]}.")
        else:
            inventario[nombre_producto] = cantidad_producto
            print(f"Se ha agregado el producto '{nombre_producto}' con una cantidad de {cantidad_producto}.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para la cantidad.")


def buscar_producto():
    nombre_producto = input("Ingrese el nombre del producto a buscar: ").lower()
    
    if nombre_producto in inventario:
        print(f"\nProducto encontrado: {nombre_producto.capitalize()}, Cantidad: {inventario[nombre_producto]}\n")
    else:
        print(f"\nEl producto '{nombre_producto}' no se encuentra en el inventario.\n")

# Este es el ciclo principal del programa. Se ejecuta hasta que el usuario decida salir.
def main():
    while True:
        print("--- Opciones del Gestor ---")
        print("1. Ver inventario")
        print("2. Agregar o actualizar producto")
        print("3. Buscar producto")
        print("4. Salir")
        opcion = input("Elige una opción (1, 2, 3 o 4): ")

        # Usa condicionales para ejecutar la acción elegida.
        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            agregar_o_actualizar_producto()
        elif opcion == '3':
            buscar_producto()
        elif opcion == '4':
            print("¡Gracias por usar el gestor de inventario!")
            break  # Rompe el ciclo y sale del programa
        else:
            print("Opción no invalida. Elige 1, 2, 3 o 4.")

