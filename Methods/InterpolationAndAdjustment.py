import time
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import tkinter as tk


class InterpolationAndAdjustment:

    def Minimos_cuadrados(self, xd, yd):
        m = len(xd)
        sx = sum(xd)
        sf = sum(yd)
        sx2 = sum(xd ** 2)
        sfx = sum(xd * yd)
        a0 = (sf * sx2 - sx * sfx) / (m * sx2 - (sx) ** 2)
        a1 = (m * sfx - sx * sf) / (m * sx2 - (sx) ** 2)
        return a0, a1

    def Polinomial_Simple(self, x_data, y_data):
        n = len(x_data)
        x0 = np.zeros(n)
        M_p = np.zeros([n, n])
        for i in range(n):
            M_p[i, 0] = 1
            for j in range(1, n):
                M_p[i, j] = M_p[i, j - 1] * x_data[i]
        a_i = self.Gauss_Seidel_(M_p, y_data, x0, 1e-6)

        return a_i

    def Gauss_Seidel_(self, A, b, x0, tol):

        D = np.diag((np.diag(A)))
        L = D - np.tril(A)
        U = D - np.triu(A)
        Tg = np.dot(np.linalg.inv(D - L), U)
        total_start_time = time.time()
        Cg = np.dot(np.linalg.inv(D - L), b)
        lam, vec = np.linalg.eig(Tg)
        radio = max(abs(lam))

        if radio < 1:
            contador = 0
            x1 = np.dot(Tg, x0) + Cg

            while (max(np.abs(x1 - x0))) > tol:
                x0 = x1
                x1 = np.dot(Tg, x0) + Cg
                contador += 1

            total_end_time = time.time()
            total_iteration_time = total_end_time - total_start_time
            return x1

    def Poly(self, a_i, ux):
        P = 0
        for i in range(len(a_i)):
            P = P + a_i[i] * ux ** i
        return P

    def Lagrange(self, x, xd, yd):
        n = len(xd)
        P = 0
        for i in range(n):
            L = 1
            for j in range(n):
                if (j != i):
                    L = L * ((x - xd[j]) / (xd[i] - xd[j]))

            P = P + L * yd[i]
        poly = sp.expand(P)
        return poly

    def escala(self, x_a, y_p):
        plt.figure(figsize=(10, 10), dpi=80)
        plt.subplot(331)
        plt.plot(x_a, y_p, 'om', label='Datos Observados')
        plt.legend()
        plt.subplot(332)
        plt.plot(x_a ** 2, y_p, 'og', label=r'$x^2$')
        plt.legend()
        plt.subplot(333)
        plt.plot(x_a ** 3, y_p, 'or', label=r'$x^3$')
        plt.legend()
        plt.subplot(334)
        plt.plot(x_a, np.sqrt(y_p), 'ok', label=r'$\sqrt{y}$')
        plt.legend()
        plt.subplot(335)
        plt.plot(x_a, 1 / np.sqrt(y_p), 'og', label=r'$\frac{1}{\sqrt{x}}$')
        plt.legend()
        plt.subplot(336)
        plt.plot(x_a, y_p ** 2, 'ob', label=r'$y^2$')
        plt.legend()
        plt.subplot(337)
        plt.plot(np.log(x_a), np.log(y_p), 'oc', label=r'$log(x), log(y)$')
        plt.legend()
        plt.subplot(338)
        plt.plot(np.log(x_a), y_p, 'om', label=r'$\log{x}$')
        plt.legend()
        plt.subplot(339)
        plt.plot(x_a, np.log(y_p), 'ob', label=r'$\log{y}$')
        plt.legend()
        return
