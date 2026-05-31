# Este codigo fue desde gemini
import tkinter as tk
from tkinter import messagebox

# Definimos la lógica de conversión
def convertir_grados():
    try:
        # 1. Obtenemos el valor de la casilla
        celsius = float(entrada_celsius.get())
        
        # 2. Aplicamos la fórmula
        fahrenheit = (celsius * 9/5) + 32
        
        # 3. Actualizamos la etiqueta con el resultado
        lbl_resultado.config(text=f"{celsius}°C son {fahrenheit:.2f}°F")
        
    except ValueError:
        messagebox.showwarning("Dato inválido", "Por favor, ingresa solo números.")

# --- Configuración de la interfaz ---
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("350x200")

tk.Label(ventana, text="Ingresa grados Celsius:").pack(pady=10)

# Casilla de entrada
entrada_celsius = tk.Entry(ventana)
entrada_celsius.pack()

# El botón "llama" a la función cuando se hace clic
btn_convertir = tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_grados)
btn_convertir.pack(pady=20)

# Etiqueta donde aparecerá el resultado
lbl_resultado = tk.Label(ventana, text="Resultado: -", font=("Arial", 12, "bold"))
lbl_resultado.pack()

ventana.mainloop()