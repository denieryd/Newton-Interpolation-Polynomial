from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Text
from tkinter.ttk import Combobox
from tkinter import filedialog
from newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes
from newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes

window_width = 700
window_height = 300
root = Tk()
root.title("Вычисление первого полинома Ньютона")
root.geometry(f'{window_width}x{window_height}')

tab_control = ttk.Notebook(root)
reading_console_tab = ttk.Frame(tab_control)
tab_control.add(reading_console_tab, text='Считывание с консоли')
tab_control.pack(expand=1, fill='both')

reading_file_tab = ttk.Frame(tab_control)
tab_control.add(reading_file_tab, text='Считывание с файла')
tab_control.pack(expand=1, fill='both')

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


def check_validate_data(x_dots, y_dots, inputed_x):
    try:
        x_dots = list(map(float, x_dots))
        if len(x_dots) == 0:
            raise ValueError

    except ValueError:
        return True, 'Множество Х должно содержать только числа и не должно быть пустым'
    try:
        y_dots = list(map(float, y_dots))
        if len(y_dots) == 0:
            raise ValueError

    except ValueError:
        return True, 'Множество Y должно содержать только числа и не должно быть пустым'
    try:
        inputed_x = float(inputed_x)
    except ValueError:
        return True, 'Координата точки по Х должна быть числом'
    if len(x_dots) != len(y_dots):
        return True, 'Количество элементов в множествах X и Y должны совпадать'
    return False, 'validated'


def calculate_polynomial(x_dots, y_dots, inputed_x, calculating_type):
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    result = None

    if calculating_type == uniform_nodes_type:
        result = calculate_newton_polynomial_uniform_nodes(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    elif calculating_type == optimal_nodes_type:
        result = calculate_newton_polynomial_optimal_nodes(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    else:
        print('Ошибка')

    return result


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

    error, msg = check_validate_data(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    # after checking data to validation we can work with it
    x_dots = list(map(float, x_dots))
    y_dots = list(map(float, y_dots))
    inputed_x = float(inputed_x)

    if error:
        messagebox.showwarning('Ошибка', msg)
        return False

    result = calculate_polynomial(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x, calculating_type=calculating_type)

    if calculating_type == uniform_nodes_type:
        messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
        f'P({inputed_x}) = {result}')
    elif calculating_type == optimal_nodes_type:
        messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
        f'P({inputed_x}) = {result}')
    else:
        print('Ошибка')


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

    check_validate_data(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
    x_dots = list(map(float, x_dots))
    y_dots = list(map(float, y_dots))
    inputed_x = float(inputed_x)

    calculating_type = type_of_polynomial.get()  # 0 - uniform nodes, 1 - optimal nodes
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    error, msg = check_validate_data(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)

    if error:
        messagebox.showwarning('Ошибка', msg)
        return False

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
