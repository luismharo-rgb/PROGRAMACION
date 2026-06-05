import random
import time
import os

# Definimos códigos de colores
VERDE = "\033[0;32m"
BLANCO_SOBRE_AZUL = "\033[1;37;44m"
RESET = "\033[0m"
ERRORES = "\033[0;31m"

os.system('cls' if os.name == 'nt' else 'clear') # borra el terminal para una mejor experiencia visual
print(f"{BLANCO_SOBRE_AZUL} .__________CARRERA DE AUTOS__________. {RESET}")
print(" ")
print(f"{VERDE}¡Bienvenido a la carrera de autos!{RESET}")
# 1. Configuración inicial
cantidad_autos = int(input(f" {VERDE}¿Cuántos autos correrán? {RESET}").strip())
lista_autos = [] # Nombres de los autos, serán "auto 1", "auto 2", etc.
posiciones = [] # Metros recorridos por cada auto
# aqui se crean los nombres de los autos y 
#se inicializan sus posiciones
for i in range(1, cantidad_autos + 1): 
    lista_autos.append(f"Auto {i}")
    posiciones.append(0) # Todos empiezan en 0 km

# Inicio de la carrera
vueltas = 10
print("\n¡Arrancan!")

for vuelta in range(1, vueltas + 1): #
    time.sleep(1) # El delay es para simular el tiempo de cada vuelta
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f"\n--- Vuelta {vuelta} / {vueltas}  ---") # nos indica en que vuelta va
    
    for i in range(len(lista_autos)): # este for es para cada auto, le asigna un avance aleatorio entre 1 y 10 kilometros
        avance = random.randint(1, 10) # Número aleatorio de avance
        posiciones[i] += avance #
        print(f"{VERDE}{lista_autos[i]} ha avanzado a: {BLANCO_SOBRE_AZUL}{posiciones[i]}km{RESET}") # imprime avance de los autos
      
# Resultado final de la carrera
print("\n--- ¡FIN DE LA CARRERA! ---")
print(f"{VERDE}Resultados finales:{RESET}")
# Encuentra todos los autos que alcanzaron la distancia ganadora
distancia_maxima = max(posiciones)
lista_ganadores = []
for i in range(len(posiciones)):
    if posiciones[i] == distancia_maxima:
        lista_ganadores.append(lista_autos[i])

if len(lista_ganadores) == 1:
    print(f"{VERDE}¡GANADOR🚗💨{BLANCO_SOBRE_AZUL}{lista_ganadores[0]}{VERDE}con {ERRORES}{max(posiciones)}{VERDE}km recorridos!{RESET}")
else:print(f"{ERRORES}¡Empate:{BLANCO_SOBRE_AZUL}{'🚗💨'.join(lista_ganadores)}{VERDE}con {ERRORES}{max(posiciones)}{VERDE}km recorridos!{RESET}")  
