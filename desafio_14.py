import string
print(".__________CUENTA PALABRAS__________.")
print(" ")
# ingresamos una frase
frase=input ("Ingrese una frase: ")
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
print(f"\nLa cantidad de palabras en la frase es: {cantidad_palabras}")
print("Las palabras son:")
for palabra in palabras:
    print(f"- {palabra}")
input("\nPresione Enter para continuar...")

