from math import factorial


def calculate_newton_polynomial_uniform_nodes(entered_array_xs, entered_array_ys, point_calculate_value_at):
    # this is algorithm uses newton polynomial for interpolation using optimal nodes
    # this algorithm is not required to understand, because there is math, not programming
    len_of_entered_array = len(entered_array_xs)
    first_elem = 0
    second_elem = 1

    if len_of_entered_array == 1:
        step = entered_array_xs[first_elem]
    else:
        step = entered_array_xs[second_elem] - entered_array_xs[first_elem]

    members_polynomial_coefficients = [entered_array_ys]

    # creating lists[list] to coefficients of finite differences
    for j in range(1, len(entered_array_xs)):
        tmp_list = []
        for v in range(len(entered_array_ys) - j):
            tmp_list.append(1)
        members_polynomial_coefficients.append(tmp_list)

    # calculating finite differences
    for current_list_pointer in range(1, len(members_polynomial_coefficients)):
        for i in range(len(members_polynomial_coefficients[current_list_pointer - 1]) - 1):
            current_coeffs = members_polynomial_coefficients[current_list_pointer - 1]
            new_delta_y = current_coeffs[i + 1] - current_coeffs[i]
            members_polynomial_coefficients[current_list_pointer][i] = new_delta_y

    result_of_using_interpolation_at_the_point = members_polynomial_coefficients[0][0]  # initial y0 value

    # calculating y=f(x) where x is point_calculate_value_at, and y is value of using interpolation at the point
    for i in range(1, len(members_polynomial_coefficients)):
        first_part_term = members_polynomial_coefficients[i][0] / (factorial(i) * (step ** i))
        second_part_term = 1  # (x-x0)(x-x1)...(x-xi)

        for j in range(i):
            second_part_term *= (point_calculate_value_at - entered_array_xs[j])

        result_term = first_part_term * second_part_term
        result_of_using_interpolation_at_the_point += result_term

    return result_of_using_interpolation_at_the_point
