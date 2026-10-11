"""
Crea un programa que lea precio, unidades y porcentaje de descuento, calcule subtotal, descuento, IVA y total, y muestre cada importe con dos decimales. Añade una condición que indique si el pedido supera un umbral de envío gratuito.
"""

# Función para calcular el subtotal
def subtotal(precio,unidades):
    subtotal_caluclado = precio * unidades
    return subtotal_caluclado

# Función para calcular el descuento
def descuento(descuento_aplicar,subtotal):
    calcular_descuento = (100 - descuento_aplicar) / 100
    subtotal_descontado = subtotal * calcular_descuento
    return subtotal_descontado

def total(subtotal_descuento):
    return subtotal_descuento * 1.21

# El precio del producto
precio = float(input("Introduzca el precio: "))

# Unidades del producto
unidades = int(input("Introduzca las unidades: "))

# El descuento del producto
descuento_porcentaje = int(input("Introduzca el descuento [En formato de: 10, 20, 30, 40, etc]: "))

# Calcular el subtotal
subtotal_calculado = subtotal(precio, unidades)

# Calcular el descuento
descuento_calculado = descuento(descuento_porcentaje, subtotal_calculado)

# Imprimimos por pantalla los datos
print(f"El subtotal es: {float(subtotal_calculado):.2f}\nEl subtotal con el descuento es: {float(descuento_calculado):.2f}\nEl total es: {float(total(descuento_calculado)):.2f}")

# Condición del envió gratuito
if float(total(descuento_calculado)) >= 120:
    print("El coste de la compra supera el umbral y el envío es GRATUITO.")
else:
    print("El coste de la compra no supera el umbral del envío GRATUITO.")