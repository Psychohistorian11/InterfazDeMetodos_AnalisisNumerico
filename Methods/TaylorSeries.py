import sympy as sp
from math import factorial
import tkinter as tk


class TaylorSeries:

    def __init__(self, root):
        window = tk.Toplevel(root)
        window.title("Método de Taylor")
        label = tk.Label(window, text="Esta es la ventana del Método de Taylor")
        label.pack(pady=10)

    def Taylor(self, f, x0, n, x):
        p = 0
        for k in range(n + 1):
            df = sp.diff(f, x, k)
            df = sp.lambdify(x, df)
            co = df(x0) * (x - x0) ** k / factorial(k)
            p = p + co

        return p
