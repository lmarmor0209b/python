"""
Guarda si una persona está matriculada (True), si tiene autorización especial (False) y su edad (17). Puede acceder si está matriculada y tiene al menos 18 años, o si tiene autorización especial. Calcula y muestra el resultado como True o False. Cambia los valores para comprobar también un caso en el que sí pueda acceder.
"""

persona = {
    "matriculada" : True,
    "autorizacion" : False,
    "edad" : 17
}

if persona["matriculada"] == True and persona["edad"] >= 18 or persona["autorizacion"] == True:
    print(True)
else:
    print(False)