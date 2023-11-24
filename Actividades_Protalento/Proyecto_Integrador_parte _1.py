
# Proyecto Integrador parte 1
# El proyecto de este curso consistirá en un videojuego de texto de recorrer laberintos. Este consistirá de laberintos representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje.
# Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.


import random

# Tamaño del laberinto
MAZE_WIDTH = 10
MAZE_HEIGHT = 10

# Caracteres del laberinto
WALL = "#"
PASSAGE = "."
PLAYER = "P"
EXIT = "E"

# Laberinto aleatorio
maze = [[random.choice([WALL, PASSAGE]) for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
maze[0][0] = PLAYER
maze[MAZE_HEIGHT - 1][MAZE_WIDTH - 1] = EXIT

# Posición inicial del jugador
player_x, player_y = 0, 0

# Función para imprimir el laberinto
def print_maze():
    for row in maze:
        print(" ".join(row))

# Solicitar el nombre del jugador
nombre_jugador = input("Ingresa tu nombre: ")
print(f"Bienvenido, {nombre_jugador}!")

# Bucle principal del juego
while True:
    print_maze()
    movimiento = input("Mueve al jugador (↑ ↓ ← →, q para salir): ").strip().lower()

    if movimiento == "q":
        break

    dx, dy = 0, 0

    if movimiento == "↑":
        dy = -1
    elif movimiento == "↓":
        dy = 1
    elif movimiento == "←":
        dx = -1
    elif movimiento == "→":
        dx = 1

    new_x = player_x + dx
    new_y = player_y + dy

    if (
        0 <= new_x < MAZE_WIDTH
        and 0 <= new_y < MAZE_HEIGHT
        and maze[new_y][new_x] != WALL
    ):
        maze[player_y][player_x] = PASSAGE
        player_x = new_x
        player_y = new_y
        maze[player_y][player_x] = PLAYER

        if maze[player_y][player_x] == EXIT:
            print("¡Felicidades! Has encontrado la salida.")
            break