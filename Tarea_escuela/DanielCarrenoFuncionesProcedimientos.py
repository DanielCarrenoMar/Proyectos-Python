from os import system

def logitud(cadena):
    return len(cadena)

def secuencia(num):
    secu = ""
    impri = ""
    for i in range(1,num+1):
        secu += str(i)

    for i in range(num,0,-1):
        for j in range(0,i):
            impri += secu[j]
        print(impri)
        impri = ""

def calculadora():
    def menu():
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        return input("Elija:")
    
    print("Bienvenido a la calculadora")
    print("Ingrese los numeros a operar")

    num1 = int(input("Numero 1:"))
    num2 = int(input("Numero 2:"))

    match elec := menu():
        case "1":
            print("La suma es:",num1+num2)
        case "2":
            print("La resta es:",num1-num2)
        case "3":
            print("La multiplicacion es:",num1*num2)

while True:
    print("Ejercicios de Funciones y Procedimientos".center(50,"-"))
    print("1- Longitud de una cadena")
    print("2- Secuencia de numeros")
    print("3- Calculadora")
    print("4- Salir")
    try:
        match elec := input("Elija el ejercicio a ejecutar: "):
            case "1":
                system("cls")
                print(logitud(input("Ingrese una cadena:")))
                input("Presione cualquier tecla para continuar")
            case "2":
                system("cls")
                secuencia(int(input("Ingrese un numero:")))
                input("Presione cualquier tecla para continuar")
            case "3":
                system("cls")
                calculadora()
                input("Presione cualquier tecla para continuar")
            case "4":
                exit()
    except ValueError:
        print("Ingrese un numero correcto")
        input("Presione cualquier tecla para continuar")