import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        contours = find_contours(image)
        display_image(image, contours)


def find_contours(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def display_image(image, contours):
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    panel.configure(image=image)
    panel.image = image


# Crear la ventana principal
root = tk.Tk()
root.title("Seleccionar imagen y encontrar contornos")

# Crear un botón para seleccionar imagen
select_button = tk.Button(root, text="Seleccionar imagen", command=select_image)
select_button.pack(pady=10)

# Crear un panel para mostrar la imagen
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Ejecutar la interfaz de usuario
root.mainloop()
