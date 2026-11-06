# Programa para saber la veces que aparece una letra en una palabra
palabra = str(input("Introduce una palabra:  ").strip().lower().replace(" ", ""))

registo_letra = {}

for i in palabra:
    if not i in registo_letra:
        registo_letra[i] = palabra.count(i)

for i in registo_letra:
    print(i, registo_letra[i])