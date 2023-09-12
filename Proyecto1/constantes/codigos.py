import keyboard
import time
import subprocess
import os

Nombres = {
    "Prueba1": "codigo1",
    "Prueba2": "codigo2"
}
class corazon():
    def Codigo1(input, num):
        time.sleep(2)
        a = 1
        while a <= int(num):
            keyboard.write(input)
            keyboard.press_and_release("enter")
            a += 1


    def Codigo2():
        print("Code2")