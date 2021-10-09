from errors import displayError


def arithmetic_arranger(problems, displayAnswer=False):
    if len(problems) > 5:
        return displayError(1)

    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    calcSpace = 4 * ' '

    for problem in problems:
        problem = problem.split()

        if problem[1] != '+' and problem[1] != '-':
            return displayError(2)

        if not problem[0].isdigit() or not problem[2].isdigit():
            return displayError(3)

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return displayError(4)

        maxDigitLength = max(len(problem[0]), len(problem[2]))
        minDigitLength = min(len(problem[0]), len(problem[2]))

        if len(problem[0]) == maxDigitLength:
            space1 = 2
            space2 = maxDigitLength - minDigitLength + 1
        elif len(problem[2]) == maxDigitLength:
            space1 = maxDigitLength - minDigitLength + 2
            space2 = 1
        if len(problem[0]) == len(problem[2]):
            space1 = 2
            space2 = 1

        dashes = maxDigitLength + 2

        row1 += space1 * ' ' + problem[0] + calcSpace
        row2 += problem[1] + space2 * ' ' + problem[2] + calcSpace
        row3 += dashes * '-' + calcSpace

        if displayAnswer and problem[1] == '+':
            answer = str(int(problem[0]) + int(problem[2]))
            space3 = dashes - len(answer)
            row4 += space3 * ' ' + answer + calcSpace
        elif displayAnswer and problem[1] == '-':
            answer = str(int(problem[0]) - int(problem[2]))
            space3 = dashes - len(answer)
            row4 += space3 * ' ' + answer + calcSpace

    arranged_problems = row1.rstrip() + '\n' + row2.rstrip() + '\n' + row3.rstrip()
    if displayAnswer:
        arranged_problems += '\n' + row4.rstrip()

    return arranged_problems
