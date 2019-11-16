from newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes
from newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes


def get_user_choice():
    while True:
        try:
            user_choice = int(input('1.Посчитать сумму через оптимальные узлы\n'
                                    '2.Посчитать сумму через равномерные узлы\n'
                                    '3.Завершить программу\n'
                                    '>>>: '))
            if user_choice not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print('Ошибка. Повторите ввод')

    return user_choice


def get_coords():
    x_dots = list(map(float, input('Введите x через пробел: ').split()))
    y_dots = list(map(float, input('Введите y через пробел: ').split()))
    inputed_x = float(input('Введите икс точки, в которой требуется посчитать значение полинома: '))

    return x_dots, y_dots, inputed_x


def main():
    while True:
        user_choice = get_user_choice()

        if user_choice != 3:
            x_dots, y_dots, inputed_x = get_coords()

            if user_choice == 1:
                polynomial_sum = calculate_newton_polynomial_optimal_nodes(x_dots=x_dots, y_dots=y_dots,
                                                                           inputed_x=inputed_x)
                print(f'Сумма полиному в точке x = {inputed_x} есть y={polynomial_sum}\n' + '='*40)

            elif user_choice == 2:
                polynomial_sum = calculate_newton_polynomial_uniform_nodes(x_dots=x_dots, y_dots=y_dots,
                                                                           inputed_x=inputed_x)
                print(f'Сумма полинома в точке х={inputed_x} есть у={polynomial_sum}\n' + '='*40)
        if user_choice == 3:
            print('Программа завершена.')
            break


main()
