"""
Una sala admite como máximo 8 personas. El programa debe llevar la cuenta de cuántas hay dentro. En cada turno, pide una acción: entra, sale o fin.

    Si la acción es entra y aún hay plazas, aumenta el aforo ocupado en uno.

    Si la sala está llena, no admitas a nadie más e informa de ello.

    Si la acción es sale y hay personas dentro, reduce el aforo ocupado en uno.

    Si la sala está vacía, no permitas que salga una persona y avisa de que no hay nadie dentro.

    Si se escribe fin, termina el control e informa de cuántas personas quedan en la sala.

Después de cada acción distinta de fin, muestra el aforo actual. Supón que las acciones introducidas son válidas. Prueba entradas y salidas en los límites, como intentar entrar con la sala llena y salir cuando está vacía.
"""

# Definición del valor "aforo"
aforo = 0

while True:

    # Impresión del menú para el usuario
    print("+-----------------------------------------------+")
    print("Acciones a realizar: ")
    print(f"1. Entra\n2. Sale\n3. Fin")
    print("+-----------------------------------------------+")

    # Le pedimos al usuario que realice una acción
    accion = str(input("Ingrese una acción: ")).lower().strip().replace(" ", "")

    # Casos para las acciones
    match accion:
        # Acción Entra
        case "entra":
            """
            Si la sala no está ocupada. Entonces se le suma
            un espectador a dicha sala.
            """
            if aforo < 8:
                aforo += 1
            else:
                """
                En caso contrario imprimimos que los asientos
                estan ocupados"""

                print("Están todos los asientos ocupados")
        
        # Acción Sale
        case "sale":
            """
            Si la sala está vacía informamos de que no hay
            nadie dentro de ella.
            """
            if aforo == 0:
                print("No hay nadie")
            else:
                # En caso contrario quitamos a un espectador.
                aforo -= 1
        
        # Acción Fin
        case "fin":
            # Finalizamos el programa y mostramos el total del aforo
            print(f"El aforo de la sala es: {aforo}")
            break
        # Caso de acción no válida
        case _:
            print("Acción no valida")