from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Text
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np
import matplotlib

from tools import get_x_dots_optimal, get_y_dots_optimal, get_additional_dots, calculate_polynomial

matplotlib.use('TkAgg')

window_width = 1500
window_height = 900
root = Tk()
root.title("Вычисление первого полинома Ньютона")
root.geometry(f'{window_width}x{window_height}')

tab_control = ttk.Notebook(root)

reading_console_tab = ttk.Frame(tab_control)
tab_control.add(reading_console_tab, text='Считывание с консоли')
tab_control.pack(expand=1, fill='both')

example_tab = ttk.Frame(tab_control)
tab_control.add(example_tab, text='Эталонный пример')
tab_control.pack(expand=1, fill='both')

reading_file_tab = ttk.Frame(tab_control)
tab_control.add(reading_file_tab, text='Считывание с файла')
tab_control.pack(expand=1, fill='both')

header_label = Label(example_tab, text="Сравнение оптимальных и равномерных узлов"
                                       "\nдля функции 12x^3-8x^2-5x+2",
                     font=("Arial Bold", 13, 'bold'))
header_label.grid(column=0, row=0)
label_input_iteration = Label(example_tab, text="Выберите n", font=("Arial Bold", 11))
label_input_iteration.grid(column=0, row=1)

label_borders = Label(example_tab, text="Введите a и b для оптимальных узлов", font=("Arial Bold", 11))

label_borders.grid(column=0, row=2)

label_input_set_x_ex = Label(example_tab, text="Введите множество x через пробел", font=("Arial Bold", 11))
label_input_set_x_ex.grid(column=0, row=3)

label_input_set_y_ex = Label(example_tab, text="Введите множество y через пробел", font=("Arial Bold", 11))
label_input_set_y_ex.grid(column=0, row=4)

label_input_set_y_ex = Label(example_tab, text="Введите точку х, для вычисление P(x)",
                             font=("Arial Bold", 11))
label_input_set_y_ex.grid(column=0, row=5)

count_n = StringVar(root)
count_n.set('4')
count_n_switching_menu = OptionMenu(example_tab, count_n, "4", "8")

count_n_switching_menu.grid(column=1, row=1)

label_borders = Label(example_tab, text="Введите a и b для оптимальных узлов", font=("Arial Bold", 11))
input_borders = Entry(example_tab, width=20)
label_borders.grid(column=0, row=2)
input_borders.grid(column=1, row=2, pady=10)

label_input_set_x_ex = Label(example_tab, text="Введите множество x через пробел", font=("Arial Bold", 11))
input_set_x_ex = Entry(example_tab, width=20)
label_input_set_x_ex.grid(column=0, row=3)
input_set_x_ex.grid(column=1, row=3, pady=10)

label_input_set_y_ex = Label(example_tab, text="Введите множество y через пробел", font=("Arial Bold", 11))
input_set_y_ex = Entry(example_tab, width=20)
input_set_y_ex.grid(column=1, row=4, pady=10)
label_input_set_y_ex.grid(column=0, row=4)

label_input_set_y_ex = Label(example_tab, text="Введите точку х, для вычисление P(x)", font=("Arial Bold", 11))
input_point_x_ex = Entry(example_tab, width=20)
label_input_set_y_ex.grid(column=0, row=5)
input_point_x_ex.grid(column=1, row=5, pady=10)

fig = Figure(figsize=(3, 3), dpi=120)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


# //////////////

def create_draw_from_gui(x_dots, y_dots, nodes_type):
    if nodes_type == 0:
        lbl = 'Равномерные узлы'
    else:
        lbl = 'Оптимальные узлы'

    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(x_dots, y_dots, label=lbl)
    ax.legend()
    canvas.draw_idle()


def create_draw_file_tab(x_dots, y_dots, nodes_type):
    if nodes_type == 0:
        lbl = 'Равномерные узлы'
    else:
        lbl = 'Оптимальные узлы'

    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(x_dots, y_dots, label=lbl)
    ax.legend()
    canvas.draw_idle()


