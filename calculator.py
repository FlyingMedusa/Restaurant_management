expression = ""


def key(elem, equation):
    global expression
    expression = expression + str(elem)
    equation.set(expression)


def equal_key(equation):
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear_key(equation):
    global expression
    equation.set("")
    expression = ""