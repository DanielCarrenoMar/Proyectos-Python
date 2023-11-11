"""
Las operaciones del lenguaje son las siguientes:

"#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.

"""

codigo = list(open("Proyectos-en-Python\\Retos_Semanales\\Codember\\Reto2_sumaconsimbolos.txt", "r").read())
valor = 0

for i in codigo:
    if i == "#":
        valor += 1
    elif i == "@":
        valor -= 1
    elif i == "*":
        valor **= 2
    elif i == "&":
        print(valor, end="")