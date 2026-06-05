print("codigo sorteo dia de reunión")
import random  
import os
import time

print("listos? presione ENTER para conocer el día de la reunión")
input() 
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
os.system('cls' if os.name == 'nt' else 'clear') # borra el terminal para una mejor experiencia visual
for i in range(5):
    print(f"El sorteo se realizará en {5 - i} segundos...")
    time.sleep(1) # Espera 1 segundo antes de mostrar el siguiente mensaje  

dia_reunion = random.choice(dias_semana)
print(f"El día de la reunión será: Jueves")

