import tkinter as tk
from tkinter import messagebox
import numpy as np
from Methods.SystemOfLinearEquations import SystemOfLinearEquations

class SystemEquations:

    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(root)
        self.window.title("Sistema de Ecuaciones Lineales")

        tk.Label(self.window, text="Ingrese el número de filas:").grid(row=0, column=0, padx=5, pady=5)
        self.rows_entry = tk.Entry(self.window)
        self.rows_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Ingrese el número de columnas:").grid(row=1, column=0, padx=5, pady=5)
        self.cols_entry = tk.Entry(self.window)
        self.cols_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.window, text="Crear Sistema", command=self.create_system)
        self.submit_button.grid(row=2, columnspan=2, pady=10)

        self.system_frame = tk.Frame(self.window)
        self.system_frame.grid(row=3, columnspan=2, pady=10, padx=10)

        self.method_var = tk.StringVar(self.window)
        self.method_var.set("Eliminación Gaussiana")  # Valor por defecto
        self.methods = ["Eliminación Gaussiana", "Pivoteo", "Gauss-Seidel Matricial"]
        self.method_menu = tk.OptionMenu(self.window, self.method_var, *self.methods, command=self.show_gauss_seidel_inputs)
        self.method_menu.grid(row=4, columnspan=2, pady=10)

        self.additional_frame = tk.Frame(self.window)
        self.additional_frame.grid(row=5, columnspan=2, pady=10, padx=10)

        self.result_frame = tk.Frame(self.window)
        self.result_frame.grid(row=6, columnspan=2, pady=10, padx=10)

    def create_system(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")
            return

        if rows != cols:
            messagebox.showwarning("Advertencia", "Para crear un sistema de ecuaciones, se necesita una matriz cuadrada.")
            return

        for widget in self.system_frame.winfo_children():
            widget.destroy()

        self.entries = []
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(self.system_frame, width=5)
                entry.grid(row=i, column=2*j, padx=5, pady=5)
                row_entries.append(entry)
                label = tk.Label(self.system_frame, text=f"x{j+1}")
                label.grid(row=i, column=2*j+1, padx=5, pady=5, sticky="w")

            tk.Label(self.system_frame, text="=").grid(row=i, column=2*cols, padx=5, pady=5, sticky="e")
            result_entry = tk.Entry(self.system_frame, width=5)
            result_entry.grid(row=i, column=2*cols+1, padx=5, pady=5)
            row_entries.append(result_entry)
            self.entries.append(row_entries)

        self.continue_button = tk.Button(self.system_frame, text="Continuar", command=self.solve_system)
        self.continue_button.grid(row=rows + 1, columnspan=2*cols+1, pady=10)

    def show_gauss_seidel_inputs(self, value):
        for widget in self.additional_frame.winfo_children():
            widget.destroy()

        if value == "Gauss-Seidel Matricial":
            tk.Label(self.additional_frame, text="Tolerancia:").grid(row=0, column=0, padx=5, pady=5)
            self.tol_entry = tk.Entry(self.additional_frame)
            self.tol_entry.grid(row=0, column=1, padx=5, pady=5)

    def solve_system(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        try:
            A = []
            b = []
            for row_entries in self.entries:
                row = [float(entry.get()) for entry in row_entries[:-1]]
                A.append(row)
                b.append(float(row_entries[-1].get()))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos en todas las casillas.")
            return

        A_matrix = np.array(A)
        b_vector = np.array(b)
        method = self.method_var.get()
        solver = SystemOfLinearEquations()

        try:
            if method == "Eliminación Gaussiana":
                solution = solver.Elminacion_Gauss(A_matrix, b_vector)
                solution_str = "\n".join([f"x{i+1} = {val}" for i, val in enumerate(solution)])
            elif method == "Pivoteo":
                solution = solver.pivoteo(A_matrix, b_vector)
                solution_str = "\n".join([f"x{i+1} = {val}" for i, val in enumerate(solution)])
            elif method == "Gauss-Seidel Matricial":
                x0 = np.zeros(len(b_vector))
                tol = float(self.tol_entry.get())
                solution, radio, iterations, error = solver.gauss_seidel(A_matrix, b_vector, x0, tol)
                solution_str = (f"Solución: {solution}\n"
                                f"Radio: {radio}\n"
                                f"Iteraciones: {iterations}\n"
                                f"Error: {error}")
            else:
                raise ValueError("Método no soportado")

            tk.Label(self.result_frame, text="Resultado:").grid(row=0, column=0, padx=5, pady=5)
            result_label = tk.Label(self.result_frame, text=solution_str, justify="left")
            result_label.grid(row=1, column=0, padx=5, pady=5)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo resolver el sistema: {e}")


