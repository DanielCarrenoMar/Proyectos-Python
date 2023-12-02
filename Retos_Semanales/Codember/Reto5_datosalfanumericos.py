"""
- id: existe y es alfanumérica
- username: existe y es alfanumérico
- email: existe y es válido (sigue el patrón user@dominio.com)
- age: es opcional pero si aparece es un número
- location: es opcional pero si aparece es una cadena de texto
"""
usuarios = open("Proyectos-en-Python\\Retos_Semanales\\Codember\\Reto5_datosalfanumericos.txt", "r").readlines()
mensaje = ""

for usu in usuarios:
    ususpli = usu[1:].split(",")
    ususpli[0] = usu[:1] + ususpli[0]
    valido = True

    if not ususpli[0].isalnum() or not ususpli[1].isalnum() or not (ususpli[2].count("@") == 1 and ususpli[2].endswith(".com")):
        valido = False
    try:
        if not ususpli[3].isdigit() and ususpli[3] != "" or not ususpli[4].isascii():
            valido = False
    except:
        pass
    
    if valido == False:  
        mensaje += ususpli[1][0:1]
        pass
        

print(mensaje)