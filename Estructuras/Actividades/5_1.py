# Función para descontar el dinero
def calcular_dinero(dinero, restar_dinero):
    dinero_restante = dinero - restar_dinero
    return dinero_restante

# Función para descontar el tiempo
def calcular_tiempo(tiempo, restar_tiempo):
    tiempo_restante = tiempo - restar_tiempo
    return tiempo_restante

# Función para almacenar datos del usuario
def almacenar_actividad(nombre_actividad, dinero_actividad, tiempo_actividad, dinero_restante):
    conjunto_actividad = []
    conjunto_actividad.append(nombre_actividad)
    conjunto_actividad.append(dinero_actividad)
    conjunto_actividad.append(tiempo_actividad)
    conjunto_actividad.append(dinero_restante)
    return conjunto_actividad


# Nombres de las actividades
NOMBRE_C = "Cine"
NOMBRE_CO = "Comer"
NOMBRE_M = "Museo"
NOMBRE_D = "Deporte"
NOMBRE_CA = "Casa"

# Valor monetario de las actividades
CINE_DINERO = 6
COMER_DINERO = 12.56
MUSEO_DINERO = 4.5
DEPORTE_DINERO = 7
CASA_DINERO = 0

# Valor en minutos de las actividades
CINE_TIEMPO = 90
COMER_TIEMPO = 90
MUSEO_TIEMPO = 120
DEPORTE_TIEMPO = 60
CASA_TIEMPO = 45

# Resumen de actividades
actividades = []

# Valores del usuario
dinero = float(input("Ingrese la cantidad de dinero que dispone: "))
tiempo = int(input("Ingrese la cantidad en minutos del tiempo que dispone: "))

# Valor de la opcion salir
opcion = ""

while opcion != "salir":
    # Inicio del menú
    print("+----------------------------------+")
    print(f"1. Cine\n2. Comer\n3. Museo\n4. Deporte\n5. Casa")
    print("+----------------------------------+")
    opcion = str(input("Ingrese una opcion: ")).lower().strip().replace(" ", "")

    match opcion:
        case "cine":
            dinero = calcular_dinero(dinero, CINE_DINERO)
            tiempo = calcular_tiempo(tiempo, CINE_TIEMPO)
            if dinero < 0 or tiempo < 0:
                print("Eliga otra opción. Esta opción supera el umbral introducido.")
            else:
                actividades.append(almacenar_actividad(NOMBRE_C, CINE_DINERO, CINE_TIEMPO, dinero))
        case "comer":
            dinero = calcular_dinero(dinero, COMER_DINERO)
            tiempo = calcular_tiempo(tiempo, COMER_TIEMPO)
            if dinero < 0 or tiempo < 0:
                print("Eliga otra opción. Esta opción supera el umbral introducido.")
            else:
                actividades.append(almacenar_actividad(NOMBRE_CO, COMER_DINERO, COMER_TIEMPO, dinero))
        case "museo":
            dinero = calcular_dinero(dinero, MUSEO_DINERO)
            tiempo = calcular_tiempo(tiempo, MUSEO_TIEMPO)
            if dinero < 0 or tiempo < 0:
                print("Eliga otra opción. Esta opción supera el umbral introducido.")
            else:
                actividades.append(almacenar_actividad(NOMBRE_M, MUSEO_DINERO, MUSEO_TIEMPO, dinero))
        case "deporte":
            dinero = calcular_dinero(dinero, DEPORTE_DINERO)
            tiempo = calcular_tiempo(tiempo, DEPORTE_TIEMPO)
            if dinero < 0 or tiempo < 0:
                print("Eliga otra opción. Esta opción supera el umbral introducido.")
            else:
                actividades.append(almacenar_actividad(NOMBRE_D, DEPORTE_DINERO, DEPORTE_TIEMPO, dinero))
        case "casa":
            dinero = calcular_dinero(dinero, CASA_DINERO)
            tiempo = calcular_tiempo(tiempo, CASA_TIEMPO)
            if dinero < 0 or tiempo < 0:
                print("Eliga otra opción. Esta opción supera el umbral introducido.")
            else:
                actividades.append(almacenar_actividad(NOMBRE_CA, CASA_DINERO, CASA_TIEMPO, dinero))

# Se imprime por pantalla el resumen de las actividades, el dinero gastado, el tiempo invertido y el total del dinero restante
print("-------------------------------------RESUMEN---------------------------------")
for i in actividades:
   print(i)
print("-----------------------------------------------------------------------------")