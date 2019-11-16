def calculate_newton_polynomial_optimal_nodes(x_dots, y_dots, inputed_x):
    terms_coeffs = []
    for i in range(len(x_dots)):
        tmp_list = []
        for j in range(len(x_dots)):
            tmp_list.append(None)
        terms_coeffs.append(tmp_list)

    for i in range(0, len(x_dots)):
        terms_coeffs[i][0] = y_dots[i]

    for k in range(1, len(x_dots)):
        for i in range(0, len(x_dots) - k):
            terms_coeffs[i][k] = (terms_coeffs[i + 1][k - 1] - terms_coeffs[i][k - 1]) / (x_dots[i + k] - x_dots[i])

    polynomial_sum = y_dots[0]

    for k in range(1, len(x_dots)):
        r = 1
        for i in range(0, k - 1 + 1):
            r = r * (inputed_x - x_dots[i])
        polynomial_sum += terms_coeffs[0][k] * r

    return polynomial_sum
