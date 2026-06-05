import os

# Limpiamos la pantalla al iniciar (compatible con Mac y Windows)
os.system('cls' if os.name == 'nt' else 'clear')

print("=== Cálculo de Promedio de Notas ===")

notas = []

while True:
    try:
        nota = int(input("\nIngrese una nota (1-12) o 0 para terminar: "))
        
        if nota == 0:
            break
            
        if nota < 1 or nota > 12:
            print("Error: La nota debe estar entre 1 y 12.")
            continue

        notas.append(nota)
    except ValueError:
        print("Error: Debes ingresar un número entero.")

# Verificamos si la lista tiene datos para evitar la división por cero
if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    estado = "APROBADO" if promedio >= 6 else "REPROBADO"
    
    print(f"\nEl promedio es: {promedio:.2f}")
    print(f"El estudiante ha quedado: {estado}")
else:
    print("\nNo se ingresaron notas. Saliendo del programa...")

print("\nGracias por usar el programa.")