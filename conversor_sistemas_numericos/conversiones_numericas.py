import math
def binario_decimal(numbin=0):
    cadbin = str(numbin)
    tamagno = int(cadbin.__len__())
    #print(tamagno)
    numerodecimal = 0
    contador = 0
    exponente = tamagno -1
    while contador < tamagno:
        if cadbin[contador] == '1':
            numerodecimal += math.pow(2,exponente)
        contador+=1
        exponente-=1
    return numerodecimal

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