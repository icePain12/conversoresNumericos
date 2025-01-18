from generador_aleatorio.generarbinarios_chatGPT import generar_binario
from conversor_sistemas_numericos.conversiones_numericas import binario_decimal
from os import system

# VARIABLES DE ENTORNO
__pruebas__ = 100
__funcion__ = 0  # 0 es para probar la función binario a decimal


def main():
    if __funcion__ == 0:
        probar_binarioDecimal()


def probar_binarioDecimal():
    system("color a && cls")
    lista_binarios = [generar_binario() for _ in range(__pruebas__)]
    escribir(lista_binarios, output='pantalla')  # Cambia a 'archivo' si deseas guardar en archivo.


def escribir(lista_binarios, output='pantalla'):
    resultados = [
        f"{i + 1}) {binario} en binario es {binario_decimal(binario)} en decimal\n"
        for i, binario in enumerate(lista_binarios)
    ]

    if output == 'pantalla':
        print("".join(resultados))
    elif output == 'archivo':
        try:
            with open("conversiones_ejemplo.txt", 'w') as archivo:
                archivo.writelines(resultados)
            print("Archivo creado exitosamente")
        except IOError as e:
            print(f"Error al crear o escribir en el archivo conversiones_ejemplo.txt: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


if __name__ == '__main__':
    main()
