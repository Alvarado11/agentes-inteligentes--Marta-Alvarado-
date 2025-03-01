import random
import time

def definir_entorno():
    return ["Camino", "Camino", "Obstaculo", "Camino", "Camino", "Obstaculo", "Camino"]

def mover_agente(pos, entorno):
    print("Iniciando patrullaje...")
    direccion = 1  # 1 para derecha, -1 para izquierda
    
    while True:
        if entorno[pos] == "Obstaculo":
            print(f"Obstaculo detectado en posición {pos}. Cambiando dirección.")
            direccion = random.choice([-1, 1])
        
        pos += direccion
        if pos < 0:
            pos = 0
            direccion = 1
        elif pos >= len(entorno):
            pos = len(entorno) - 1
            direccion = -1
        
        print(f"Agente en posición {pos} ({entorno[pos]})")
        time.sleep(1)

if __name__ == "__main__":
    entorno = definir_entorno()
    posicion_inicial = 0
    mover_agente(posicion_inicial, entorno)
