import sympy as sp
import tkinter as tk


class ZerosOfFunctions:

    def bisection(self, f, a, b, tol):
        global c
        if f(a) * f(b) > 0:
            print(f"la función no cumple el teorema en: {a, b}")
        else:
            i = 0
            while abs(b - a) > tol:
                c = (a + b) / 2
                if f(a) * f(c) < 0:
                    b = c
                else:
                    a = c
                i += 1
            return c, i

    def positionFalse(self, f, a, b, tol):
        if f(a) * f(b) > 0:
            print(f"la función no cumple el teorema en: {a, b}")
        else:
            i = 0
            c = a - f(a) * (a - b) / (f(a) - f(b))
            while abs(f(c)) > tol:
                c = a - f(a) * (a - b) / (f(a) - f(b))
                if f(a) * f(c) < 0:
                    b = c
                else:
                    a = c
                i += 1
            return c, i

    def newton(self, f, x0, tol, variable=None):
        if not variable:
            variable = sp.symbols('x')

        df = sp.diff(f, variable)
        xv = [x0]

        next_x = sp.lambdify(variable, variable - f / df)
        counter = 0
        while True:
            xv.append(next_x(xv[-1]))
            counter += 1
            if abs(xv[-1] - xv[-2]) < tol:
                break
        return xv[-1], counter

    def secante(self, f, x0, x1, tol):
        global xnext
        Error = abs(x1 - x0)
        counter = 0
        while Error > tol:
            xnext = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))
            Error = abs(xnext - x0)
            x0 = x1
            x1 = xnext
            counter += 1
        return xnext, counter
