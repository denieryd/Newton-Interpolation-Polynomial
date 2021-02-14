<<<<<<< HEAD
import math
import numpy as np
from newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes
from newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes


def get_x_dots_optimal(x0, xn, n):
    """
    get optimal Chebyshev nodes

    :param x0: lower border (a)
    :param xn: upper border (b)
    :param n: count
    :return: list of x dots
    """

    x_dots = []
    for i in range(0, n):
        xi = ((xn + x0) / 2) - ((xn - x0) / 2) * math.cos(math.pi * (2 * i + 1) / (2 * n + 2))
        x_dots.append(xi)
    return x_dots


def get_y_dots_optimal(count):
    """
    gives list of ordinates of optimal Chebyshev nodes for specified x0 and xn (-5, 8)
    :param count: count of terms
    :return: list of ordinates
    """

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
                180.80483335512648]


def calculate_polynomial(x_dots, y_dots, inputed_x, calculating_type):
    """
    return ordinate value of specified x
    :param x_dots: specified x dots
    :param y_dots: specified y dots
    :param inputed_x: dot it needs to calculate in
    :param calculating_type: choosing algorithm
    :return: P(inputed_x)
    """
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


def get_additional_dots(x_dots_uniform, x_dots_optimal, y_dots_uniform, y_dots_optimal):
    """
    agmenting x, y dots to draw smooth graph

    :param x_dots_uniform: x dots to uniform nodes
    :param x_dots_optimal: x dots to optimal nodes
    :param y_dots_uniform: y dots to uniform nodes
    :param y_dots_optimal: y dots to optimal nodes
    :return: augmented 4 list of x, y dots (for uniform and optimal nodes)
    """

    new_y_dots_uniform_nodes = []
    new_y_dots_optimal_nodes = []

    new_x_dots = list(np.linspace(-15, 15, 30))

    for x_dot in new_x_dots:
        res_uniform = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=x_dot,
                                           calculating_type=0)
        res_optimal = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=x_dot,
                                           calculating_type=1)
        new_y_dots_uniform_nodes.append(res_uniform)
        new_y_dots_optimal_nodes.append(res_optimal)

    return new_x_dots, new_y_dots_uniform_nodes, new_y_dots_optimal_nodes
=======
import math
import numpy as np
from newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes
from newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes


def get_x_dots_optimal(x0, xn, n):
    """
    get optimal Chebyshev nodes

    :param x0: lower border (a)
    :param xn: upper border (b)
    :param n: count
    :return: list of x dots
    """

    x_dots = []
    for i in range(0, n):
        xi = ((xn + x0) / 2) - ((xn - x0) / 2) * math.cos(math.pi * (2 * i + 1) / (2 * n + 2))
        x_dots.append(xi)
    return x_dots


def get_y_dots_optimal(count):
    """
    gives list of ordinates of optimal Chebyshev nodes for specified x0 and xn (-5, 8)
    :param count: count of terms
    :return: list of ordinates
    """

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
                180.80483335512648]


def calculate_polynomial(x_dots, y_dots, inputed_x, calculating_type):
    """
    return ordinate value of specified x
    :param x_dots: specified x dots
    :param y_dots: specified y dots
    :param inputed_x: dot it needs to calculate in
    :param calculating_type: choosing algorithm
    :return: P(inputed_x)
    """
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


def get_additional_dots(x_dots_uniform, x_dots_optimal, y_dots_uniform, y_dots_optimal):
    """
    agmenting x, y dots to draw smooth graph

    :param x_dots_uniform: x dots to uniform nodes
    :param x_dots_optimal: x dots to optimal nodes
    :param y_dots_uniform: y dots to uniform nodes
    :param y_dots_optimal: y dots to optimal nodes
    :return: augmented 4 list of x, y dots (for uniform and optimal nodes)
    """

    new_y_dots_uniform_nodes = []
    new_y_dots_optimal_nodes = []

    new_x_dots = list(np.linspace(-15, 15, 30))

    for x_dot in new_x_dots:
        res_uniform = calculate_polynomial(x_dots=x_dots_uniform, y_dots=y_dots_uniform, inputed_x=x_dot,
                                           calculating_type=0)
        res_optimal = calculate_polynomial(x_dots=x_dots_optimal, y_dots=y_dots_optimal, inputed_x=x_dot,
                                           calculating_type=1)
        new_y_dots_uniform_nodes.append(res_uniform)
        new_y_dots_optimal_nodes.append(res_optimal)

    return new_x_dots, new_y_dots_uniform_nodes, new_y_dots_optimal_nodes
>>>>>>> 5a55ef66b279a68dd2145a078146501617883da9
