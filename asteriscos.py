def astericos(cadena:str, subcadena:str) -> str:
    newCadena:str = ""
    palabra:str = ""
    cambio:bool = False
    for index in range(len(cadena)):
        if (cadena[index] == " " and cadena[index+1] != " ") or cadena[index] == ",":
            if palabra.find(subcadena) != -1:
                cambio = True
                newCadena += " "+"*"*len(palabra)
            else:
                newCadena += palabra
            palabra = ""
        palabra += cadena[index]
    if cambio:
        return newCadena
    else:
        return "Texto sin cambio, la subcadena no fue encontrada en el texto”."
    
print(astericos("hola soy soy daniel aqui daniel .", "aqu"))