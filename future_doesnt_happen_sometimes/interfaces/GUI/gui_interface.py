from tkinter import *
from tkinter import messagebox
from tkinter import Text
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import matplotlib
import numpy as np

from interfaces.GUI.utility import pattern_func

from utility.tools import (calculate_xs_for_optimal_nodes, calculate_ys_for_optimal_nodes, get_additional_dots,
                           calculate_polynomial)

from interfaces.GUI.tabs_interface.gui_tabs_controller_interface import TabsController

from core.core_app_constants import APPLYING_OPTIMAL_NODES_ALGORITHM, APPLYING_UNIFORM_NODES_ALGORITHM
from core.core_errors import NewtonPolynomialWrongChoiceOfAlgorithm

from languages.russian.messaged_used_in_app import wrong_algorithm_choice_msg


class GUIInstaller:
    def __init__(self, window_width, window_height, title, tabs_controller):
        matplotlib.use('TkAgg')
        self.root = Tk()
        self.tabs_controller = tabs_controller

        self.fig = Figure(figsize=(3, 3), dpi=120)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        self.root.title(title)
        self.root.geometry(f'{window_width}x{window_height}')


class GUIInterface(GUIInstaller):
    def __init__(self, window_width, window_height, title, tabs_controller):
        super().__init__(window_width=window_width,
                         window_height=window_height,
                         title=title,
                         tabs_controller=tabs_controller)

    def make_draw(self, entered_array_xs, entered_array_ys, calculating_method):
        if calculating_method == APPLYING_UNIFORM_NODES_ALGORITHM:
            legend_label = 'Равномерные узлы'
        elif calculating_method == APPLYING_OPTIMAL_NODES_ALGORITHM:
            legend_label = 'Оптимальные узлы'
        else:
            raise NewtonPolynomialWrongChoiceOfAlgorithm(wrong_algorithm_choice_msg)

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot(entered_array_xs, entered_array_ys, label=legend_label)
        ax.legend()
        self.canvas.draw_idle()


tabs_controller = TabsController
gui = GUIInterface(window_width=1500, window_height=900)


def calculate_polynomial_from_gui_interface():
    calculating_type = type_of_polynomial.get() + 1  # calculating_type equals either 1 or 2 here

    if calculating_type == APPLYING_UNIFORM_NODES_ALGORITHM:
        entered_array_xs = list(map(float, input_set_x.get().split()))
        entered_array_ys = list(map(float, input_set_y.get().split()))
        point_calculate_value_at = float(input_point_x.get())

        new_x_dots = list(np.linspace(entered_array_xs[0], entered_array_xs[-1], 100))
        new_y_dots = []

        for x_dot in new_x_dots:
            res = calculate_polynomial(x_dots=entered_array_xs, y_dots=entered_array_ys, inputed_x=x_dot,
                                       calculating_type=0)
            new_y_dots.append(res)

        result = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=inputed_x,
                                      calculating_type=0)
        make_draw(new_x_dots, new_y_dots, 0)

        if calculating_type == uniform_nodes_type:
            messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
                                             f'P({inputed_x}) = {result}')
        elif calculating_type == optimal_nodes_type:
            messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
                                             f'P({inputed_x}) = {result}')
        else:
            print('Ошибка')

    elif calculating_type == optimal_nodes_type:
        a, b, count = input_set_x.get().split()
        a, b, count = float(a), float(b), int(count)
        y_dots_optimal = calculate_ys_for_optimal_nodes(4)  # list(map(float, input_set_y.get().split()))
        inputed_x = float(input_point_x.get())

        x_dots_optimal = calculate_xs_for_optimal_nodes(a, b, count)

        new_x_dots = list(np.linspace(x_dots_optimal[0], x_dots_optimal[-1], 100))
        new_y_dots = []
        for x_dot in new_x_dots:
            res = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=x_dot,
                                       calculating_type=1)
            new_y_dots.append(res)

        result = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=inputed_x,
                                      calculating_type=1)  # switch 1 to variable

        make_draw(new_x_dots, new_y_dots, 1)

        if calculating_type == uniform_nodes_type:
            messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
                                             f'P({inputed_x}) = {result}')
        elif calculating_type == optimal_nodes_type:
            messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
                                             f'P({inputed_x}) = {result}')
        else:
            print('Ошибка')


# /////


def create_draw_ex_tab(x_dots_polynomial=None, y_dots_uniform=None, y_dots_optimal=None):
    pattern_func_x_dots = np.linspace(-10, 13, 200)
    pattern_func_y_dots = []
    for x_dot in pattern_func_x_dots:
        pattern_func_y_dots.append(pattern_func(x_dot))

    fig.clear()
    ax = fig.add_subplot(111)
    if y_dots_uniform is not None:
        ax.plot(x_dots_polynomial, y_dots_uniform, label='равномерные узлы')
    if y_dots_optimal is not None:
        ax.plot(x_dots_polynomial, y_dots_optimal, label='оптимальные узлы')
    ax.plot(pattern_func_x_dots, pattern_func_y_dots, label='12x^3-8x^2-5x+2')
    ax.legend()
    canvas.draw_idle()


create_draw_ex_tab()


