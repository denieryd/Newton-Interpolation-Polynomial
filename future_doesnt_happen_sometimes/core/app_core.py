from abc import ABC, abstractmethod

from core.core_app_constants import APPLYING_UNIFORM_NODES_ALGORITHM, APPLYING_OPTIMAL_NODES_ALGORITHM, END_PROGRAM
from core.core_errors import NewtonPolynomialWrongChoiceOfAlgorithm

from languages.russian.messaged_used_in_app import (initial_prompt_to_enter_type_of_algorithm_msg,
                                                    initial_prompt_to_enter_type_of_algorithm_error_msg,
                                                    enter_array_xs_msg,
                                                    enter_array_xy_msg,
                                                    enter_point_calculate_value_at_msg,
                                                    wrong_algorithm_choice_msg,
                                                    program_scheduled_completion_msg)

from math_algorithm.newton_poly_with_optimal_nodes import calculate_newton_polynomial_optimal_nodes
from math_algorithm.newton_poly_with_uniform_nodes import calculate_newton_polynomial_uniform_nodes


class NewtonPolynomialApp(ABC):
    def __init__(self):

        self.calculate_newton_polynomial_optimal_nodes = calculate_newton_polynomial_optimal_nodes
        self.calculate_newton_polynomial_uniform_nodes = calculate_newton_polynomial_uniform_nodes

        self.initial_prompt_to_enter_type_of_algorithm_msg = initial_prompt_to_enter_type_of_algorithm_msg
        self.initial_prompt_to_enter_type_of_algorithm_error_msg = initial_prompt_to_enter_type_of_algorithm_error_msg
        self.enter_array_xs_msg = enter_array_xs_msg
        self.enter_array_xy_msg = enter_array_xy_msg
        self.enter_point_calculate_value_at_msg = enter_point_calculate_value_at_msg
        self.wrong_algorithm_choice_msg = wrong_algorithm_choice_msg

    @abstractmethod
    def get_user_choice_for_algorithm(self):
        return NotImplementedError

    @abstractmethod
    def get_coords_from_user_to_apply_interpolation(self):
        return NotImplementedError

    def calculate_interpolation(self, entered_array_xs, entered_array_ys, point_calculate_value_at, calculating_method):
        if calculating_method == APPLYING_OPTIMAL_NODES_ALGORITHM:
            result_of_using_interpolation_at_the_point = self.calculate_newton_polynomial_optimal_nodes(
                entered_array_xs=entered_array_xs,
                entered_array_ys=entered_array_ys,
                point_calculate_value_at=point_calculate_value_at)

        elif calculating_method == APPLYING_UNIFORM_NODES_ALGORITHM:
            result_of_using_interpolation_at_the_point = self.calculate_newton_polynomial_uniform_nodes(
                entered_array_xs=entered_array_xs,
                entered_array_ys=entered_array_ys,
                point_calculate_value_at=point_calculate_value_at)
        else:
            raise NewtonPolynomialWrongChoiceOfAlgorithm(wrong_algorithm_choice_msg)

        return result_of_using_interpolation_at_the_point

    def main(self):
        while True:
            user_choice = self.get_user_choice_for_algorithm()

            if user_choice in [APPLYING_OPTIMAL_NODES_ALGORITHM, APPLYING_UNIFORM_NODES_ALGORITHM]:
                entered_array_xs, entered_array_ys, point_calculate_value_at = self.get_coords_from_user_to_apply_interpolation()

                result_of_using_interpolation_at_the_point = self.calculate_interpolation(
                    entered_array_xs=entered_array_xs,
                    entered_array_ys=entered_array_ys,
                    point_calculate_value_at=point_calculate_value_at,
                    calculating_method=user_choice)

                output_msg = f'Сумма полинома в точке x = {point_calculate_value_at}' \
                             f' есть y={result_of_using_interpolation_at_the_point}\n' + '=' * 40

                print(output_msg)

            elif user_choice == END_PROGRAM:
                print(program_scheduled_completion_msg)
                break
