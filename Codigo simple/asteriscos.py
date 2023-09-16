num = int(input("ingrese numero: "))
asteriscos = ""
cont = num
cont1 = 1
while cont1 < num:
    asteriscos += "*"*cont1
    print(asteriscos)
    asteriscos = ""
    cont1 += 1
while cont > 0:
    asteriscos += "*"*cont
    print(asteriscos)
    asteriscos = ""
    cont -= 1