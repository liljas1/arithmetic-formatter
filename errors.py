def displayError(error):
    if error == 1:
        return "Error: Too many problems."
    elif error == 2:
        return "Error: Operator must be '+' or '-'."
    elif error == 3:
        return "Error: Numbers must only contain digits."
    else:
        return "Error: Numbers cannot be more than four digits."
