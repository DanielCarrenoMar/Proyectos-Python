def quicksort(lista):
    if len(lista) < 2:
        return lista

    menor , pivot, mayor = particion(lista)

    print(menor, pivot, mayor)

    return quicksort(menor),[pivot], quicksort(mayor)

def particion(lista):
    pivot = lista.pop(-1)
    menor = []
    mayor = []
    i = 0

    for j in range(len(lista)):
        if lista[j] <= pivot:
            menor.append( lista[j])
        else:
            mayor.append(lista[j])

    return menor, pivot, mayor

a,b,c = quicksort([3,6,21,6,3,1,8,3,22,4,9])            

print("menor", a, "pivot" ,b, "mayor", c)