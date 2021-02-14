import numpy as np

from tkinter import *
from tkinter import ttk

from math_algorithm.newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes
from math_algorithm.newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes

from interfaces.GUI.utility import calculate_xs_for_optimal_nodes, calculate_ys_for_optimal_nodes, pattern_func
from interfaces.GUI.utility import get_additional_dots, calculate_polynomial


class TabsController:
    def __init__(self, root):
        self.root = root
        self._tabs_controller = ttk.Notebook(root)

        self.reading_console_tab = ttk.Frame(self._tabs_controller)
        self.example_tab = ttk.Frame(self._tabs_controller)
        self.reading_file_tab = ttk.Frame(self._tabs_controller)

        # todo: refactor here (it needs to have good style of init)

        self.type_of_polynomial = IntVar()
        self.type_of_polynomial.set(0)
        self.count_n = StringVar(self.root)
        self.count_n.set('4')
        self.count_n_switching_menu = OptionMenu(self.example_tab, self.count_n, "4", "8")

        self.input_borders = None
        self.input_set_x_ex = None
        self.input_set_y_ex = None
        self.input_point_x_ex = None
        self.btn_calculate_polynomial_ex_tab = None

    def init_controller(self):
        self._init_tabs()
        self._create_and_init_all_entities_in_example_tab()
        self._create_and_init_all_entities_in_reading_console_tab()

    def _init_tabs(self):
        self._tabs_controller.add(self.reading_console_tab, text='Считывание с консоли')
        self._tabs_controller.pack(expand=1, fill='both')

        self._tabs_controller.add(self.example_tab, text='Эталонный пример')
        self._tabs_controller.pack(expand=1, fill='both')

        self._tabs_controller.add(self.reading_file_tab, text='Считывание с файла')
        self._tabs_controller.pack(expand=1, fill='both')

    def _create_and_init_all_entities_in_example_tab(self):
        # LABELS IN EXAMPLE TAB HERE
        header_label = Label(self.example_tab, text="Сравнение оптимальных и равномерных узлов"
                                                    "\nдля функции 12x^3-8x^2-5x+2",
                             font=("Arial Bold", 13, 'bold'))
        header_label.grid(column=0, row=0)

        label_input_iteration = Label(self.example_tab, text="Выберите n", font=("Arial Bold", 11))
        label_input_iteration.grid(column=0, row=1)

        label_borders = Label(self.example_tab, text="Введите a и b для оптимальных узлов", font=("Arial Bold", 11))
        label_borders.grid(column=0, row=2)

        label_input_set_x_ex = Label(self.example_tab, text="Введите множество x через пробел", font=("Arial Bold", 11))
        label_input_set_x_ex.grid(column=0, row=3)

        label_input_set_y_ex = Label(self.example_tab, text="Введите множество y через пробел", font=("Arial Bold", 11))
        label_input_set_y_ex.grid(column=0, row=4)

        label_input_set_y_ex = Label(self.example_tab, text="Введите точку х, для вычисление P(x)",
                                     font=("Arial Bold", 11))
        label_input_set_y_ex.grid(column=0, row=5)

        # INPUT FIELDS AND LABELS IN EXAMPLE TAB

        self.count_n_switching_menu.grid(column=1, row=1)

        label_borders = Label(self.example_tab, text="Введите a и b для оптимальных узлов", font=("Arial Bold", 11))
        self.input_borders = Entry(self.example_tab, width=20)
        label_borders.grid(column=0, row=2)
        self.input_borders.grid(column=1, row=2, pady=10)

        label_input_set_x_ex = Label(self.example_tab, text="Введите множество x через пробел",
                                     font=("Arial Bold", 11))
        self.input_set_x_ex = Entry(self.example_tab, width=20)
        label_input_set_x_ex.grid(column=0, row=3)
        self.input_set_x_ex.grid(column=1, row=3, pady=10)

        label_input_set_y_ex = Label(self.example_tab, text="Введите множество y через пробел",
                                     font=("Arial Bold", 11))
        self.input_set_y_ex = Entry(self.example_tab, width=20)
        self.input_set_y_ex.grid(column=1, row=4, pady=10)
        label_input_set_y_ex.grid(column=0, row=4)

        label_input_set_y_ex = Label(self.example_tab, text="Введите точку х, для вычисление P(x)",
                                     font=("Arial Bold", 11))
        self.input_point_x_ex = Entry(self.example_tab, width=20)
        label_input_set_y_ex.grid(column=0, row=5)
        self.input_point_x_ex.grid(column=1, row=5, pady=10)

        self.btn_calculate_polynomial_ex_tab = Button(self.example_tab, text="Найти значение полинома",
                                                      command=self.calculate_polynomial_from_example_tab,
                                                      width=25)

        self.btn_calculate_polynomial_ex_tab.grid(column=2, row=5, padx=15, pady=5)

    def _create_and_init_all_entities_in_reading_console_tab(self):
        label_input_set_x = Label(self.reading_console_tab, text="Введите множество x через пробел",
                                  font=("Arial Bold", 11))
        input_set_x = Entry(self.reading_console_tab, width=20)
        label_input_set_x.grid(column=0, row=0)
        input_set_x.grid(column=1, row=0, pady=10)

        label_input_set_y = Label(self.reading_console_tab, text="Введите множество y через пробел",
                                  font=("Arial Bold", 11))
        input_set_y = Entry(self.reading_console_tab, width=20)
        input_set_y.grid(column=1, row=3, pady=10)
        label_input_set_y.grid(column=0, row=3)

        label_input_set_y = Label(self.reading_console_tab, text="Введите точку х, для вычисление P(x)",
                                  font=("Arial Bold", 11))
        input_point_x = Entry(self.reading_console_tab, width=20)
        label_input_set_y.grid(column=0, row=4)
        input_point_x.grid(column=1, row=4, pady=10)

        radio_btn_uniform_nodes = Radiobutton(self.reading_console_tab, text='Полином с равномерными узлами',
                                              variable=self.type_of_polynomial, value=0)
        radio_btn_optimal_nodes = Radiobutton(self.reading_console_tab, text='Полином с оптимальными узлами',
                                              variable=self.type_of_polynomial, value=1)
        radio_btn_uniform_nodes.grid(column=0, row=5)
        radio_btn_optimal_nodes.grid(column=1, row=5)

    def create_draw_ex_tab(self, x_dots_polynomial=None, y_dots_uniform=None, y_dots_optimal=None):
        xs = np.linspace(-10, 13, 200)
        ys = []
        for x in xs:
            ys.append(pattern_func(x))

        fig.clear()
        ax = fig.add_subplot(111)
        if y_dots_uniform is not None:
            ax.plot(x_dots_polynomial, y_dots_uniform, label='равномерные узлы')
        if y_dots_optimal is not None:
            ax.plot(x_dots_polynomial, y_dots_optimal, label='оптимальные узлы')
        ax.plot(pattern_func_x_dots, pattern_func_y_dots, label='12x^3-8x^2-5x+2')
        ax.legend()
        canvas.draw_idle()

    def calculate_polynomial_from_example_tab(self):
        a, b = list(map(float, self.input_borders.get().split()))
        count = int(self.count_n.get())
        x_dots_uniform = list(map(float, self.input_set_x_ex.get().split()))
        y_dots_uniform = list(map(float, self.input_set_y_ex.get().split()))
        inputed_x = float(self.input_point_x_ex.get())

        x_dots_optimal = calculate_xs_for_optimal_nodes(a, b, count)
        y_dots_optimal = calculate_ys_for_optimal_nodes(count)

        new_x_dots_polynomial, new_y_dots_uniform, new_y_dots_optimal = get_additional_dots(
            x_dots_uniform=x_dots_uniform,
            x_dots_optimal=x_dots_optimal,
            y_dots_optimal=y_dots_optimal,
            y_dots_uniform=y_dots_uniform)
        uniform_nodes = 0
        optimal_nodes = 1

        result_with_optimal = calculate_polynomial(entered_array_xs=x_dots_optimal,
                                                   entered_array_ys=y_dots_optimal,
                                                   point_calculate_value_at=inputed_x,
                                                   calculating_type=optimal_nodes)

        result_with_uniform = calculate_polynomial(entered_array_xs=x_dots_uniform,
                                                   entered_array_ys=y_dots_uniform,
                                                   point_calculate_value_at=inputed_x,
                                                   calculating_type=uniform_nodes)

        create_draw_ex_tab(new_x_dots_polynomial, new_y_dots_uniform, new_y_dots_optimal)

        messagebox.showinfo('Результат', f'Оптимальные узлы P({inputed_x}) = {result_with_optimal}\n'
                                         f'Равномерные узлы P({inputed_x}) = {result_with_uniform}\n'
                                         f'Значение самой функции: {pattern_func(inputed_x)}')
