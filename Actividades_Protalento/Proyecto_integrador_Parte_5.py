import os
import random

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    def mover(self, direccion):
        x, y = self.inicio
        if direccion == "arriba":
            x -= 1
        elif direccion == "abajo":
            x += 1
        elif direccion == "izquierda":
            y -= 1
        elif direccion == "derecha":
            y += 1
        if 0 <= x < len(self.mapa) and 0 <= y < len(self.mapa[0]) and self.mapa[x][y] != "#":
            self.inicio = (x, y)
        if self.inicio == self.fin:
            return "¡Ganaste!"
        return "Sigue intentando."

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, fin = self.cargar_mapa_random(path_a_mapas)
        super().__init__(mapa, inicio, fin)

    def cargar_mapa_random(self, path_a_mapas):
        archivos_de_mapas = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(archivos_de_mapas)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)
        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
            dimensiones = lineas[0].strip().split()
            filas, columnas = int(dimensiones[0]), int(dimensiones[1])
            mapa = [linea.strip() for linea in lineas[1:1 + filas]]
            
            try:
                inicio = tuple(map(int, lineas[1 + filas].strip().split()))
                fin = tuple(map(int, lineas[2 + filas].strip().split()))
            except ValueError:
                raise ValueError("Las coordenadas de inicio o fin no son números enteros válidos en el archivo de mapa.")
            
        return mapa, inicio, fin

# Ejemplo de uso:
if __name__ == "__main__":
    juego = JuegoArchivo("C:/Users/cnarv/OneDrive/Escritorio/carpeta_con_mapas")
    while True:
        print("\n".join(juego.mapa))
        print("Coordenadas de inicio:", juego.inicio)
        print("Coordenadas de fin:", juego.fin)
        direccion = input("Ingresa una dirección (arriba/abajo/izquierda/derecha): ")
        resultado = juego.mover(direccion)
        print(resultado)
        if resultado == "¡Ganaste!":
            break
