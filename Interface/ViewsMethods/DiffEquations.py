import tkinter as tk

class DiffEquations:

    def __init__(self, root):
        window = tk.Toplevel(root)
        window.title("Ecuaciones Diferenciales")
        label = tk.Label(window, text="Esta es la ventana de Ecuaciones Diferenciales")
        label.pack(pady=10)