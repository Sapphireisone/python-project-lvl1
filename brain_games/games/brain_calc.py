import random


DESCRIPTION = str('What is the result of the expression?')
DIAPASONE_FROM = 1
DIAPASONE_TO = 99


def count(x, y, symbol):
    if symbol == '+':
        result = x + y
    elif symbol == '-':
        result = x - y
    else:
        result = x * y
    return result


def calculate():
    variants_of_symbol = '+-*'
    expression = random.choice(variants_of_symbol)
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    qwest_text = f'{num_1} {expression} {num_2}'
    result = count(num_1, num_2, expression)
    return qwest_text, result
