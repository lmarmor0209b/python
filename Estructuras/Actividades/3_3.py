"""
Una máquina vende un producto que cuesta 170 céntimos. Solicita el valor de cada moneda en céntimos, de una en una; acepta 10, 20, 50 y 100. La persona puede introducir monedas hasta completar el precio.

Si se introduce una moneda no aceptada, informa del problema y vuelve a solicitar una moneda sin aumentar el importe pagado. Cuando se haya alcanzado o superado el precio, indica que entrega el producto y cuánto cambio debe devolver. El programa debe terminar en cuanto la compra se pueda completar.

No hace falta validar que la entrada se pueda convertir a número. Al final, muestra el cambio tanto en céntimos como en euros.
"""
# Declaración de variables
precio_producto = 170
descontar = 0

while precio_producto != 0:
    # Impresión por pantalla de un menú gráfico para el usuario
    print("-------------------------------------------")
    print(f"Precio del producto {precio_producto}")
    print("-------------------------------------------")
    print("Monedas aceptadas:")
    print("10 céntimos")
    print("20 céntimos")
    print("50 céntimos")
    print("100 céntimos")
    print("-------------------------------------------")
    # Petición al usuario de favor para el ingreso de las monedas
    descontar = int(input("Introduzca las monedas necesarias para alcancar el precio indicado: "))

    # Diferentes opciones para las diferentes monedas
    match descontar:
        case 10:
            precio_producto -= 10
        case 20:
           precio_producto -= 20
        case 50:
            precio_producto -= 50
        case 100:
            precio_producto -= 100
        # Caso de que el usuario cometa una errata
        case _:
            print("Ese valor no se acepta, favor de ingresar valor aceptado.")

# Impresión de precio completado. Para indicar el usuario de que se ha completado el precio asignado.
print("Precio completado")