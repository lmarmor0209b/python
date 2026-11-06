def convertir_numero(texto):
    try:
        texto = int(texto)
    except ValueError:
        print("No es un número")
    else:
        if texto < 0 or texto > 4:
            print("No es un valor correcto")
        else:
            return texto

def menu():
    print("------------ Eliga una opcion ----------------------")
    print(f"1. Añadir\n2. Quitar\n3. Repartir cuenta\n4. Salir")
    print("----------------------------------------------------")

def menu_productos():
    print("------------ Escriba una opción ----------------------")
    print(f"Pan\nLeche\nHuevos\nSalir")
    print("----------------------------------------------------")

def quitar_producto():
    print("Que producto desea quitar: ")
    opcion_producto = input("Ingrese el nombre del producto: ").lower().strip().replace(" ","")

    try:
        carrito.remove(opcion_producto)
    except ValueError:
        print("No se han agregado productos a la lista o se ha introducido un producto que no existe en la base de datos.")


# La caja de los productos
CAJA_PRODUCTOS = {
    "pan":0.85,
    "leche": 1.20,
    "huevos": 2.50
}

# Carrito
carrito = []

# Iniciacilización de opcion
opcion = ""

# Inicio del bucle
while opcion != 4:
    # Mostrar el menú
    menu()
    # Pedir una opción
    opcion = convertir_numero(input("Ingrese una opción: "))

    match opcion:
        # Añadir productos
        case 1:
            while opcion != "salir":
                menu_productos()
                try:
                    opcion = input("Ingrese la opción: ").strip().replace(" ","").lower()

                    match opcion:
                        case "pan":
                            carrito.append("pan")
                        case "leche":
                            carrito.append("leche")
                        case "huevos":
                            carrito.append("huevos")
                        case "salir":
                            print("Vuelta al menu principal")
                        case _:
                            print("No existe la opción: ")

                except ValueError as e:
                    print(f"El error es {e}")
        
        # Quitar productos
        case 2:
            quitar_producto()
        case 3:

            # Total de objetos en el carrito por categorias
            total_pan = carrito.count("pan")
            total_leche = carrito.count("leche")
            total_huevos = carrito.count("huevos")

            # Calculo de precio
            total_calculado_pan = total_pan * CAJA_PRODUCTOS["pan"]
            total_calculado_leche = total_leche * CAJA_PRODUCTOS["leche"]
            total_calculado_huevos = total_huevos * CAJA_PRODUCTOS["huevos"]

            print("----------------------- TOTAL -----------------------")
            print(f"Producto\tCantidad\tTotal")
            print(f"Pan\t\t{total_pan}\t\t{round(total_calculado_pan, 2)}")
            print(f"Leche\t\t{total_leche}\t\t{round(total_calculado_leche, 2)}")
            print(f"Huevos\t\t{total_huevos}\t\t{round(total_calculado_huevos, 2)}")
            print("------------------------------------------------------")

            # Total de todo los productos
            total = total_calculado_pan + total_calculado_leche + total_calculado_huevos
            
            print(f"Total calculado: {round(total, 2)}")

        case 4:
            print("Adiós")