def calculate_polynomial_from_gui_interface():
    """
    Reading data from inputs in the program
    :return:
    """

    calculating_type = type_of_polynomial.get()
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    print('POLY TYPE', calculating_type)
    if calculating_type == uniform_nodes_type:
        x_dots_uniform = list(map(float, input_set_x.get().split()))
        y_dots_uniform = list(map(float, input_set_y.get().split()))
        inputed_x = float(input_point_x.get())

        new_x_dots = list(np.linspace(x_dots_uniform[0], x_dots_uniform[-1], 100))
        new_y_dots = []
        for x_dot in new_x_dots:
            res = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=x_dot,
                                       calculating_type=0)
            new_y_dots.append(res)

        result = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=inputed_x,
                                      calculating_type=0)
        create_draw_from_gui(new_x_dots, new_y_dots, 0)

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
        y_dots_optimal = get_y_dots_optimal(4)  # list(map(float, input_set_y.get().split()))
        inputed_x = float(input_point_x.get())

        x_dots_optimal = get_x_dots_optimal(a, b, count)

        new_x_dots = list(np.linspace(x_dots_optimal[0], x_dots_optimal[-1], 100))
        new_y_dots = []
        for x_dot in new_x_dots:
            res = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=x_dot,
                                       calculating_type=1)
            new_y_dots.append(res)

        result = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=inputed_x,
                                      calculating_type=1)  # switch 1 to variable

        create_draw_from_gui(new_x_dots, new_y_dots, 1)

        if calculating_type == uniform_nodes_type:
            messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
            f'P({inputed_x}) = {result}')
        elif calculating_type == optimal_nodes_type:
            messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
            f'P({inputed_x}) = {result}')
        else:
            print('Ошибка')


# /////


def pattern_func(x):
    return 12 * (x ** 3) - 8 * (x ** 2) - 5 * x + 2


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

    x_dots_optimal = get_x_dots_optimal(a, b, count)
    y_dots_optimal = get_y_dots_optimal(count)

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


btn_calculate_polynomial_ex_tab = Button(example_tab, text="Найти значение полинома",
                                         command=calculate_polynomial_from_example_tab,
                                         width=25)

btn_calculate_polynomial_ex_tab.grid(column=2, row=5, padx=15, pady=5)

# ///////

label_input_set_x = Label(reading_console_tab, text="Введите множество x через пробел", font=("Arial Bold", 11))
input_set_x = Entry(reading_console_tab, width=20)
label_input_set_x.grid(column=0, row=0)
input_set_x.grid(column=1, row=0, pady=10)

label_input_set_y = Label(reading_console_tab, text="Введите множество y через пробел", font=("Arial Bold", 11))
input_set_y = Entry(reading_console_tab, width=20)
input_set_y.grid(column=1, row=3, pady=10)
label_input_set_y.grid(column=0, row=3)

label_input_set_y = Label(reading_console_tab, text="Введите точку х, для вычисление P(x)", font=("Arial Bold", 11))
input_point_x = Entry(reading_console_tab, width=20)
label_input_set_y.grid(column=0, row=4)
input_point_x.grid(column=1, row=4, pady=10)

type_of_polynomial = IntVar()
type_of_polynomial.set(0)

radio_btn_uniform_nodes = Radiobutton(reading_console_tab, text='Полином с равномерными узлами',
                                      variable=type_of_polynomial, value=0)
radio_btn_optimal_nodes = Radiobutton(reading_console_tab, text='Полином с оптимальными узлами',
                                      variable=type_of_polynomial, value=1)
radio_btn_uniform_nodes.grid(column=0, row=5)
radio_btn_optimal_nodes.grid(column=1, row=5)


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

    create_draw_file_tab(new_x_dots, new_y_dots, calculating_type)

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
