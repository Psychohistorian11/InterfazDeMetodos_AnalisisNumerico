import tkinter as tk
from tkinter import messagebox
import numpy as np

class SystemEquations:

    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("Sistema de Ecuaciones Lineales")

        tk.Label(self.window, text="Ingrese el número de filas:").grid(row=0, column=0, padx=5, pady=5)
        self.rows_entry = tk.Entry(self.window)
        self.rows_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Ingrese el número de columnas:").grid(row=1, column=0, padx=5, pady=5)
        self.cols_entry = tk.Entry(self.window)
        self.cols_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.window, text="Crear Sistema", command=self.create_system)
        self.submit_button.grid(row=2, columnspan=2, pady=10)

        self.system_frame = tk.Frame(self.window)
        self.system_frame.grid(row=3, columnspan=2, pady=10, padx=10)

    def create_system(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")
            return

        if rows != cols:
            messagebox.showwarning("Advertencia", "Para crear un sistema de ecuaciones, se necesita una matriz cuadrada.")
            return

        # Limpiar el frame del sistema de ecuaciones antes de agregar los nuevos widgets
        for widget in self.system_frame.winfo_children():
            widget.destroy()

        self.entries = []
        for i in range(rows):
            row_entries = []

            # Etiquetas x1, x2, x3, ...
            for j in range(cols):
                entry = tk.Entry(self.system_frame, width=5)
                entry.grid(row=i, column=2*j, padx=5, pady=5)
                row_entries.append(entry)
                label = tk.Label(self.system_frame, text=f"x{j+1}")
                label.grid(row=i, column=2*j+1, padx=5, pady=5, sticky="w")

            # Igualdad y término independiente
            tk.Label(self.system_frame, text="=").grid(row=i, column=2*cols, padx=5, pady=5, sticky="e")
            result_entry = tk.Entry(self.system_frame, width=5)
            result_entry.grid(row=i, column=2*cols+1, padx=5, pady=5)
            row_entries.append(result_entry)
            self.entries.append(row_entries)

        self.solve_button = tk.Button(self.system_frame, text="Resolver", command=self.solve_system)
        self.solve_button.grid(row=rows + 1, columnspan=2*cols+1, pady=10)

    def solve_system(self):
        try:
            A = []
            b = []
            for row_entries in self.entries:
                row = [float(entry.get()) for entry in row_entries[:-1]]  # Coeficientes
                A.append(row)
                b.append(float(row_entries[-1].get()))  # Término independiente
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todas las casillas.")
            return

        print(A)
        print(b)

