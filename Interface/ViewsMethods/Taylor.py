import tkinter as tk
from tkinter import messagebox
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Methods.TaylorSeries import TaylorSeries


class Taylor:

    def __init__(self, root):
        self.root = root
        self.x = sp.symbols('x')
        self.taylorSeries = TaylorSeries()

        window = tk.Toplevel(root)
        window.title("Método de Taylor")

        tk.Label(window, text="Ingrese el polinomio:").grid(row=1, column=0, padx=5, pady=5)
        self.polynomial_entry = tk.Entry(window)
        self.polynomial_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="Ingrese el grado del polinomio:").grid(row=2, column=0, padx=5, pady=5)
        self.degree_entry = tk.Entry(window)
        self.degree_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(window, text="Ingrese el punto inicial (x0):").grid(row=3, column=0, padx=5, pady=5)
        self.x0_entry = tk.Entry(window)
        self.x0_entry.grid(row=3, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(window, text="Calcular", command=self.calculate_taylor)
        self.calculate_button.grid(row=4, columnspan=2, pady=10)

        self.calculate_cota_button = tk.Button(window, text="Calcular Cota", command=self.show_cota_input, state=tk.DISABLED)
        self.calculate_cota_button.grid(row=5, column=0, padx=5, pady=5)

        self.calculate_multiple_button = tk.Button(window, text="Calcular Múltiples Polinomios", command=self.show_multiple_input, state=tk.DISABLED)
        self.calculate_multiple_button.grid(row=5, column=1, padx=5, pady=5)

        self.plot_frame = tk.Frame(window)
        self.plot_frame.grid(row=6, columnspan=2, pady=10, padx=10)

        self.result_label = tk.Label(window, text="")
        self.result_label.grid(row=7, columnspan=2, pady=5)

        self.cota_label = tk.Label(window, text="Ingrese el valor de x para la cota:")
        self.cota_entry = tk.Entry(window)
        self.cota_result_label = tk.Label(window, text="")
        self.cota_button = tk.Button(window, text="Calcular Cota", command=self.calculate_cota)

        self.multiple_label = tk.Label(window, text="Ingrese la lista de grados para múltiples polinomios:")
        self.multiple_entry = tk.Entry(window)
        self.multiple_result_label = tk.Label(window, text="")
        self.multiple_button = tk.Button(window, text="Calcular Múltiples Polinomios", command=self.calculate_multiple)

    def calculate_taylor(self):
        polynomial_str = self.polynomial_entry.get()
        degree_str = self.degree_entry.get()
        x0_str = self.x0_entry.get()

        if not polynomial_str or not degree_str or not x0_str:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            polynomial = sp.sympify(polynomial_str)
            degree = int(degree_str)
            x0 = float(sp.N(sp.sympify(x0_str)))  # Convierte usando SymPy
        except Exception as e:
            messagebox.showerror("Error", f"Error en la entrada: {e}")
            return

        self.taylor_poly = self.taylorSeries.taylor(polynomial, x0, degree)
        self.plot_taylor(polynomial, self.taylor_poly, x0)
        self.result_label.config(text=f"Polinomio de Taylor: {self.taylor_poly}")

        self.calculate_cota_button.config(state=tk.NORMAL)
        self.calculate_multiple_button.config(state=tk.NORMAL)

    def plot_taylor(self, original_func, taylor_poly, x0):
        fig, ax = plt.subplots()

        p = sp.lambdify(self.x, taylor_poly)
        w = np.linspace(x0 - 1, x0 + 1, 1000)

        ax.plot(w, p(w), 'r--', label=f'Polinomio de Taylor (grado {self.degree_entry.get()})')

        original_func_lambdified = sp.lambdify(self.x, original_func)
        ax.plot(w, original_func_lambdified(w), label='Función Original')

        # Graficar el punto inicial
        ax.plot([x0], [original_func_lambdified(x0)], 'bo', label=f'Punto inicial (x0={x0})')

        ax.legend()

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def show_cota_input(self):
        self.cota_label.grid(row=8, column=0, padx=5, pady=5)
        self.cota_entry.grid(row=8, column=1, padx=5, pady=5)
        self.cota_button.grid(row=9, columnspan=2, pady=5)
        self.cota_result_label.grid(row=10, columnspan=2, pady=5)

    def show_multiple_input(self):
        self.multiple_label.grid(row=8, column=0, padx=5, pady=5)
        self.multiple_entry.grid(row=8, column=1, padx=5, pady=5)
        self.multiple_button.grid(row=9, columnspan=2, pady=5)
        self.multiple_result_label.grid(row=10, columnspan=2, pady=5)

    def calculate_cota(self):
        try:
            x_val = float(sp.N(sp.sympify(self.cota_entry.get())))  # Convierte usando SymPy
            polynomial_str = self.polynomial_entry.get()
            degree_str = self.degree_entry.get()
            x0_str = self.x0_entry.get()
            polynomial = sp.sympify(polynomial_str)
            degree = int(degree_str)
            x0 = float(sp.N(sp.sympify(x0_str)))  # Convierte usando SymPy
            cota_value = self.taylorSeries.cota(polynomial, x_val, x0, degree)
            self.cota_result_label.config(text=f"Cota: {cota_value}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en la entrada: {e}")

    def calculate_multiple(self):
        try:
            degrees_str = self.multiple_entry.get()
            degree_list = [int(deg.strip()) for deg in degrees_str.split(',')]

            polynomial_str = self.polynomial_entry.get()
            x0_str = self.x0_entry.get()
            polynomial = sp.sympify(polynomial_str)
            x0 = float(sp.N(sp.sympify(x0_str)))  # Convierte usando SymPy

            fig, ax = plt.subplots()

            original_func_lambdified = sp.lambdify(self.x, polynomial)
            w = np.linspace(x0 - 1, x0 + 1, 1000)

            ax.plot(w, original_func_lambdified(w), label='Función Original')

            for i, degree in enumerate(degree_list):
                taylor_poly = self.taylorSeries.taylor(polynomial, x0, degree)
                p = sp.lambdify(self.x, taylor_poly)
                ax.plot(w, p(w), linestyle='--', label=f'Polinomio Taylor (grado {degree})')

            ax.plot([x0], [original_func_lambdified(x0)], 'bo', label=f'Punto inicial (x0={x0})')
            ax.legend()

            for widget in self.plot_frame.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except Exception as e:
            messagebox.showerror("Error", f"Error en la entrada: {e}")

