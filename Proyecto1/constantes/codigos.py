import keyboard
import time
import subprocess

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
        code = 'python -u "c:\\Users\\EQUIPO i3\\Documents\\Codigos\\Proyecto1\\constantes\\code\\Basadobot.py"'
        subprocess.call(code, shell=True)
        print("Codigo 2")