def mergesort(lista):
    if len(lista) < 2:
        return lista
    else:
        middle = len(lista) // 2
        right = mergesort(lista[:middle])
        left = mergesort(lista[middle:])
        print(right, left)
        return merge(right, left)
    
def merge(lista1, lista2):
    i, j = 0, 0
    result = []
    while(i < len(lista1) and j < len(lista2)):
        if lista1[i] < lista2[j]:
            result.append(lista1[i])
            i += 1
        else:
            result.append(lista2[j])
            j += 1
    result += lista1[i:]
    result += lista2[j:]
    return result

lista = [4,5,67,8,2,4,7,1,2,3, 4]
print(mergesort(lista))