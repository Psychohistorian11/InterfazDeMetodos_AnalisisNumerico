import tkinter as tk
from tkinter import font as tkfont

from Interface.ViewsMethods.Zeros import Zeros
from Interface.ViewsMethods.Taylor import Taylor
from Interface.ViewsMethods.SystemEquations import SystemEquations
from Interface.ViewsMethods.DiffEquations import DiffEquations
from Interface.ViewsMethods.Interpolation import Interpolation

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")

        # Set window size
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")  # Light grey background for better contrast

        # Define fonts
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        self.button_font = tkfont.Font(family="Helvetica", size=14)

        # Create title label
        label = tk.Label(root, text="Elija la solución que desea realizar:", font=self.title_font, bg="#f0f0f0")
        label.pack(pady=20)

        # Button configurations
        button_config = {
            'font': self.button_font,
            'bg': "#e7e7e7",  # Light grey button background
            'fg': "black",
            'activebackground': "#c7c7c7",  # Darker grey when button is pressed
            'activeforeground': "black",
            'relief': "raised",
            'width': 27,
            'height': 1
        }

        # Create buttons with enhanced styling
        btn_taylor = tk.Button(root, text="Método de Taylor", command=self.open_taylor_series, **button_config)
        btn_taylor.pack(pady=5)

        btn_open_interpolation_and_adjustment = tk.Button(root, text="Interpolación y Ajuste",
                                                          command=self.open_interpolation_and_adjustment, **button_config)
        btn_open_interpolation_and_adjustment.pack(pady=5)

        btn_open_systemOf_linear_equations = tk.Button(root, text="Sistemas de Ecuaciones Lineales",
                                                       command=self.open_systemOf_linear_equations, **button_config)
        btn_open_systemOf_linear_equations.pack(pady=5)

        btn_open_zerosOf_functions = tk.Button(root, text="Ceros de funciones",
                                               command=self.open_zerosOf_functions, **button_config)
        btn_open_zerosOf_functions.pack(pady=5)

        btn_open_differential_equations = tk.Button(root, text="Ecuaciones Diferenciales",
                                                    command=self.open_differential_equations, **button_config)
        btn_open_differential_equations.pack(pady=5)

    def open_taylor_series(self):
        Taylor(self.root)

    def open_interpolation_and_adjustment(self):
        Interpolation(self.root)

    def open_systemOf_linear_equations(self):
        SystemEquations(self.root)

    def open_zerosOf_functions(self):
        Zeros(self.root)

    def open_differential_equations(self):
        DiffEquations(self.root)

