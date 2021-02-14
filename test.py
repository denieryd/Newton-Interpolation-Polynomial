<<<<<<< HEAD
import math
from tools import get_x_dots_optimal


def get_x_s(x0, xn, n):
    x_dots = []
    for i in range(n):
        xi = (x0 + xn) / 2 + (x0 - xn) / 2 * math.cos((2 * i + 1) / (2 * n + 2) * math.pi)
        x_dots.append(xi)
    return x_dots

# print(get_x(1, 10, 10))
# print(get_x_dots_optimal(1, 10, 10))
=======
import math
from tools import get_x_dots_optimal


def get_x_s(x0, xn, n):
    x_dots = []
    for i in range(n):
        xi = (x0 + xn) / 2 + (x0 - xn) / 2 * math.cos((2 * i + 1) / (2 * n + 2) * math.pi)
        x_dots.append(xi)
    return x_dots

# print(get_x(1, 10, 10))
# print(get_x_dots_optimal(1, 10, 10))
>>>>>>> 5a55ef66b279a68dd2145a078146501617883da9
