import math
import numpy as np

from math_algorithm.newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes
from math_algorithm.newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes


def pattern_func(x):
    return 12 * (x ** 3) - 8 * (x ** 2) - 5 * x + 2


def calculate_xs_for_optimal_nodes(x0, xn, n):
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


def calculate_ys_for_optimal_nodes(count):
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


def calculate_polynomial(entered_array_xs, entered_array_ys, point_calculate_value_at, calculating_type):
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    result = None
    if calculating_type == uniform_nodes_type:
        result = calculate_newton_polynomial_uniform_nodes(entered_array_xs=entered_array_xs,
                                                           entered_array_ys=entered_array_ys,
                                                           point_calculate_value_at=point_calculate_value_at)
    elif calculating_type == optimal_nodes_type:
        result = calculate_newton_polynomial_optimal_nodes(entered_array_xs=entered_array_xs,
                                                           entered_array_ys=entered_array_ys,
                                                           point_calculate_value_at=point_calculate_value_at)
    else:
        raise ValueError('calculating_type should be optimal_nodes type or uniform')

    return result


def get_additional_dots(x_dots_uniform, x_dots_optimal, y_dots_uniform, y_dots_optimal):
    uniform_nodes_type = 0
    optimal_nodes_type = 1

    new_y_dots_uniform_nodes = []
    new_y_dots_optimal_nodes = []

    new_x_dots = list(np.linspace(-15, 15, 30))

    for x_dot in new_x_dots:
        res_uniform = calculate_polynomial(entered_array_xs=x_dots_uniform,
                                           entered_array_ys=y_dots_uniform,
                                           point_calculate_value_at=x_dot,
                                           calculating_type=uniform_nodes_type)

        res_optimal = calculate_polynomial(entered_array_xs=x_dots_optimal,
                                           entered_array_ys=y_dots_optimal,
                                           point_calculate_value_at=x_dot,
                                           calculating_type=optimal_nodes_type)
        new_y_dots_uniform_nodes.append(res_uniform)
        new_y_dots_optimal_nodes.append(res_optimal)

    return new_x_dots, new_y_dots_uniform_nodes, new_y_dots_optimal_nodes
