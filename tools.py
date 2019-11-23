import math


def get_x_dots_optimal(x0, xn, n):
    x_dots = []
    for i in range(0, n):
        xi = ((xn + x0) / 2) - ((xn - x0) / 2) * math.cos(math.pi * (2 * i + 1) / (2 * n + 2))
        x_dots.append(xi)
    return x_dots