def calculate_polynomial_from_example_tab():
    """
    Reading data from inputs in the program
    :return:
    """

    a, b = list(map(float, input_borders.get().split()))
    count = int(count_n.get())
    x_dots_uniform = list(map(float, input_set_x_ex.get().split()))
    y_dots_uniform = list(map(float, input_set_y_ex.get().split()))
    inputed_x = float(input_point_x_ex.get())

    x_dots_optimal = calculate_xs_for_optimal_nodes(a, b, count)
    y_dots_optimal = calculate_ys_for_optimal_nodes(count)

    new_x_dots_polynomial, new_y_dots_uniform, new_y_dots_optimal = get_additional_dots(x_dots_uniform=x_dots_uniform,
                                                                                        x_dots_optimal=x_dots_optimal,
                                                                                        y_dots_optimal=y_dots_optimal,
                                                                                        y_dots_uniform=y_dots_uniform)
    uniform_nodes = 0
    optimal_nodes = 1

    result_with_optimal = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=inputed_x,
                                               calculating_type=optimal_nodes)

    result_with_uniform = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=inputed_x,
                                               calculating_type=uniform_nodes)

    create_draw_ex_tab(new_x_dots_polynomial, new_y_dots_uniform, new_y_dots_optimal)

    messagebox.showinfo('Результат', f'Оптимальные узлы P({inputed_x}) = {result_with_optimal}\n'
                                     f'Равномерные узлы P({inputed_x}) = {result_with_uniform}\n'
                                     f'Значение самой функции: {pattern_func(inputed_x)}')


# ///////


def create_draw(x_dots, y_dots_uniform, y_dots_optimal):
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(x_dots, y_dots_uniform, label='uniform')
    ax.plot(x_dots, y_dots_optimal, label='optimal')
    print('Create_draw_2: y_uni, y_opti', y_dots_uniform, '\n', y_dots_optimal)
    ax.legend()
    canvas.draw_idle()


btn_calculate_polynomial = Button(reading_console_tab, text="Найти значение полинома",
                                  command=calculate_polynomial_from_gui_interface,
                                  width=25)

btn_calculate_polynomial.grid(column=0, row=6, padx=15, pady=5)

# ==================================

radio_btn_uniform_nodes = Radiobutton(reading_file_tab, text='Полином с равномерными узлами',
                                      variable=type_of_polynomial, value=0)
radio_btn_optimal_nodes = Radiobutton(reading_file_tab, text='Полином с оптимальными узлами',
                                      variable=type_of_polynomial, value=1)
radio_btn_uniform_nodes.grid(column=0, row=2)
radio_btn_optimal_nodes.grid(column=1, row=2)

label_for_add_member = Label(reading_file_tab, text='Считывание с файла', font=("Arial Bold", 12, "bold"))
label_for_add_member.grid(column=0, row=1, pady=1)

label_for_add_member = Label(reading_file_tab, text='Считанные с файла значения', font=("Arial Bold", 12))
label_for_add_member.grid(column=0, row=5, pady=1)

description_text = Text(reading_file_tab, height=4, width=30, font=("Arial Bold", 11))
description_text.grid(column=0, row=6, padx=5)

global_file_path = None


def chose_file():
    file_path = filedialog.askopenfilename()
    global global_file_path
    global_file_path = file_path

    with open(file_path, mode='r', encoding='utf8') as f:
        x_dots = f.readline()
        y_dots = f.readline()
        inputed_x = f.readline()
    description_text.insert(END, f'x: {x_dots}'
                                 f'y: {y_dots}'
                                 f't: {inputed_x}')


def calculate_polynomial_from_file():
    global global_file_path
    with open(global_file_path, mode='r', encoding='utf8') as f:
        x_dots = f.readline().split()
        y_dots = f.readline().split()
        inputed_x = f.readline()

    calculating_type = type_of_polynomial.get()  # 0 - uniform nodes, 1 - optimal nodes
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    x_dots = list(map(float, x_dots))
    y_dots = list(map(float, y_dots))
    inputed_x = float(inputed_x)

    result = calculate_polynomial(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x, calculating_type=calculating_type)

    new_x_dots = list(np.linspace(x_dots[0], x_dots[-1], 100))
    new_y_dots = []
    for x_dot in new_x_dots:
        res = calculate_polynomial(x_dots=x_dots, y_dots=y_dots, inputed_x=x_dot,
                                   calculating_type=calculating_type)
        new_y_dots.append(res)

    make_draw(new_x_dots, new_y_dots, calculating_type)

    if calculating_type == uniform_nodes_type:
        messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
                                         f'P({inputed_x}) = {result}')
    elif calculating_type == optimal_nodes_type:
        messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
                                         f'P({inputed_x}) = {result}')
    else:
        print('Ошибка')


btn_add_member = Button(reading_file_tab, text="Выбрать файл", command=chose_file,
                        width=15)
btn_add_member.grid(column=0, row=3, pady=5)

btn_add_member = Button(reading_file_tab, text="Найти значение полинома", command=calculate_polynomial_from_file,
                        width=30)
btn_add_member.grid(column=0, row=4, pady=10)

if __name__ == '__main__':
    def setup():
        input_borders.insert(0, '-5 8')
        input_set_x_ex.insert(0, '-5 -2 2 8')
        input_set_y_ex.insert(0, '-1673 -116 56 5594')


    setup()

    root.mainloop()
