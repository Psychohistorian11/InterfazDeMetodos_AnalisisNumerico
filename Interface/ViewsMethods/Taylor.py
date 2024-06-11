import tkinter as tk

class Taylor:

    def __init__(self, root):
        window = tk.Toplevel(root)
        window.title("Método de Taylor ")
        label = tk.Label(window, text="Esta es la ventana de Método de Taylor ")
        label.pack(pady=10)