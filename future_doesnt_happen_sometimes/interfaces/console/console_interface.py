from math_algorithm.newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes
from math_algorithm.newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes
from core.core_gate import NewtonPolynomialWrongChoiceOfAlgorithm

from core.core_app_constants import APPLYING_OPTIMAL_NODES_ALGORITHM, APPLYING_UNIFORM_NODES_ALGORITHM, END_PROGRAM

from languages.russian.messaged_used_in_app import (initial_prompt_to_enter_type_of_algorithm_msg,
                                                    initial_prompt_to_enter_type_of_algorithm_error_msg,
                                                    enter_array_xs_msg,
                                                    enter_array_xy_msg,
                                                    enter_point_calculate_value_at_msg,
                                                    wrong_algorithm_choice_msg)


def get_user_choice_for_algorithm():
    while True:
        try:
            user_choice = int(input(initial_prompt_to_enter_type_of_algorithm_msg))
            if user_choice not in [APPLYING_OPTIMAL_NODES_ALGORITHM, APPLYING_UNIFORM_NODES_ALGORITHM, END_PROGRAM]:
                raise ValueError
            break
        except ValueError:
            print(initial_prompt_to_enter_type_of_algorithm_error_msg)

    return user_choice


def get_coords_from_user_to_apply_interpolation():
    entered_array_xs = list(map(float, input(enter_array_xs_msg).split()))
    entered_array_ys = list(map(float, input(enter_array_xy_msg).split()))
    point_calculate_value_at = float(input(enter_point_calculate_value_at_msg))

    return entered_array_xs, entered_array_ys, point_calculate_value_at


def calculate_interpolation(entered_array_xs, entered_array_ys, point_calculate_value_at, calculating_method):
    if calculating_method == APPLYING_OPTIMAL_NODES_ALGORITHM:
        result_of_using_interpolation_at_the_point = calculate_newton_polynomial_optimal_nodes(
            entered_array_xs=entered_array_xs,
            entered_array_ys=entered_array_ys,
            point_calculate_value_at=point_calculate_value_at)

    elif calculating_method == APPLYING_UNIFORM_NODES_ALGORITHM:
        result_of_using_interpolation_at_the_point = calculate_newton_polynomial_uniform_nodes(
            entered_array_xs=entered_array_xs,
            entered_array_ys=entered_array_ys,
            point_calculate_value_at=point_calculate_value_at)
    else:
        raise NewtonPolynomialWrongChoiceOfAlgorithm(wrong_algorithm_choice_msg)

    return result_of_using_interpolation_at_the_point


def main():
    while True:
        user_choice = get_user_choice_for_algorithm()

        if user_choice in [APPLYING_OPTIMAL_NODES_ALGORITHM, APPLYING_UNIFORM_NODES_ALGORITHM]:
            entered_array_xs, entered_array_ys, point_calculate_value_at = get_coords_from_user_to_apply_interpolation()

            result_of_using_interpolation_at_the_point = calculate_interpolation(
                entered_array_xs=entered_array_xs,
                entered_array_ys=entered_array_ys,
                point_calculate_value_at=point_calculate_value_at,
                calculating_method=user_choice)

            output_msg = f'Сумма полинома в точке x = {point_calculate_value_at}' \
                         f' есть y={result_of_using_interpolation_at_the_point}\n' + '=' * 40

            print(output_msg)

        if user_choice == 3:
            print('Программа завершена.')
            break

