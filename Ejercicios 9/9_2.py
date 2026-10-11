"""
Guarda en una variable una duración total de 7384 segundos. Calcula cuántas horas completas, minutos restantes y segundos restantes contiene, usando división entera (//) y resto (%). Muestra los tres resultados; deben ser 2 horas, 3 minutos y 4 segundos.
"""

segundos = 7384

print(f"Es un total de: {segundos // 60 // 60} horas {segundos // 60 % 60} minutos {segundos % 60} segundos")