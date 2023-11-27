from pynput.mouse import Button, Controller
from pynput import mouse
from time import sleep
from os import system

#Segundos de espera entre click
espera = 1

clicks = []
try:
    save = eval(open("Save.txt","r").read())
except:
    save = {}
    open("Save.txt","w")

def on_click(x, y, button, pressed):
    if pressed == True and button == Button.left:
        clicks.append(["click", x, y])
        print(clicks)

    if button == Button.middle:
        return False
    
def on_scroll(x, y, dx, dy):
    
    if len(clicks) == 0 or clicks[-1][0] != "scroll":
        clicks.append(["scroll",dx ,dy])
        print(clicks)
        return

    if dx * clicks[-1][1] >= 0 and dy * clicks[-1][2] >= 0:
        clicks[-1][1] += dx ; clicks[-1][2] += dy
        print(clicks)
        return
    else:
        clicks.append(["scroll",dx ,dy])
        print(clicks)

def time(time=3):
    for i in range(time):
        sleep(1)
        print(F"Second {i+1}")

def click(x,y,espe=2):
    Controller().position = (x, y)
    sleep(espe)
    Controller().press(Button.left)
    Controller().release(Button.left)

def scroll(dx,dy,espe=2):
    
    Controller().scroll(dx,dy)
    sleep(espe)

def wach():
    system("cls")
    print("Grabando clicks PULSE CLICK CENTRAL PARA TERMINAR")
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

    system("cls")
    print("Guardando clicks... Por favor ingresar nombre del archivo")
    save_name = input("Nombre: ")
    save[save_name] = clicks

    system("cls")
    try:
        open("Save.txt","w").write(str(save))
        print("Guardado")
    except:
        print("Error al guardar")

def execute():
    system("cls")
    save = eval(open("Save.txt","r").read())
    print(save.keys())
    while True:
        choise = input("Elegir guardado: ")
        try:
            clicks = save[choise]
            break
        except:
            print("Error al cargar")

    system("cls")
    repetir = int(input("Repetir cuantas veces: "))
    system("cls")

    time(3)
    for i in range(repetir):
        for name,x,y in clicks:
            if name == "click":
                click(x, y, espera)
            elif name == "scroll":
               scroll(x, y, espera)
    system("cls")

def delete():
    system("cls")
    save = eval(open("Save.txt","r").read())
    print(save.keys())
    while True:
        choise = input("Elegir guardado: ")
        try:
            save.pop(choise)
            open("Save.txt","w").write(str(save))
            break
        except:
            print("Error al eliminar")
    system("cls")
#MENU
while True:
    print("1. Guardar clicks")
    print("2. Borrar clicks guardados")
    print("3. Ejecutar clicks")
    print("4. Salir del programa")
    chose = int(input("Choose: "))
    match chose:
        case 1:
            time(3)
            wach()
        case 2:
            delete()
        case 3:
            execute()
        case 4:
            break


