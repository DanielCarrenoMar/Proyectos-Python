

#########################
##### CONDICIONALES #####
#########################
"""
1) Un hombre desea saber cuanto dinero se genera por concepto de
interés sobre la cantidad que tiene en inversión en el banco. El decidirá
reinvertir los intereses siempre y cuando estos exceda a 7000$ y en ese
caso desea saber cuanto dinero tendrá finalmente en su cuenta.
"""
def f_interes_cond():
    inversion = float(input("Inversion: "))
    interes = float(input("Interes: "))
    interes = inversion * interes
    if interes > 7000:
        inversion += interes
    print(f"Inversion: {inversion}")


#######################
##### REPETITIVOS #####
#######################
"""
1) Leer 10 números e imprimir solamente los números
positivos
"""
def f_numeros_positivos_repe():
    numeros = []
    for i in range(3):
        numeros.append(int(input("Numero: ")))
    print("")
    for i in numeros:
        if i > 0:
            print(Fore.LIGHTGREEN_EX,f"{i} es positivo."+Style.RESET_ALL, end=" ")
        else:
            print(Fore.LIGHTRED_EX,f"{i} es negativo."+Style.RESET_ALL, end=" ")

"""
2) Leer 20 números e imprimir cuantos son positivos,
cuantos negativos y cuantos neutros.
"""
def f_num_20_repe():
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

"""
3) Leer 15 números negativos y convertirlos a positivos e
imprimir la suma de dichos números.
"""
def f_suma_negativa_repe():
    suma = 0
    for i in range(5):
        num = int(input("Numero: "))
        suma += abs(num)
    print (suma)

"""
4) Calcular e imprimir la tabla de multiplicar de un número
cualquiera. Imprimir el multiplicando, el multiplicador y
el producto
"""
def  f_tablas_multiplicar_repe():
    num = int(input("Numero: "))
    for i in range(1,9):
        print(f"{num} x {i} = {num*i}")

"""
5) Suponga que se tiene un conjunto de calificaciones de
un grupo de 40 alumnos. Realizar un algoritmo para
calcular la calificación media y la calificación más baja
de todo el grupo
"""
