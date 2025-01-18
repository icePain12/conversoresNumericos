import random

# Función para generar un número binario aleatorio entre 0 y 10000
def generar_binario():
    return format(random.randint(0, 10000), 'b')
