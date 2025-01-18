import math
# DEFINIMOS LOS METODOS PARA HACER LAS CONVERSIONES.
def decimal_binario(num):
    exp = 0
    while True:
        if math.pow(2,exp) >= num:
            break
        exp += 1
    exp -=1
    return exp
import math

numbin = 1011011
cadbin = str(numbin)
tamagno = len(cadbin)
numerodecimal = 0

print(f'El tamaño es: {tamagno}')

# Recorremos la cadena binaria
for i in range(tamagno):
    # Calculamos la posición desde la derecha
    exponente = tamagno - 1 - i
    if cadbin[i] == '1':  # Si el bit actual es 1
        numerodecimal += math.pow(2, exponente)
        print(f'Bit {i} (exponente {exponente}): {numerodecimal}')

print(f'El número decimal es: {numerodecimal}')

### FORMA ALTERNATIVA DE HACERLO. ###

##numbin = 1011011
##cadbin = str(numbin)
##tamagno = int(cadbin.__len__())
##print(tamagno)
##numerodecimal = 0
##contador = tamagno - 1
##print(f'el tamaño es: {tamagno}')
##for digito in cadbin:
##    if digito == '1':
##        numerodecimal += math.pow(2,contador)
##        print(f'{contador}: {numerodecimal}')
##    contador-=1

##print(numerodecimal)