import os

def string_to_map(map_string):
    map_list = map_string.strip().split('\n')
    map_matrix = [list(row) for row in map_list]
    return map_matrix

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_game_loop(map_matrix, initial_position, final_position):
    px, py = initial_position

    while (px, py) != final_position:
        clear_screen()
        map_matrix[py][px] = 'P'
        print_map(map_matrix)

        move = input("Mueve al jugador con las teclas de flecha (↑, ↓, ←, →): ")

        if move == '↑' and py > 0 and map_matrix[py - 1][px] != '#':
            map_matrix[py][px] = '.'
            py -= 1
        elif move == '↓' and py < len(map_matrix) - 1 and map_matrix[py + 1][px] != '#':
            map_matrix[py][px] = '.'
            py += 1
        elif move == '←' and px > 0 and map_matrix[py][px - 1] != '#':
            map_matrix[py][px] = '.'
            px -= 1
        elif move == '→' and px < len(map_matrix[0]) - 1 and map_matrix[py][px + 1] != '#':
            map_matrix[py][px] = '.'
            px += 1

    clear_screen()
    map_matrix[py][px] = 'P'
    print_map(map_matrix)
    print("¡Has llegado al final!")

def print_map(map_matrix):
    for row in map_matrix:
        print(''.join(row))

# Ejemplo de mapa de laberinto (reemplaza con tu propio mapa)
laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = string_to_map(laberinto)

# Posición inicial y final (ajusta estas coordenadas según tu propio laberinto)
posicion_inicial = (0, 0)
posicion_final = (9, 9)

main_game_loop(mapa, posicion_inicial, posicion_final)
