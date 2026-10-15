# Importar la libreria random para generar un número aleatorio
import random 


# Opciones de la cuenta
estado_cuenta = True
titular = "Juan Pérez Garrido-Fernández"
saldo = random.randint(0, 1000)

# Menú de opciones para el usuario
print("---------------------")
print("1. Ingresar")
print("2. Retirar")
print("3. Abrir cuenta")
print("4. Cerrar cuenta")
print("5. Consultar")
print("---------------------")

# Entrada de la opción del usuario
opcion = input("Ingrese una opción: ").strip().lower()

# Comprobamos la opción insertada por el usuario
match opcion:
    # Ingresar dinero
    case "ingresar":
        # Pedimos la cantidad a ingresar
        cantidad_ingresar = float(input("Ingrese una cantidad: "))

        # Comprobamos si es correcta o no la cantidad
        if cantidad_ingresar < 0:
            print("La cantidad a ingresar no es válida")
        # Si es correcta la sumamos a la cantidad de la cuenta
        else:
            saldo += cantidad_ingresar

    # Retirar dinero
    case "retirar":
        # Pedimos la cantidad a retirar
        cantidad_retirar = float(input("Ingrese una cantidad: "))

        # Comprobamos si es correcta o no la cantidad
        if cantidad_retirar < 0:
            print("La cantidad a ingresar no es válida")
        # Si es correcta la restamos a la cantidad de la cuenta
        else:
            saldo -= cantidad_retirar
            if saldo < 0:
                saldo = 0
    
    case "abrircuenta":
        if estado_cuenta == True:
            print("Ya hay una cuenta abierta")
        else:
            estado_cuenta = True
            titular = str(input("Ingrese el nombre del titular: "))
            saldo = random.randint(0, 1_0_0_0)
    case "cerrarcuenta":
        estado_cuenta = False
        print("La cuenta ha sido cerrada")
    case "consultar":
        print(titular)
        print("--------------------------")
        print(f"Saldo: {saldo}")
    case _:
        print("Opción no valida")