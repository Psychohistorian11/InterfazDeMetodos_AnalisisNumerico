import sympy as sp
from math import factorial
import tkinter as tk
import numpy as np


class TaylorSeries:

    def taylor(self, f, x0, n, x=sp.symbols("x")):
        p = 0
        for k in range(n + 1):
            df = sp.diff(f, x, k)
            df = sp.lambdify(x, df)
            co = df(x0) * (x - x0) ** k / factorial(k)
            p = p + co

        return p

    def cota(self, f, px, x0, n, x=sp.symbols("x")):
        M = max(x0, px)
        m = min(x0, px)
        w = np.linspace(m, M, 1000)
        dfn = sp.lambdify(x, sp.diff(f, x, n + 1))
        ma = np.max(np.abs(dfn(w)))
        c = ma * (px - x0) ** (n + 1) / factorial(n + 1)
        return c
