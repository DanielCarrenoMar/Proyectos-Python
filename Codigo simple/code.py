class Coche:
        def __init__(self, marca, modelo):
                self.marca = marca
                self.modelo = modelo
                self.arrancado = False
        
        def arrancar(self):
                self.arrancado = True
                print("El", self.modelo, self.marca, "ha arrancado")

        def parar(self):
                self.arrancado = False
                print("El", self.modelo, self.marca, "ha PARADO")

laguna = Coche("Renol", "Laguna")
tesla = Coche("Tesla", "Model 3")

print(laguna.modelo, laguna.marca)
print(tesla.modelo, tesla.marca)

laguna.arrancar()
tesla.arrancar()

print(laguna.arrancado)
print(tesla.arrancado)

laguna.parar()
tesla.parar()
