import random
import time

# Definir el entorno como una cuadrícula
# 0 representa una celda libre, 1 representa un obstáculo

def crear_entorno(filas, columnas):
    return [[0 if random.random() > 0.2 else 1 for _ in range(columnas)] for _ in range(filas)]

# Función para imprimir el entorno visualmente
def mostrar_entorno(entorno, posicion):
    for i, fila in enumerate(entorno):
        fila_str = ""
        for j, celda in enumerate(fila):
            if (i, j) == posicion:
                fila_str += "A "  # Representar al agente
            elif celda == 1:
                fila_str += "# "  # Representar obstáculo
            else:
                fila_str += ". "  # Representar camino libre
        print(fila_str.strip())
    print()

# Movimiento del agente en la cuadrícula
def mover_agente(entorno, posicion_inicial):
    filas, columnas = len(entorno), len(entorno[0])
    posicion = posicion_inicial
    visitados = set()  # Guardar las posiciones ya visitadas
    
    print("Iniciando exploración...")
    while True:
        mostrar_entorno(entorno, posicion)
        visitados.add(posicion)
        
        # Generar movimientos posibles (arriba, abajo, izquierda, derecha)
        movimientos = [
            (posicion[0] - 1, posicion[1]),  # Arriba
            (posicion[0] + 1, posicion[1]),  # Abajo
            (posicion[0], posicion[1] - 1),  # Izquierda
            (posicion[0], posicion[1] + 1)   # Derecha
        ]
        
        # Filtrar movimientos válidos (dentro del entorno y sin obstáculos)
        movimientos_validos = [
            (r, c) for r, c in movimientos 
            if 0 <= r < filas and 0 <= c < columnas and entorno[r][c] == 0 and (r, c) not in visitados
        ]
        
        if movimientos_validos:
            posicion = random.choice(movimientos_validos)  # Elegir un movimiento aleatorio entre los válidos
        else:
            print("No hay movimientos disponibles. Exploración terminada.")
            break
        
        time.sleep(1)

if __name__ == "__main__":
    filas, columnas = 5, 5  # Definir dimensiones del entorno
    entorno = crear_entorno(filas, columnas)
    posicion_inicial = (0, 0)  # El agente empieza en la esquina superior izquierda
    mover_agente(entorno, posicion_inicial)
