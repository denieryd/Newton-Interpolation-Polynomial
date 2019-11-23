from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Text
from tkinter import filedialog

import matplotlib

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes
from newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes

import numpy as np

from tools import get_x_dots_optimal

matplotlib.use('TkAgg')

window_width = 1000
window_height = 600
root = Tk()
root.title("Вычисление первого полинома Ньютона")
root.geometry(f'{window_width}x{window_height}')

tab_control = ttk.Notebook(root)

example_tab = ttk.Frame(tab_control)
tab_control.add(example_tab, text='Эталонный пример')
tab_control.pack(expand=1, fill='both')

reading_console_tab = ttk.Frame(tab_control)
tab_control.add(reading_console_tab, text='Считывание с консоли')
tab_control.pack(expand=1, fill='both')

reading_file_tab = ttk.Frame(tab_control)
tab_control.add(reading_file_tab, text='Считывание с файла')
tab_control.pack(expand=1, fill='both')


# //////////////


def calculate_polynomial(x_dots, y_dots, inputed_x, calculating_type):
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    result = None
    print(calculating_type, 'calc type')
    if calculating_type == uniform_nodes_type:
        print('yes uni')
        result = calculate_newton_polynomial_uniform_nodes(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    elif calculating_type == optimal_nodes_type:
        print('yes, opti')
        print(x_dots, y_dots)
        result = calculate_newton_polynomial_optimal_nodes(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    else:
        print('Ошибка')

    return result


def create_x_dots(lower_border, high_border, step):
    x_dots = [lower_border]
    while lower_border < high_border:
        lower_border += step
        x_dots.append(lower_border)
    return x_dots


def get_additional_dots(x_dots_uniform, x_dots_optimal, y_dots_uniform, y_dots_optimal):
    new_y_dots_uniform_nodes = []
    new_y_dots_optimal_nodes = []

    new_x_dots = list(np.linspace(-15, 15, 200))

    for x_dot in new_x_dots:
        res_uniform = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=x_dot,
                                           calculating_type=0)
        res_optimal = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=x_dot,
                                           calculating_type=1)
        new_y_dots_uniform_nodes.append(res_uniform)
        new_y_dots_optimal_nodes.append(res_optimal)

    return new_x_dots, new_y_dots_uniform_nodes, new_y_dots_optimal_nodes


def calculate_polynomial_from_gui_interface():
    """
    Reading data from inputs in the program
    :return:
    """

    x_dots = input_set_x.get().split()  # if x_dots is None else x_dots
    y_dots = input_set_y.get().split()  # if y_dots is None else y_dots
    inputed_x = input_point_x.get()  # if inputed_x is None else inputed_x

    calculating_type = type_of_polynomial.get()  # 0 - uniform nodes, 1 - optimal nodes
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    error, msg = False, 'mock error validate'  # check_validate_data(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    # after checking data to validation we can work with it
    if error:
        messagebox.showwarning('Ошибка', msg)
        return False
    else:

        if calculating_type == optimal_nodes_type:
            x0 = float(x_dots[0])
            xn = float(x_dots[1])
            step = float(x_dots[2])
            count = int((xn - x0) / step + 1)
            print(f'count is {count}')
            x_dots_optimal = get_x_dots_optimal(x0, xn, count)
            x_dots_uniform = create_x_dots(x0, xn, step)
            print(x_dots_optimal, 'dots optimal')
            print('x_dots_uni, opti len', len(x_dots_uniform), len(x_dots_uniform))
        elif calculating_type == uniform_nodes_type:
            pass
        # x_dots = list(map(float, x_dots))
        y_dots = list(map(float, y_dots))
        inputed_x = float(inputed_x)

        # new_x_dots = create_x_dots(lower_border, high_border, step / 100)
        lower_border = float(x_dots[0])
        high_border = float(x_dots[-1])
        new_x_dots = np.linspace(lower_border, high_border, 100)
        # new_y_dots_uniform, new_y_dots_optimal = get_additional_dots(x_dots, y_dots, new_x_dots)

    result = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots, inputed_x=inputed_x,
                                  calculating_type=1)  # switch 1 to variable
    print('result is:', result)
    # create_draw_2(new_x_dots, new_y_dots_uniform, new_y_dots_optimal)

    if calculating_type == uniform_nodes_type:
        messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
        f'P({inputed_x}) = {result}')
    elif calculating_type == optimal_nodes_type:
        messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
        f'P({inputed_x}) = {result}')
    else:
        print('Ошибка')


# /////


header_label = Label(example_tab, text="Сравнение оптимальных и равномерных узлов"
                                       "\nдля функции 12x^3-8x^2-5x+2", font=("Arial Bold", 13, 'bold'))
header_label.grid(column=0, row=0)

label_input_iteration = Label(example_tab, text="Выберите n", font=("Arial Bold", 11))
count_n = StringVar(root)
count_n.set('4')
count_n_switching_menu = OptionMenu(example_tab, count_n, "4", "8")
label_input_iteration.grid(column=0, row=1)
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


def get_y_dots_optimal(count):
    if count == 4:
        return [-1381.4614750443766,
                -179.44171639342537,
                16.99999999999998,
                1556.3671878257146]
    elif count == 8:
        return [1.3008848966265942,
                2.5389166448734786,
                1.272654113572865,
                -1.3347452240844833,
                6.6875,
                41.21983426316527,
                105.73833675454303,
                180.80483335512648, ]


def setup():
    input_borders.insert(0, '-5 8')
    input_set_x_ex.insert(0, '-5 -2 2 8')
    input_set_y_ex.insert(0, '-1673 -116 56 5594')


setup()

fig = Figure(figsize=(3, 3), dpi=120)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def pattern_func(x):
    return 12 * (x ** 3) - 8 * (x ** 2) - 5 * x + 2


def create_draw_ex_tab(x_dots_polynomial=None, y_dots_uniform=None, y_dots_optimal=None):
    pattern_func_x_dots = np.linspace(-15, 15, 100)
    pattern_func_y_dots = []
    for x_dot in pattern_func_x_dots:
        pattern_func_y_dots.append(pattern_func(x_dot))

    fig.clear()
    ax = fig.add_subplot(111)
    if y_dots_uniform is not None:
        ax.plot(x_dots_polynomial, y_dots_uniform, label='uniform')
    if y_dots_optimal is not None:
        ax.plot(x_dots_polynomial, y_dots_optimal, label='optimal')
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

    step = (b - a) / (count - 1)
    x_dots_optimal = get_x_dots_optimal(a, b, count)
    print(f'xdotsoptimal', x_dots_optimal)
    y_dots_optimal = get_y_dots_optimal(count)
    # new_x_dots = create_x_dots(lower_border, high_border, step / 100)
    # lower_border = float(x_dots[0])
    # high_border = float(x_dots[-1])
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

    messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
    f'P({inputed_x}) = {result_with_optimal} '
    f'С равномерными узлами '
    f'P({inputed_x}) = {result_with_uniform}')


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

    # error, msg = check_validate_data(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)

    # if error:
    #    messagebox.showwarning('Ошибка', msg)
    #    return False

    x_dots = list(map(float, x_dots))
    y_dots = list(map(float, y_dots))
    inputed_x = float(inputed_x)

    result = calculate_polynomial(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x, calculating_type=calculating_type)

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
    root.mainloop()
