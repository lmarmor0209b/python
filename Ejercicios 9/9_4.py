"""
Un aula tiene 12 plazas disponibles. Reserva 3 plazas y después cancela 1 reserva, actualizando la variable con asignación aumentada. Muestra el número final de plazas y, mediante una expresión condicional, muestra "Hay plazas" si queda alguna o "Completo" si no queda ninguna.
"""

plazas = 12
plazas = plazas - 3
plazas = plazas + 1

if plazas != 0:
    print("Quedan plazas")
else:
    print("No hay plazas")