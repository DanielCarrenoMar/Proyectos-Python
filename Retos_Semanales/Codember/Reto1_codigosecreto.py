"""
** El reto **
Los mensajes son palabras separadas por espacios como este:
gato perro perro coche Gato peRRo sol
Necesitamos que el programa nos devuelva el número de veces que aparece cada palabra en el mensaje, independientemente 
de si está en mayúsculas o minúsculas.
El resultado será una cadena de texto con la palabra y el número de veces que aparece en el mensaje, con este formato:
gato2perro3coche1sol1
¡Las palabras son ordenadas por su primera aparición en el mensaje!
** Más ejemplos: **
llaveS casa CASA casa llaves -> llaves2casa3
taza ta za taza -> taza2ta1za1
casas casa casasas -> casas1casa1casas1
"""
codigo = open("Proyectos-en-Python\\Retos_Semanales\\Codember\\Reto1_codigosecreto.txt", "r").read().lower().split(" ")
palabras = {}

for i in codigo:
    if i not in palabras:
        palabras[i] = 1
    else:
        palabras[i] += 1

for pala, num in palabras.items():
    print(F"{pala}{num}", end="")
