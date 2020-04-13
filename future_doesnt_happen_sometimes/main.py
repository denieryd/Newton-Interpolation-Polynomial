from core.app_core import NewtonPolynomialApp

import interfaces.console.console_interface as console_interface


class ConsoleApp(NewtonPolynomialApp):
    def __init__(self):
        super().__init__()

    def get_user_choice_for_algorithm(self):
        return console_interface.get_user_choice_for_algorithm()

    def get_coords_from_user_to_apply_interpolation(self):
        return console_interface.get_coords_from_user_to_apply_interpolation()

    def main(self):
        super().main()


c = ConsoleApp()
c.main()
