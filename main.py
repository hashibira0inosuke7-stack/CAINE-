import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import platform
import sys
import os

# 👉 keyboard solo en Windows
if platform.system() == "Windows":
    import keyboard

# -------- FIX RUTAS PARA EXE --------
def ruta_archivo(nombre):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nombre)
    return nombre

ventana_anterior = ""
tiempo_ultimo_cambio = time.time()

# -------- FRASES --------
frases = {
    "inicio": ["¡BIENVENIDO AL INCREÍBLE CIRCO DIGITAL! 🎪"],
    "entretenido": ["Hmm… interesante 🍿","No puedes parar de ver eso 😏"],
    "dibujo": ["¡Arte en proceso! 🎨","Me gusta tu estilo"],
    "juego": ["Ohhh… esto me interesa 🎮"],
    "general": ["Curioso… 😏"],
    "aburrido": ["Esto es aburrido…","Haz algo interesante…"],
    "enojado": ["¡YA BASTA! 😡"]
}

# -------- IMÁGENES (TUS NOMBRES) --------
imagenes = {
    "inicio": ["caine_inicio.png"],
    "feliz": ["caine_feliz1.png", "caine_feliz2.png", "caine_feliz3.png"],
    "enojado": ["caine_enojado1.png", "caine_enojado2.png", "caine_enojado3.png"],
    "dibujo": ["caine_dibujo1.png", "caine_dibujo2.png", "caine_dibujo3.png"],
    "interesado": ["caine_interesado1.png", "caine_interesado2.png", "caine_interesado3.png"],
    "entretenido": ["caine_entretenido1.png"],
    "aburrido": ["caine_aburrido1.png", "caine_aburrido2.png", "caine_aburrido3.png"],
    "dormido": ["caine_dormido.png"],
    "asustado": ["caine_asustado.png"]
}

# -------- DETECTAR VENTANA --------
def obtener_ventana():
    if platform.system() == "Windows":
        try:
            import pygetwindow as gw
            w = gw.getActiveWindow()
            return w.title.lower() if w else ""
        except:
            return ""
    return ""

# -------- MOSTRAR CAINE --------
def mostrar_caine(texto, tipo):
    ventana = tk.Tk()
    ventana.overrideredirect(True)
    ventana.attributes("-topmost", True)

    img_path = ruta_archivo(random.choice(imagenes[tipo]))
    img = Image.open(img_path).resize((250, 250))
    img = ImageTk.PhotoImage(img)

    label = tk.Label(ventana, image=img)
    label.image = img
    label.pack()

    tk.Label(ventana, text=texto).pack()

    ventana.bind("<Button-1>", lambda e: apagar())

    ventana.geometry(f"300x300+{random.randint(0,800)}+{random.randint(0,500)}")

    ventana.after(7000, ventana.destroy)
    ventana.mainloop()

# -------- REACCIÓN --------
def reaccionar(nombre):
    if "youtube" in nombre:
        return random.choice(frases["entretenido"]), "entretenido"
    elif "chrome" in nombre:
        return random.choice(frases["entretenido"]), "entretenido"
    elif "paint" in nombre:
        return random.choice(frases["dibujo"]), "dibujo"
    elif "game" in nombre:
        return random.choice(frases["juego"]), "interesado"
    else:
        return random.choice(frases["general"]), "feliz"

# -------- APAGAR --------
def apagar():
    mostrar_caine("...", "asustado")
    time.sleep(1)
    sys.exit()

# -------- INICIO --------
def mostrar_inicio():
    mostrar_caine(frases["inicio"][0], "inicio")

# -------- MONITOR --------
def monitor():
    global ventana_anterior, tiempo_ultimo_cambio

    mostrar_inicio()

    while True:

        # 👉 ESC + 1 en Windows
        if platform.system() == "Windows":
            try:
                if keyboard.is_pressed("esc") and keyboard.is_pressed("1"):
                    apagar()
            except:
                pass

        ventana_actual = obtener_ventana()

        if ventana_actual and ventana_actual != ventana_anterior:
            texto, tipo = reaccionar(ventana_actual)
            mostrar_caine(texto, tipo)

            ventana_anterior = ventana_actual
            tiempo_ultimo_cambio = time.time()

        if time.time() - tiempo_ultimo_cambio > 60:
            mostrar_caine(random.choice(frases["aburrido"]), "aburrido")
            tiempo_ultimo_cambio = time.time()

        time.sleep(1)

# -------- START --------
monitor()