from pynput import keyboard
from time import sleep

funciones = ["print()","input()"]
i = 0

def on_activate_2():
    keyboard.Controller().press('"')
    keyboard.Controller().release(keyboard.Key.shift)
    keyboard.Controller().press(keyboard.Key.left)

def on_activate_3():
    keyboard.Controller().press(")")
    keyboard.Controller().release(keyboard.Key.shift)
    keyboard.Controller().press(keyboard.Key.left)

def on_activate_4():
    keyboard.Controller().press(keyboard.Key.backspace)
    keyboard.Controller().press("[")
    keyboard.Controller().press("]")
    keyboard.Controller().release(keyboard.Key.shift)
    keyboard.Controller().press(keyboard.Key.left)

def on_activate_print():
    global i

    keyboard.Controller().release(keyboard.Key.alt)
    keyboard.Controller().press(keyboard.Key.backspace)
    keyboard.Controller().type(funciones[i])

    keyboard.Controller().press(keyboard.Key.left)

    i = (i+1) % len(funciones)
    print("valor: ", i)

with keyboard.GlobalHotKeys({
        '<shift>+2': on_activate_2,
        '<shift>+8': on_activate_3,
        '<shift>+ñ': on_activate_4,
        '<alt>+w': on_activate_print,
        '<shift>+q': exit}) as h:
    h.join()

