import os

# Función para borrar la terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicializar el número en 0
numero = 0

while numero <= 50:
    # Borrar la terminal
    clear_terminal()

    # Imprimir el nuevo número
    print(f'Número actual: {numero}')

    # Leer la tecla 'n' del teclado
    tecla = input('Presiona "n" para continuar: ')

    if tecla == 'n':
        numero += 1
    else:
        print('Tecla incorrecta. Presiona "n" para continuar.')

print('Has alcanzado el número 50. ¡Terminado!')
