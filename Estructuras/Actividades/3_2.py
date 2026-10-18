"""
Pide un número entero mayor que 1 y determina si es primo. Un número primo solo se puede dividir exactamente entre 1 y entre sí mismo.

Prueba, si algún número entre 2 y el número anterior al introducido lo divide exactamente. Si encuentras un divisor, el número no es primo, si terminas las comprobaciones sin encontrar ninguno, sí lo es. Muestra el resultado. Comprueba el programa con un número primo, uno compuesto y el 2, que es el menor número primo.
"""

print(1 % 1)
print(1 % 1)

while True:
    numero_usuario = int(input("Ingrese un número: "))

    # Condicional de primo
    if numero_usuario // 1 == numero_usuario and numero_usuario // numero_usuario == 1:
        print("El número es primo")
        break
    else:
        print("El número no es primo")
        break