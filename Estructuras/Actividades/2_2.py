# Fución precio_segun_edad
def precio_edad(edad):
    if edad <= 12:
        return 5
    elif edad >= 65:
        return 6
    else:
        return 8

# Variables de operacion
edad = int(input("Ingresa tu edad: "))
dia_semana = str(input("Ingresa el día de la semana: ")).strip().lower()
sesion_tres_d = int(input("La sesión es 3d [0 - Para no | 1 - Para sí]: "))

tipo_sesion = "" # Para introducir el tipo de sesion

# Asignamos un precio a la entrada en función de la edad
calcular_precio_edad = precio_edad(edad)

# Aplicamos descuento en función del día
match dia_semana:
    case "miercoles":
        calcular_precio_edad -= 1

# Aplicamos subida si es 3d o no
match sesion_tres_d:
    case 0:
        tipo_sesion = "Función Normal"
        calcular_precio_edad = calcular_precio_edad
    case 1:
        tipo_sesion = "Función 3D"
        calcular_precio_edad += 2

# Desglose de los detalles
print(f"Usted tiene: {edad} años\nEl día de su sesión es el: {dia_semana}\nSu sesión es: {tipo_sesion}\nEl precio es: {calcular_precio_edad}")