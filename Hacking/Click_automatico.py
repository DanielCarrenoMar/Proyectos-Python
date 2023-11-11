from pynput.mouse import Button, Controller
from pynput import mouse
from time import sleep

espera = 1
clicks = []

def on_click(x, y, button, pressed):
    if Controller().position not in clicks and button == Button.left:
        clicks.append(Controller().position)
        print(clicks)

    if button == Button.middle:
        return False
    
def on_scroll(x, y, button, pressed):
    print("a")

def wach():
    print("Grabando clicks PULSE CLICK CENTRAL PARA TERMINAR")
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
    print("Guardado")

def execute():
    repetir = int(input("Repetir cuantas veces: "))
    time(3)

    for i in range(repetir):
        for x,y in clicks:
            click(x, y, espera)

def click(x,y,espe=2):
    Controller().position = (x, y)
    sleep(espe)
    Controller().press(Button.left)
    Controller().release(Button.left)

def time(time=3):
    for i in range(time):
        sleep(1)
        print(F"Second {i+1}")

wach()
execute()


"""
MENU

print("1. Guardar clicks")
print("2. Ejecutar clicks")
print("3. Salir del programa")
chose = int(input("Choose: "))
if chose == 1:
    wach()
elif chose == 2:
    execute()
elif chose == 3:
    exit()
"""


