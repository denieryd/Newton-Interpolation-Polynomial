def calculate_newton_polynomial_optimal_nodes(entered_array_xs, entered_array_ys, point_calculate_value_at):
    # this is algorithm uses newton polynomial for interpolation using optimal nodes
    # this algorithm is not required to understand, because there is math, not programming

    members_polynomial_coefficients = []
    for i in range(len(entered_array_xs)):
        tmp_list = []
        for j in range(len(entered_array_xs)):
            tmp_list.append(None)
        members_polynomial_coefficients.append(tmp_list)

    for i in range(0, len(entered_array_xs)):
        members_polynomial_coefficients[i][0] = entered_array_ys[i]

    for k in range(1, len(entered_array_xs)):
        for i in range(0, len(entered_array_xs) - k):
            members_polynomial_coefficients[i][k] = (members_polynomial_coefficients[i + 1][k - 1] -
                                                     members_polynomial_coefficients[i][k - 1]) / (
                                                            entered_array_xs[i + k] - entered_array_xs[i])

    result_of_using_interpolation_at_the_point = entered_array_ys[0]

    for k in range(1, len(entered_array_xs)):
        r = 1
        for i in range(0, k - 1 + 1):
            r = r * (point_calculate_value_at - entered_array_xs[i])
        result_of_using_interpolation_at_the_point += members_polynomial_coefficients[0][k] * r

    return result_of_using_interpolation_at_the_point
