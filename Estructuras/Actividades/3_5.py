"""
Simula el uso de una cuenta bancaria mediante un menú que se repite hasta que se elija salir. La cuenta empieza activa, tiene un titular y un saldo inicial aleatorio entre 0 € y 1.000 €. Puedes usar el módulo random para generar el saldo. En cada vuelta, pide una operación: ingresar, retirar, consultar, cerrar cuenta, abrir cuenta o salir.

Aplica estas reglas:

    Ingresar: solicita una cantidad positiva y súmala al saldo. Solo se puede operar con una cuenta activa.
    Retirar: solicita una cantidad positiva. Solo permite la retirada si la cuenta está activa y hay saldo suficiente.
    Consultar: muestra el titular, el saldo y si la cuenta está activa o cerrada.
    Cerrar cuenta: solo se puede cerrar si está activa y el saldo es 0.
    Abrir cuenta: solo se puede abrir si está cerrada. Al abrirla, el saldo empieza en 0 €.
    Salir: termina el menú y muestra el estado final de la cuenta.

Si una operación no se puede realizar, explica el motivo y vuelve a mostrar el menú. Normaliza el texto de la operación para aceptar mayúsculas y espacios sobrantes. Supón que las cantidades introducidas son números positivos; no hace falta gestionar errores de conversión. Prueba una secuencia que incluya un ingreso, una retirada superior al saldo disponible, una consulta, un intento de cierre con saldo, una retirada que deje el saldo en cero, el cierre, una nueva apertura y la salida.
"""

# Libreria para generar un número aleatorio
import random

# Variables de la cuenta estándar
estado_cuenta = True
titular = "Titular Anónimo"
saldo = random.randint(0, 1000)


while True:
    # Imprimos por pantalla las acciones para el usuario
    print("-----------------------------------------")
    print("1. Ingresar")
    print("2. Retirar")
    print("3. Consultar")
    print("4. Cerrar cuenta")
    print("5. Abrir cuenta")
    print("6. Salir")
    print("-----------------------------------------")
    print(f"\n")
    # Le pedimos que ingrese una acción
    accion = str(input("Introduzca una opción: ")).strip().lower().replace(" ", "")

    # Casos para las acciones
    match accion:
        case "ingresar":

            # Le pedimos al usuario la cantidad a ingresar
            cantidad = float(input("Que cantidad desea ingresar en su cuenta: "))

            # Nos aseguramos que dicha cantidad sea mayor o igual a 0
            while cantidad <= 0:
                print("Esa cantidad no es posible.")
                cantidad = float(input("Ingrese una cantidad válida: "))

            # Cumplida esa condición se lo sumamos al sueldo
            else:
                saldo += cantidad
                print(saldo)

        # Acción retirar
        case "retirar":

            # Pedimos al usuario una cantidad a retirar
            cantidad = float(input("Ingrese la cantidad a retirar de su cuenta: "))

            # Nos cercioramos si la cantidad no es mayor al dinero que hay en cuenta
            while True:
                if saldo - cantidad < 0:
                    print ("Quiere retirar más dinero del que hay en cuenta.")
                    cantidad = float(input("Ingrese la cantidad correcta a retirar de su cuenta: "))

            # Si la cantidad es correcta, la descontamos del saldo de la cuenta.
                else:
                    saldo -= cantidad
                    print(saldo)
                    break

        # Acción para consultar la cuenta
        case "consultar":
            print("Estado: Abierta")
            print(f"Saldo: {saldo}")
            print(f"Titular: {titular}")

        # Acción para cerrar la cuenta
        case "cerrarcuenta":
            if estado_cuenta == True:
                estado_cuenta = False
                saldo = 0
                titular = ""
            else:
                print("Se necesita abrir una cuenta para realizar esta acción.")

        # Abrir cuenta
        case "abrircuenta":
            if estado_cuenta == False:
                estado_cuenta = True
                saldo = 0
                titular = str(input("Ingrese su nombre: "))
            else:
                print("Ya hay una cuenta abierta...")

        # Acción salir
        case "salir":
            if estado_cuenta == True:
                print("Estado: Abierta")
                print(f"Saldo: {saldo}")
                print(f"Titular: {titular}")
            else:
                print("Estado: Cerrada")
                print("No existe saldo")
                print("No existe titular")
            break

        # Si no existe la opción en cuestión
        case _:
            print("Acción no válida...")