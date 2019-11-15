# creating first newton polynomial
from math import factorial

x_dots = [-0.5, 0, 0.5, 1]
y_dots = [1, 2, -1, 1]

coef_y = []
for j in range(len(x_dots)):
    if j == 0:
        coef_y.append(y_dots)
    else:
        tmp_list = []
        for v in range(len(y_dots) - j):
            tmp_list.append(1)
        coef_y.append(tmp_list)

print(coef_y)

step = 0.5

for current_list_pointer in range(1, len(coef_y)):
    for i in range(len(coef_y[current_list_pointer - 1]) - 1):
        current_coeffs = coef_y[current_list_pointer - 1]
        new_delta_y = current_coeffs[i + 1] - current_coeffs[i]
        coef_y[current_list_pointer][i] = new_delta_y
        print(new_delta_y)

print(coef_y)

for i in range(len(coef_y)):
    print(coef_y[i][0])


def calculate_polynomial():
    inputed_x = float(input('Введите x: '))
    polynomial_sum = 0

    for i in range(0, len(coef_y)):
        if i == 0:
            polynomial_sum += coef_y[i][0]  # [0][0]
        else:
            first_part_term = coef_y[i][0] / (factorial(i) * (step ** i))
            second_part_term = 1  # product should be here
            for j in range(i):
                second_part_term *= (inputed_x - x_dots[j])
            result_term = first_part_term * second_part_term
            polynomial_sum += result_term

    print(polynomial_sum)
    print(12* (inputed_x**3) - 8 * (inputed_x ** 2) - 5* inputed_x + 2)



calculate_polynomial()
