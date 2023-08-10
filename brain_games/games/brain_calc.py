import random


QWEST_CALC = str('What is the result of the expression?')


def calc():
    letter = '+-*'
    symbol = random.choices(letter)
    symbol = symbol[0]
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    qwest_num = f'{num1} {symbol} {num2}'
    if symbol == '+':
        result = num1 + num2
    elif symbol == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return qwest_num, result
