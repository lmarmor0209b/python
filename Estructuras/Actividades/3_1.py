"""
Un sistema permite hasta tres intentos para introducir un código. El código correcto es "4826".

Pide el código y comunica si el acceso está autorizado. Si no es correcto, permite intentarlo de nuevo y avisa de cuántos intentos quedan. Después del tercer error, muestra que el acceso se ha bloqueado. Cuando el código sea correcto, no vuelvas a pedirlo.

Prueba el caso en que se acierta en el primer intento, en el último intento y en ninguno. Resuelve el ejercicio usando un bucle y condicionales.
"""

CODIGO = 4826
usuario_codigo = "" # Convertirlo luego a número entero
INTENTOS = 3

# Iniciamos el bucle de los intentos
for i in range(3):
    usuario_codigo = input("Ingrese un código: ")

    # Condicional de comprobación
    if int(usuario_codigo) == CODIGO:
        print("Código correcto")
        break
    else:
        print("Código incorrecto")
        INTENTOS -= 1
        print(f"Quedan {INTENTOS} intentos")

    # Condicional si el usuario falla todos los intentos
    match i:
        case 2:
            print("Se ha bloquedado el acceso")