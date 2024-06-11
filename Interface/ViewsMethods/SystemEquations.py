import tkinter as tk

class SystemEquations:

    def __init__(self, root):
        window = tk.Toplevel(root)
        window.title("Sistema de Ecuacioenes Lineales")
        label = tk.Label(window, text="Esta es la ventana de Sistema de Ecuacioenes Lineales")
        label.pack(pady=10)