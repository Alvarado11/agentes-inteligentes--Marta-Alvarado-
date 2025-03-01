import heapq
import time

# Definir el entorno con valores de recompensa en cada celda
# Celdas con valores más altos representan mayores recompensas
entorno = [
    [3, 1, 4, 2, 8],
    [5, 2, 3, 7, 1],
    [2, 6, 8, 3, 4],
    [1, 3, 2, 4, 7],
    [4, 7, 1, 5, 9]
]

# Coordenadas de movimientos posibles: (fila, columna)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para imprimir el entorno con la ruta del agente
def mostrar_entorno(entorno, ruta):
    """Muestra la matriz del entorno con la ruta recorrida marcada con '*'."""
    entorno_copy = [fila[:] for fila in entorno]  # Copia del entorno original para no modificarlo
    for r, c in ruta:
        entorno_copy[r][c] = '*'  # Marcar la ruta en la matriz
    
    for fila in entorno_copy:
        print(" ".join(str(c) if c != '*' else c for c in fila))  # Imprimir la matriz con la ruta
    print()

# Algoritmo para seleccionar la mejor ruta basada en utilidad
def encontrar_ruta_optima(entorno):
    """Encuentra la ruta con la mayor utilidad desde la esquina superior izquierda hasta la inferior derecha."""
    filas, columnas = len(entorno), len(entorno[0])
    inicio, meta = (0, 0), (filas - 1, columnas - 1)  # Definir inicio y meta
    
    # Cola de prioridad max-heap para evaluar rutas basadas en recompensa
    cola = []
    heapq.heappush(cola, (-entorno[0][0], inicio, []))  # Se usa negativo para simular un max-heap
    visitados = set()
    
    while cola:
        utilidad_neg, (r, c), ruta = heapq.heappop(cola)  # Obtener el nodo con mayor recompensa
        
        if (r, c) in visitados:
            continue  # Evitar visitar nodos ya explorados
        visitados.add((r, c))
        ruta = ruta + [(r, c)]  # Agregar nodo a la ruta
        
        # Si llegamos a la meta, mostramos la ruta óptima
        if (r, c) == meta:
            print("Ruta óptima encontrada:")
            mostrar_entorno(entorno, ruta)
            return
        
        # Explorar movimientos válidos
        for dr, dc in movimientos:
            nr, nc = r + dr, c + dc
            if 0 <= nr < filas and 0 <= nc < columnas:
                heapq.heappush(cola, (-entorno[nr][nc], (nr, nc), ruta))  # Agregar nuevo nodo con prioridad
        
        time.sleep(0.5)  # Simulación del tiempo de procesamiento
    
    print("No se encontró una ruta a la meta.")

if __name__ == "__main__":
    print("Entorno Inicial:")
    mostrar_entorno(entorno, [])  # Mostrar el entorno original
    encontrar_ruta_optima(entorno)  # Ejecutar el algoritmo para encontrar la mejor ruta

