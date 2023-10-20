"""Leer 20 números e imprimir cuantos son positivos,
cuantos negativos y cuantos neutros."""
def num_20():
    numeros = []
    posi = 0
    nega = 0
    neu = 0
    
    for i in range(20):
        numeros.append(int(input("Numeros: ")))
    for i in numeros:
        if i < 0:
            nega += 1
        elif i > 0:
            posi += 1
        else:
            neu += 1

    print("")
    print("Numeros: ")
    print(f"Positivos: {posi} Negativos {nega} Neutros {neu}")

num_20()
