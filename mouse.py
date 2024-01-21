import ctypes

# Obtener la velocidad actual del mouse
get_mouse_speed = 112
speed = ctypes.c_int()
ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)
print(f"La velocidad actual del mouse es {speed.value}")

# Cambiar la velocidad del mouse a un valor entre 1 y 20
set_mouse_speed = 113
new_speed = 20  # Cambia este valor para ajustar la sensibilidad
ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, new_speed, 0)
print(f"La nueva velocidad del mouse es {new_speed}")

# Obtener la velocidad actual del mouse
get_mouse_speed = 112
speed = ctypes.c_int()
ctypes.windll.user32.SystemParametersInfoA(get_mouse_speed, 0, ctypes.byref(speed), 0)
print(f"La velocidad actual del mouse es {speed.value}")