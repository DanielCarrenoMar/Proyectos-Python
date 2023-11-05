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

def wach():    
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    nombre = input("Guardar como: ")
    open("clicks.txt", "w").write(nombre + ": " + str(clicks) + "\n")

def execute():
    clicks = open("clicks.txt", "r").read()
    clicks = clicks[0:clicks.find(":")], clicks[clicks.find(":")+4:-2].replace("(", "").replace(")", "").replace(" ", "").split(",")
    print(clicks)
    """"
    for x,y in clicks:
        click(x, y, espera)
    """

def click(x,y,espe=2):
    Controller().position = (x, y)
    sleep(espe)
    Controller().press(Button.left)
    Controller().release(Button.left)

def time(time=3):
    for i in range(time):
        sleep(1)
        print(F"Second {i+1}")


print("1. Save")
print("2. Execute")
print("3. Exit")
chose = int(input("Choose: "))
if chose == 1:
    wach()
elif chose == 2:
    execute()
elif chose == 3:
    exit()



