def check_validate_data(x_dots, y_dots, inputed_x):
    try:
        x_dots = list(map(float, x_dots))
        if len(x_dots) == 0:
            raise ValueError

    except ValueError:
        return True, 'Множество Х должно содержать только числа и не должно быть пустым'
    try:
        y_dots = list(map(float, y_dots))
        if len(y_dots) == 0:
            raise ValueError

    except ValueError:
        return True, 'Множество Y должно содержать только числа и не должно быть пустым'
    try:
        if len(inputed_x) == 0:
            raise ValueError
        inputed = float(inputed_x)
    except ValueError:
        return True, 'Координата точки по Х должна быть числом'

    return False, 'validated'