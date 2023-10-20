"""
Calcular e imprimir la tabla de multiplicar de un número
cualquiera. Imprimir el multiplicando, el multiplicador y
el producto
"""
def  tablas_multiplicar(num):
    for i in range(1,9):
        print(f"- {num} x {i} = {num*i}")
        
tablas_multiplicar(4)
