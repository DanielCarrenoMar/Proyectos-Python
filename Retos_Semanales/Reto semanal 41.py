"""
 * Este es un reto especial por Halloween.
 * Te encuentras explorando una mansión abandonada llena de habitaciones.
 * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
 * Tu misión es encontrar la habitación de los dulces.
 *
 * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
 * (Tienes total libertad para ser creativo con los textos)
 *
 * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
 *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
 *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
 *   Esta podría ser una representación:
 *   🚪⬜️⬜️⬜️
 *   ⬜️👻⬜️⬜️
 *   ⬜️⬜️⬜️👻
 *   ⬜️⬜️🍭⬜️
 * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
 *   Si no lo aciertas no podrás desplazarte.
 * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
 *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
 * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
 * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
 *   tengas que responder dos preguntas para salir de ella.
 """
from random import randrange
from numpy import *
from os import system
import time
from colorama import *

# 0 ⬜️ 1 🚪 2 ⬛ 3 👻 4 🍭 
elementos = ["⬜️", "🚪", "⬛", "👻", "🍭"]

class Game:
    def __init__(self,xy):
        self.xy = xy
        self.posX = 0
        self.posY = 0
    def casa(self):
        self.casa = zeros(shape=(self.xy,self.xy), dtype=int)
        self.casajugador = zeros(shape=(self.xy,self.xy), dtype=int)
        self.casajugador[0][0] = 1

        puerta = randrange(0, self.xy)

        for y in range(self.xy):
            for x in range(self.xy):
                if x == 0 and y == 0:
                    self.casa[y][x] = 1
                elif x == puerta and y == self.xy-1:
                    self.casa[y][x] = 4
                else:
                    if randrange(0,10) == 0:
                        self.casa[y][x] = 3
                    else:
                        self.casa[y][x] = 0
    
    def dibujar(self):
        print("Posicion del jugador:", Fore.LIGHTRED_EX, self.posX, self.posY,Style.RESET_ALL)
        print("", end="       ")
        for y in range(self.xy):
            for x in range(self.xy):
                if self.casajugador[y][x] == 0:
                    print(elementos[0], end= " ")
                elif self.casajugador[y][x] == 1:
                    print(elementos[1], end= " ")
                elif self.casajugador[y][x] == 2:
                    print(elementos[2], end= " ")
                elif self.casajugador[y][x] == 3:
                    print(elementos[3], end= " ")
                elif self.casajugador[y][x] == 4:
                    print(elementos[4], end= " ")
            print("")
            print("", end="       ")
        print("")
    def mover(self):
        opciones = {"Derecha":False,"Izquierda":False,"Arriba":False,"Abajo":False}

        if self.posX+1 < self.xy:
            opciones["Derecha"] = True
        if self.posX-1 >= 0:
            opciones["Izquierda"] = True
        if self.posY-1 >= 0:
            opciones["Arriba"] = True
        if self.posY+1 >= 0:
            opciones["Abajo"] = True
        
        print("Te puedes mover a: "), print("")

        for a,b in opciones.items():
            if b == True:
                print(a)

        print("")

        eleccion = input("A donde desea moverse: ")

        if eleccion == "Derecha" or eleccion == "derecha" or eleccion == "de" and opciones["Derecha"] == True:
            self.posX += 1
        if eleccion == "Izquierda" or eleccion == "izquierda" or eleccion == "iz" and opciones["Izquierda"] == True:
            self.posX -= 1
        if eleccion == "Arriba" or eleccion == "arriba" or eleccion == "ar" and opciones["Arriba"] == True:
            self.posY -= 1
        if eleccion == "Abajo" or eleccion == "abajo" or eleccion == "ab" and opciones["Abajo"] == True:
            self.posY += 1

        if self.casa[self.posY][self.posX] == 0:
            self.casajugador[self.posY][self.posX] = 2
        elif self.casa[self.posY][self.posX] == 3:
            self.casajugador[self.posY][self.posX] = 3
        else:
            self.casajugador[self.posY][self.posX] = self.casa[self.posY][self.posX]

    def verificar_habitacion(self):
        if self.casa[self.posY][self.posX] == 0:
            frases = ["O, parece que estas en una habitacion vacia... ¡¿pero que es eso de ahí?!, hay un papel en una mesa que dice:",
                      
                      ]

            print(frases[randrange(0,len(frases))])
   
            self._pregunta() 

        elif self.casa[self.posY][self.posX] == 3:
            frasesfant = ["¡Oh no! ¡Hay un fantasma!, y peor aun ¡Es un fanatico de los quiz!",
                           "*Musica de undertale*"]
            
            print(frasesfant[randrange(0,len(frasesfant)-1)])

            print("      .-."+"\n"
                "     (o o) boo!"+"\n"
                "     | O \ "+"\n"
                "     \   \ "+"\n"
                "     `~~~' ")

            self._pregunta()

            system("cls")
            print("Pero ahora... ¡Comienza la pregunta BONUS!")

            self._pregunta()

        elif self.casa[self.posY][self.posX] == 4:
            print(Fore.MAGENTA+"¡Felicidades! ¡Has encontrado la habitacion de los dulces!"+Style.RESET_ALL)
            print("")
            return(True)
    
    def _pregunta(self):
        preguntas = [
            "¿Cuál es el lugar más frío de la tierra?",
            "¿Quién escribió La Odisea?",
            "¿Dónde originaron los juegos olímpicos?",
            "¿Cuál es el río más largo del mundo?",
            "¿Quién escribió la novela 'Cien años de soledad'?",
            "¿Cuál es el país más grande del mundo por área?",
            "¿Quién pintó la obra 'La noche estrellada'?",
            "¿Cuál es el océano más grande del mundo?",
            "¿En qué año se lanzó el primer juego de Super Mario Bros?",
            "¿Cuál es el nombre del personaje principal en la serie de juegos 'The Legend of Zelda'?",
            "¿Cuál es el nombre del personaje principal en la serie de juegos 'Assassin's Creed'?",
            "¿Cuál es el nombre del personaje principal en la serie de juegos 'Final Fantasy'?",
            "¿Cuál es el nombre del personaje principal en la serie de juegos 'Metal Gear Solid'?"
            ]
        respuestas = [
            ["la antartida", "antartida"],
            ["homero"],
            ["olimpia"],
            "nilo",
            "gabriel garcia marquez",
            "rusia",
            "vincent van gogh",
            "pacifico",
            "1985",
            "link",
            "desmond miles",
            "cloud strife",
            "solid snake"
            ]
        
        while True:
            pregunta = randrange(0,len(preguntas))

            print("|"+preguntas[pregunta]+"|")
            print("")

            respuesta = input("Ingrese su respuesta: ")

            if respuesta.lower() in respuestas[pregunta]:
                system("cls")

                print(Fore.GREEN+"¡Correcto!"+Style.RESET_ALL)
                self.casa[self.posY][self.posX] = 2

                time.sleep(1)
                break  

            else:
                system("cls")
                print(Fore.RED+"Incorrecto, siguiente pregunta..."+Style.RESET_ALL)
                time.sleep(1)
                system("cls")

mansion = Game(4)
mansion.casa()
while True:
    
    mansion.dibujar()
    mansion.mover()
    system("cls")
    mansion.dibujar()
    if mansion.verificar_habitacion() == True:
        break
    else:
        pass
    system("cls")