import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Methods.DifferentialEquations import DifferentialEquations

class DiffEquations:
    def __init__(self, root):
        self.root = root
        self.DifferentialEquations = DifferentialEquations()

        self.window = tk.Toplevel(root)
        self.window.title("Ecuaciones Diferenciales")

        tk.Label(self.window, text="Ingrese la ecuación diferencialal :").grid(row=0, column=0, padx=5, pady=5)
        self.equation = tk.Entry(self.window)
        self.equation.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Ingrese valor inicial de t (a):").grid(row=1, column=0, padx=5, pady=5)
        self.a_entry = tk.Entry(self.window)
        self.a_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Ingrese valor final de t (b):").grid(row=2, column=0, padx=5, pady=5)
        self.b_entry = tk.Entry(self.window)
        self.b_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Ingrese el punto inicial (x0):").grid(row=3, column=0, padx=5, pady=5)
        self.x0_entry = tk.Entry(self.window)
        self.x0_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Ingrese el valor de h:").grid(row=4, column=0, padx=5, pady=5)
        self.h_entry = tk.Entry(self.window)
        self.h_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Seleccione el método de solución:").grid(row=5, column=0, padx=5, pady=5)
        self.method_var = tk.StringVar(self.window)
        self.method_var.set("Euler")
        method_menu = tk.OptionMenu(self.window, self.method_var, "Euler", "Runge-Kutta")
        method_menu.grid(row=5, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(self.window, text="Calcular", command=self.solve_equation)
        self.calculate_button.grid(row=6, column=0, pady=10)

        self.compare_button = tk.Button(self.window, text="Comparar", command=self.compare_plots)
        self.compare_button.grid(row=6, column=1, pady=10)

        # Frame para contener el gráfico
        self.graph_frame = tk.Frame(self.window)
        self.graph_frame.grid(row=7, columnspan=2, padx=5, pady=5)

    def solve_equation(self):
        method = self.method_var.get()

        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        x0 = float(self.x0_entry.get())
        h = float(self.h_entry.get())

        equation_str = self.equation.get()
        f = lambda t, y: eval(equation_str)  # Convertir la ecuación a una función lambda

        if method == "Euler":
            t, yeu = self.DifferentialEquations.Euler(f, a, b, x0, h)
            self.plot_Euler(t, yeu)
        elif method == "Runge-Kutta":
            t, yrk = self.DifferentialEquations.Rk4(f, a, b, x0, h)
            self.plot_Rk4(t, yrk)

    def plot_Euler(self, t, yeu):
        # Limpiar el frame del gráfico antes de actualizarlo
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig = plt.figure(figsize=(6, 4))
        plt.plot(t, yeu, 'ro-', label='Euler')
        plt.xlabel("t")
        plt.ylabel("y")
        plt.title("Solución usando Método de Euler")
        plt.legend()

        # Integrar el gráfico en el interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def plot_Rk4(self, t, yrk):
        # Limpiar el frame del gráfico antes de actualizarlo
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig = plt.figure(figsize=(6, 4))
        plt.plot(t, yrk, 'bo-', label='Runge-Kutta')
        plt.xlabel("t")
        plt.ylabel("y")
        plt.title("Solución usando Método de Runge-Kutta")
        plt.legend()

        # Integrar el gráfico en el interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def compare_plots(self):
        method = self.method_var.get()

        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        x0 = float(self.x0_entry.get())
        h = float(self.h_entry.get())

        equation_str = self.equation.get()
        f = lambda t, y: eval(equation_str)  # Convertir la ecuación a una función lambda

        t_euler, yeu = self.DifferentialEquations.Euler(f, a, b, x0, h)
        t_Rk4, yrk = self.DifferentialEquations.Rk4(f, a, b, x0, h)

        # Limpiar el frame del gráfico antes de actualizarlo
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig = plt.figure(figsize=(6, 4))
        plt.plot(t_euler, yeu, 'ro-', label='Euler')
        plt.plot(t_Rk4, yrk, 'bo-', label='Runge-Kutta')
        plt.xlabel("t")
        plt.ylabel("y")
        plt.title("Comparación de Métodos: Euler vs Runge-Kutta")
        plt.legend()

        # Integrar el gráfico en el interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


