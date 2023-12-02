"""
Cada archivo tiene un nombre con dos partes, separadas por un guion (-).
La primera parte es una cadena alfanumérica y la segunda es unchecksum, 
que es una cadena formada por los caracteres que sólo aparecen una vez en la
primera parte y en el orden en que aparecen.
Ejemplos:

Nombre del archivo: xyzz33-xy
Resultado: ✅ Real (El checksum es válido)

Nombre del archivo: abcca1-ab1
Resultado: ❌ Falso (El checksum debería ser b1, es incorrecto)
"""

texto = open("Proyectos-en-Python\\Retos_Semanales\\Codember\\Reto4_dostextos.txt", "r").read().splitlines()
reales = []


for code in texto:
    code = code.split("-")

    valido = True
    for check in code[1]:
        if code[0].count(check) != 1: valido = False

    if valido: reales.append(code[1])

print(reales[int(input("Ingrese el numero de la cadena a verificar: "))-1])
        