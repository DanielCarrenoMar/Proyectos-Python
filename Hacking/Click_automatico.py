from pynput.mouse import Button, Controller
from pynput import mouse
from time import sleep

#mouse = Controller()
espera = 0.8
clicks = []

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    clicks.append(mouse.position)
    print(clicks)
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()


#ciclo = int(input("ciclos de click: "))



def click(x,y,espe=2):
    mouse.position = (x, y)
    sleep(espe)
    mouse.press(Button.left)
    mouse.release(Button.left)

"""for i in range(ciclo):
    sleep(espera)
    mouse.scroll(0, -2)
    click(895, 651, espera)
    click(481, 306, espera)
    click(479, 337, espera)
    click(493, 390, espera)
    click(573, 207, espera)
"""