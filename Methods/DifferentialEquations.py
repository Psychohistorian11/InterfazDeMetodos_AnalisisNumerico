import numpy as np
import tkinter as tk

class DifferentialEquations:

    def Euler(self, f, a, b, co, h):
        n = int((b - a) / h)
        t = np.linspace(a, b, n + 1)
        yeu = [co]
        for i in range(n):
            yeu.append(yeu[i] + h * f(t[i], yeu[i]))
        return t, yeu

    def Rk4(self, f, a, b, h, c0):
        yr = [c0]
        n = int((b - a) / h)
        t = np.linspace(a, b, n + 1)
        for i in range(n):
            k1 = h * f(t[i], yr[i])
            k2 = h * f(t[i] + h / 2, yr[i] + 1 / 2 * k1)
            k3 = h * f(t[i] + h / 2, yr[i] + 1 / 2 * k2)
            k4 = h * f(t[i] + h / 2, yr[i] + 1 / 2 * k3)
            yr.append(yr[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
        return yr, t
