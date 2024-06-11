import numpy as np
import time
import tkinter as tk


class SystemOfLinearEquations:

    def __init__(self, root):
        window = tk.Toplevel(root)
        window.title("Sistemas de Ecuaciones Lineales")
        label = tk.Label(window, text="Esta es la ventana de Sistemas de Ecuaciones Lineales")
        label.pack(pady=10)

    def Gauss_Seidel_(self, A, b, x0, tol):

        global error
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
                error = max(np.abs(x1 - x0))

            total_end_time = time.time()
            total_iteration_time = total_end_time - total_start_time
            return x1, Tg, Cg, radio, error, total_iteration_time

        else:
            print("El sistema no converge")

    def Gauss_Sumas(self, A, b, x0, tol):
        global error
        n = len(b)
        x1 = np.zeros(n)
        M = 50
        norm = 2
        cont = 0

        start = time.time()

        while norm > tol and cont < M:
            for i in range(n):
                aux = 0
                for j in range(n):
                    if (i != j):
                        aux = aux - A[i, j] * x0[j]
                x1[i] = (b[i] + aux) / A[i, i]
                norm = np.max(np.abs(x1 - x0))
                x0 = x1.copy()
            cont += 1
            error = norm
        end = time.time()
        tiempo = end - start
        return x1, error, tiempo

    def Elminacion_Gauss(self, A, b):
        n = len(b)
        x = np.zeros(n)

        for k in range(n - 1):
            for i in range(k + 1, n):
                lam = A[i][k] / A[k][k]
                A[i, k:n] = A[i, k:n] - lam * A[k, k:n]
                b[i] = b[i] - lam * b[k]

        for k in range(n - 1, -1, -1):
            x[k] = (b[k] - np.dot(A[k, k + 1:n], x[k + 1:n])) / A[k, k]

        return x
