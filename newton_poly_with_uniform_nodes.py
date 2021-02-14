# creating first newton polynomial
from math import factorial


def calculate_newton_polynomial_uniform_nodes(x_dots, y_dots, inputed_x):
    if len(x_dots) == 1:
        step = x_dots[0]
    else:
        step = x_dots[1] - x_dots[0]

    terms_coeffs = [y_dots]

    # creating lists[list] to coeffs of finite differences
    for j in range(1, len(x_dots)):
        tmp_list = []
        for v in range(len(y_dots) - j):
            tmp_list.append(1)
        terms_coeffs.append(tmp_list)

    # calculating finite differences
    for current_list_pointer in range(1, len(terms_coeffs)):
        for i in range(len(terms_coeffs[current_list_pointer - 1]) - 1):
            current_coeffs = terms_coeffs[current_list_pointer - 1]
            new_delta_y = current_coeffs[i + 1] - current_coeffs[i]
            terms_coeffs[current_list_pointer][i] = new_delta_y

    polynomial_sum = terms_coeffs[0][0]  # initial y0 value

    # calculating y=f(x) at the x inputed
    for i in range(1, len(terms_coeffs)):
        first_part_term = terms_coeffs[i][0] / (factorial(i) * (step ** i))
        second_part_term = 1  # (x-x0)(x-x1)...(x-xi)

        for j in range(i):
            second_part_term *= (inputed_x - x_dots[j])

        result_term = first_part_term * second_part_term
        polynomial_sum += result_term

    return polynomial_sum
