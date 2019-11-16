from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
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


def calculate_polynomial():
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    calculating_type = type_of_polynomial.get()  # 0 - uniform nodes, 1 - optimal nodes

    try:
        x_dots = list(map(float, input_set_x.get().split()))
        if len(x_dots) == 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning('Ошибка', 'Множество Х должно содержать только числа и не должно быть пустым')
        return False
    try:
        y_dots = list(map(float, input_set_y.get().split()))
        if len(y_dots) == 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning('Ошибка', 'Множество Y должно содержать только числа и не должно быть пустым')
        return False
    try:
        inputed_x = float(input_point_x.get())
    except ValueError:
        messagebox.showwarning('Ошибка', 'Координата точки по Х должна быть числом')
        return False

    if len(x_dots) != len(y_dots):
        messagebox.showwarning('Ошибка', 'Количество элементов в множествах X и Y должны совпадать')
        return False  # error

    if calculating_type == uniform_nodes_type:
        result = calculate_newton_polynomial_uniform_nodes(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
        messagebox.showinfo('Результат', f'Значение полинома P(x) с равномерными узлами '
        f'P({inputed_x}) = {result}')
    elif calculating_type == optimal_nodes_type:
        result = calculate_newton_polynomial_optimal_nodes(x_dots=x_dots, y_dots=y_dots, inputed_x=inputed_x)
        messagebox.showinfo('Результат', f'Значение полинома P(x) с оптимальными узлами '
        f'P({inputed_x}) = {result}')
    else:
        print('Ошибка')


btn_calculate_polynomial = Button(reading_console_tab, text="Найти значение полинома", command=calculate_polynomial,
                                  width=25)
btn_calculate_polynomial.grid(column=0, row=6, padx=15, pady=5)

label_for_add_member = Label(reading_file_tab, text='Считывание с файла', font=("Arial Bold", 16))
label_for_add_member.grid(column=0, row=6, pady=5)

input_add_name = Entry(reading_file_tab, width=20)
input_add_surname = Entry(reading_file_tab, width=20)
input_add_phone_number = Entry(reading_file_tab, width=20)
input_add_name.grid(column=0, row=8)
input_add_surname.grid(column=1, row=8, padx=5)
input_add_phone_number.grid(column=2, row=8, padx=25)


def add_new_member():
    pass


def del_member():
    pass


btn_add_member = Button(reading_file_tab, text="Добавить нового сотрудника", command=add_new_member, width=30)
btn_add_member.grid(column=0, row=9, pady=10, padx=5)

if __name__ == '__main__':
    root.mainloop()
