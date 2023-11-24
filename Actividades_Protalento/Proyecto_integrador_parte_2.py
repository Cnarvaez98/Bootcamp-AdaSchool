import readchar

# Bucle infinito
while True:
    # Leer un carácter del teclado
    char = readchar.readchar()

    # Imprimir el carácter leído
    print(f'Carácter leído: {char}')

    # Comprobar si se presionó la tecla de flecha hacia arriba (UP)
    if char == '\x1b[A':
        print("Tecla de flecha hacia arriba (UP) presionada. Saliendo del programa.")
        break
