"""
3) Leer 15 números negativos y convertirlos a positivos e
imprimir la suma de dichos números.
"""

def suma_negativa():
    suma = 0
    for i in range(5):
        num = int(input("Numero: "))
        suma += abs(num)
    print (suma)

suma_negativa()
