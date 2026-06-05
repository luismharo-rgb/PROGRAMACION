import string
# Definimos códigos de colores
VERDE = "\033[0;32m"
BLANCO_SOBRE_AZUL = "\033[1;37;44m"
RESET = "\033[0m"
ERRORES = "\033[0;31m"
print(f"{BLANCO_SOBRE_AZUL} .__________CUENTA PALABRAS__________. {RESET}")
print(" ")
print(f"{VERDE}Ingrese una frase: {RESET}")
# ingresamos una frase
frase=input().strip() # usamos strip() para eliminar espacios al inicio y al final de la frase, esto ayuda a evitar contar palabras vacías si el usuario ingresa espacios adicionales.
# verificamos si la frase está vacía después de eliminar los espacios, si es así, mostramos un mensaje y salimos del programa.
if not frase:
    print(f"{ERRORES}No se ingresó ninguna frase. Por favor, intente nuevamente.{RESET}")
    exit()
# si la frase no está vacía, procedemos a limpiar el texto y contar las palabras.    
else:
    # usamos str.maketrans para crear una tabla de traducción que elimine la puntuación y los signos de interrogación/exclamación
    tabla = str.maketrans("", "", string.punctuation + "¿¡")
    # string.punctuation incluye todos los signos de puntuación comunes, y añadimos "¿¡" 
    # para eliminar también esos caracteres, en español estos son comunes al inicio de preguntas y exclamaciones.
    texto_limpio = frase.translate(tabla)
    # translate() reemplaza cada carácter en la cadena según la tabla de traducción,
    # eliminando así la puntuación y los signos de interrogación/exclamación.
    # split() sin parámetros maneja \n, \t y múltiples espacios automáticamente
    # esto corregido conforme a la ultima evaluación de corrección de IA.
    palabras = texto_limpio.split()
    # luego palabras es una lista de las palabras en el texto limpio, y cantidad_palabras 
    # es el número total de palabras.
    cantidad_palabras = len(palabras)
    # finalmente, mostramos el resultado al usuario. Si no se encontraron palabras, 
    # indicamos que no se encontraron palabras en la frase ingresada.
    if cantidad_palabras == 0:
        print(f"{ERRORES}No se encontraron palabras en la frase ingresada.{RESET}")
    else:
        print(f"{VERDE}\nLa cantidad de palabras en la frase es: {cantidad_palabras}{RESET}")
        print(f"{VERDE}Las palabras son:{RESET}")
        for palabra in palabras:
            print(f"{VERDE}- {palabra}{RESET}")
        input(f"\n{VERDE}Presione Enter para continuar...{RESET}")

