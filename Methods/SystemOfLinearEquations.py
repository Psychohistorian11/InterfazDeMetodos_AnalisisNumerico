import numpy as np
import time
import tkinter as tk


class SystemOfLinearEquations:

    def gauss_seidel(self, A, b, x0, tol):

        D = np.diag(np.diag(A))
        L = D - np.tril(A)
        U = D - np.triu(A)
        Tg = np.dot(np.linalg.inv(D - L), U)
        Cg = np.dot(np.linalg.inv(D - L), b)
        lam, vec = np.linalg.eig(Tg)
        radio = max(abs(lam))
        i = 0  # iterations
        if radio < 1:
            x1 = np.dot(Tg, x0) + Cg
            i += 1
            error = max(abs(x1-x0))
            while max(np.abs(x1 - x0)) > tol:
                x0 = x1
                x1 = np.dot(Tg, x0) + Cg
                i += 1
                error = max(abs(x1-x0))
            return x1, radio, i, error
        else:
            print("El sistema iterativo no converge a la solución única del sistema")

    def pivoteo(self, A, b):

        n = len(b)
        for i in range(n):
            max_fila = np.argmax(np.abs(A[i:n, i])) + i
            if A[max_fila, i] == 0:
                raise ValueError("El sistema no tiene solución única.")
            A[[i, max_fila]] = A[[max_fila, i]]
            b[[i, max_fila]] = b[[max_fila, i]]
            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]
                b[j] -= factor * b[i]
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        return x

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
