from pynput.keyboard import Key, Listener, Controller
from os import *


teclado = Controller()
keys = []

def presionar_tecla(key):
    keys.append(key)

def soltar_tecla(key):
    if key == Key.esc:
        return False
    if key == Key.space:
        teclado.press(' ')


with Listener(on_press = presionar_tecla, on_release = soltar_tecla) as listener:
    listener.join()


