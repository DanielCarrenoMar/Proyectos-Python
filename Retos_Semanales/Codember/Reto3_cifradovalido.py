claves = open("Proyectos-en-Python\\Retos_Semanales\\Codember\\Reto3_cifradovalido.txt", "r").read().splitlines()
invalidas = []
validas = 0

for clave in claves:
    min, max = clave[0:clave.index(":")].split(" ")[0].split("-")
    letra = clave[0:clave.index(":")].split(" ")[1]
    codigo = clave[clave.index(": ")+1:]

    if int(min) <= codigo.count(letra) <= int(max):
        validas += 1
    else:
        invalidas.append(codigo)

print("Validas:",validas)
print("Invalidas:", len(invalidas))
print(invalidas[int(input("Elija una posicion de las invalidas: "))])