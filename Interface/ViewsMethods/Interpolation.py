import tkinter as tk
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Methods.InterpolationAndAdjustment import InterpolationAndAdjustment

class Interpolation:

    def __init__(self, root):
        self.x = sp.symbols('x')
        self.interpolation_methods = InterpolationAndAdjustment()

        window = tk.Toplevel(root)
        window.title("Interpolación y Ajuste")

        tk.Label(window, text="Ingrese los valores de x:").grid(row=0, column=0, padx=5, pady=5)
        self.x_data_entry = tk.Entry(window)
        self.x_data_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(window, text="Ingrese los valores de y:").grid(row=1, column=0, padx=5, pady=5)
        self.y_data_entry = tk.Entry(window)
        self.y_data_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(window, text="Ingrese dato de aproximación:").grid(row=2, column=0, padx=5, pady=5)
        self.appr_data_entry = tk.Entry(window)
        self.appr_data_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(window, text="Seleccione el método de interpolación:").grid(row=3, column=0, padx=5, pady=5)
        self.method_var = tk.StringVar(window)
        self.method_var.set("Lagrange")
        method_menu = tk.OptionMenu(window, self.method_var, "Lagrange", "Polinomial_Simple", "Minimos_cuadrados")
        method_menu.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(window, text="Interpolar", command=self.interpolate).grid(row=4, columnspan=2, pady=10)

        self.plot_frame = tk.Frame(window)
        self.plot_frame.grid(row=5, columnspan=2, pady=10)

        self.result_label = tk.Label(window, text="")
        self.result_label.grid(row=6, columnspan=2, pady=5)

    def interpolate(self):
        x_data = np.array(list(map(float, self.x_data_entry.get().split(','))))
        y_data = np.array(list(map(float, self.y_data_entry.get().split(','))))
        method = self.method_var.get()

        if method == "Lagrange":
            result = self.interpolation_methods.Lagrange(self.x, x_data, y_data)
            return self.plot_lagrange(x_data, y_data, result)
        elif method == "Polinomial_Simple":
            result = self.interpolation_methods.Pol_simple2(x_data, y_data)
            return self.plot_polinomial_simple(x_data, y_data, result)
        elif method == "Minimos_cuadrados":
            b, m = self.interpolation_methods.Minimos_cuadrados(x_data, y_data)
            return self.plot_minimos_cuadrados(x_data, y_data, b, m)

    def plot_minimos_cuadrados(self, x_data, y_data, b, m):
        fig, ax = plt.subplots()
        ux = np.linspace(min(x_data), max(x_data), 1000)
        p = lambda x: b + m * x

        ax.plot(ux, p(ux), label="Ajuste por mínimos cuadrados")
        ax.plot(x_data, y_data, "ok", label="Observados")
        ax.plot(x_data, p(x_data), "ro", label="Obtenidos")
        ax.legend()

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Mostrar el polinomio y el valor aproximado
        poly_str = f"{b:.2f} + {m:.2f}x"
        appr_data = float(self.appr_data_entry.get())
        approx_value = p(appr_data)
        result_text = f"Polinomio: {poly_str}\nValor aproximado en {appr_data}: {approx_value:.2f}"
        self.result_label.config(text=result_text)

    def plot_polinomial_simple(self, x_data, y_data, coefficients):
        fig, ax = plt.subplots()
        ux = np.linspace(min(x_data), max(x_data), 1000)

        ax.plot(x_data, y_data, "p", label="Observados")
        ax.plot(ux, self.interpolation_methods.Poly(coefficients, ux), label="Polinomio simple")
        ax.legend()

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Crear la representación legible del polinomio
        poly_terms = [f"{coeff:.2f}x^{i}" if i > 0 else f"{coeff:.2f}" for i, coeff in enumerate(coefficients)]
        poly_str = " + ".join(poly_terms)
        poly_str = poly_str.replace("+ -", "- ")

        # Evaluar el polinomio en el punto de aproximación
        appr_data = float(self.appr_data_entry.get())
        approx_value = self.interpolation_methods.Poly(coefficients, appr_data)
        result_text = f"Polinomio: {poly_str}\nValor aproximado en {appr_data}: {approx_value:.2f}"
        self.result_label.config(text=result_text)

    def plot_lagrange(self, x_data, y_data, result):
        fig, ax = plt.subplots()
        P_x = sp.lambdify(self.x, result)
        ux = np.linspace(min(x_data), max(x_data), 1000)

        ax.plot(x_data, y_data, "pm", label="Observados")
        ax.plot(ux, P_x(ux), label="Lagrange")

        ax.legend()

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Crear la representación legible del polinomio
        poly_str = str(result)
        poly_str = poly_str.replace("**", "^")
        poly_str = poly_str.replace("*", "")

        # Evaluar el polinomio en el punto de aproximación
        appr_data = float(self.appr_data_entry.get())
        approx_value = P_x(appr_data)
        result_text = f"Polinomio: {poly_str}\nValor aproximado en {appr_data}: {approx_value:.2f}"
        self.result_label.config(text=result_text)


