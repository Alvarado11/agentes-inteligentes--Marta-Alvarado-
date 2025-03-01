import heapq
import time

# Definir el entorno del laberinto
# 0 representa camino libre, 1 representa pared, 'E' es la entrada y 'S' la salida
laberinto = [
    ['E', 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 'S']
]

# Coordenadas de movimientos posibles: (fila, columna)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para imprimir el laberinto con la ruta del agente
def mostrar_laberinto(laberinto, ruta):
    lab_copy = [fila[:] for fila in laberinto]
    for r, c in ruta:
        if lab_copy[r][c] not in ['E', 'S']:
            lab_copy[r][c] = '*'
    
    for fila in lab_copy:
        print(" ".join(str(c) for c in fila))
    print()

# Algoritmo de búsqueda A* para encontrar la ruta más corta
def buscar_salida(laberinto):
    filas, columnas = len(laberinto), len(laberinto[0])
    
    # Encontrar la posición de entrada y salida
    inicio, meta = None, None
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == 'E':
                inicio = (i, j)
            elif laberinto[i][j] == 'S':
                meta = (i, j)
    
    if not inicio or not meta:
        print("Laberinto inválido: falta entrada o salida")
        return
    
    # Cola de prioridad para explorar nodos por costo
    cola = []
    heapq.heappush(cola, (0, inicio, []))  # (costo, nodo actual, ruta tomada)
    visitados = set()
    
    while cola:
        costo, (r, c), ruta = heapq.heappop(cola)
        
        if (r, c) in visitados:
            continue
        visitados.add((r, c))
        ruta = ruta + [(r, c)]
        
        # Si llegamos a la meta, mostramos la ruta
        if (r, c) == meta:
            print("Ruta encontrada:")
            mostrar_laberinto(laberinto, ruta)
            return
        
        # Explorar movimientos válidos
        for dr, dc in movimientos:
            nr, nc = r + dr, c + dc
            if 0 <= nr < filas and 0 <= nc < columnas and laberinto[nr][nc] != 1:
                heapq.heappush(cola, (costo + 1, (nr, nc), ruta))
        
        time.sleep(0.5)  # Simulación del tiempo de procesamiento
    
    print("No se encontró una ruta a la salida.")

if __name__ == "__main__":
    print("Laberinto Inicial:")
    mostrar_laberinto(laberinto, [])
    buscar_salida(laberinto)
