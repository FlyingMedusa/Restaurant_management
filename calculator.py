expression = ""


def press(num, equation):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress(equation):
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:

        equation.set(" error ")
        expression = ""


def clear(equation):
    global expression
    expression = ""
    equation.set("")