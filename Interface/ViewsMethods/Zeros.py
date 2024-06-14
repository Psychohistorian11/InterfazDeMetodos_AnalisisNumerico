import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Methods.ZerosOfFunctions import ZerosOfFunctions
import ast


class Zeros:

    def __init__(self, root):
        self.root = root
        self.x = sp.symbols("x")
        self.zerosFunctions = ZerosOfFunctions()
        self.text = ""

        window = tk.Toplevel(root)
        window.title("Ceros de funciones")
        tk.Label(window, text="Ingrese la función (use x como variable): ").grid(row=1, column=0, padx=5, pady=5)
        self.function_entry = tk.Entry(window)
        self.function_entry.insert(0,
                                   "x+2")
        self.function_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="Ingrese el intervalo[a,b] o valor inicial [a]:").grid(row=2, column=0, padx=5, pady=5)
        self.interval_entry = tk.Entry(window)
        self.interval_entry.insert(0, "[ ]")
        self.interval_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(window, text="Ingrese la tolerancia:").grid(row=3, column=0, padx=5, pady=5)
        self.tolerance_entry = tk.Entry(window)
        self.tolerance_entry.insert(0, "1e-6")
        self.tolerance_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(window, text="Seleccione el método para encontrar la raíz:").grid(row=4, column=0, padx=5, pady=5)
        self.method_var = tk.StringVar(window)
        self.method_var.set("Bisección")
        method_menu = tk.OptionMenu(window, self.method_var, "Bisección", "Falsa Posición", "Newton", "Secante")
        method_menu.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(window, text="Calcular raíz", command=self.calculate_root).grid(row=5, column=0, columnspan=2, pady=5)

        tk.Label(window, text="Raiz :").grid(row=6, column=0, padx=5, pady=5)
        self.root_label = tk.Label(window, text="")
        self.root_label.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(window, text="Iteraciones :").grid(row=7, column=0, padx=5, pady=5)
        self.i_label = tk.Label(window, text="")
        self.i_label.grid(row=7, column=1, padx=5, pady=5)

        # Crear el área de gráficos
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, window)
        self.canvas.get_tk_widget().grid(row=8, column=0, columnspan=2, pady=5)

    def calculate_root(self):
        try:
            function_s = sp.sympify(self.function_entry.get())
            function = sp.lambdify(self.x, function_s)
            try:
                interval = list(ast.literal_eval(self.interval_entry.get()))
                if not isinstance(interval, list):
                    raise Exception("El intervalo ingresado debe ser una lista válida de Python")
                for value in interval:
                    float(value)
            except(ValueError, SyntaxError):
                raise Exception(
                    "El intervalo ingresado debe contener solo números y estar en formato de lista válido de Python")

            method = self.method_var.get()
            tolerance = float(self.tolerance_entry.get())
            if tolerance <= 0:
                raise Exception("La tolerancia debe ser mayor que 0")
            elif tolerance < 1e-10:
                raise Exception("La tolerancia debe ser mayor que 1e-10")
            if len(interval) > 1:
                start = float(interval[0])
                end = float(interval[1])
                if start >= end:
                    raise Exception("El valor de inicio debe ser menor que el valor final")
                if method == "Bisección":
                    root, counter = self.zerosFunctions.bisection(function, start, end, tolerance)
                elif method == "Falsa Posición":
                    root, counter = self.zerosFunctions.positionFalse(function, start, end, tolerance)
                elif method == "Secante":
                    root, counter = self.zerosFunctions.secante(function, start, end, tolerance)
                else:
                    raise Exception("Método no reconocido para un intervalo cerrado [a, b]")
            elif len(interval) == 1:
                start = float(interval[0])
                end = start + 1  # Asignar un valor a end para el método de Newton
                if method == "Newton":
                    root, counter = self.zerosFunctions.newton(function_s, start, tolerance)
                else:
                    raise Exception("Método no reconocido para un valor inicial [a]")
            else:
                raise Exception("Debe ingresar un intervalo válido [a] o [a, b]")
            self.root_label.config(text=str(root))
            self.i_label.config(text=str(counter))
            self.ax.clear()
            x_vals = np.linspace(start, end, 400)
            y_vals = function(x_vals)
            self.ax.plot(x_vals, y_vals, label='Función')
            self.ax.axhline(0, color='black', linewidth=0.5)
            self.ax.scatter(root, function(root), color='red', zorder=5, label='Raíz')
            self.ax.legend()
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", str(e))