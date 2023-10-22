from pynput import keyboard
from time import sleep

def on_activate_1():
    print("exit")
    

def on_activate_2():
    keyboard.Controller().press('"')
    keyboard.Controller().release(keyboard.Key.shift)
    keyboard.Controller().press(keyboard.Key.left)

def on_activate_3():
    keyboard.Controller().press(")")
    keyboard.Controller().release(keyboard.Key.shift)
    keyboard.Controller().press(keyboard.Key.left)

with keyboard.GlobalHotKeys({
        '<shift>+2': on_activate_2,
        '<shift>+8': on_activate_3,
        '<shift>+q': exit}) as h:
    h.join()
