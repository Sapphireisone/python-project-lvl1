import random


DESCRIPTION = str('What is the result of the expression?')
NUMBER_LOW = 1
NUMBER_MAX = 99


def calculate(x, y, symbol):
    if symbol == '+':
        return x + y
    elif symbol == '-':
        return x - y
    else:
        return x * y


def get_question_and_answer():
    variants_of_symbol = '+-*'
    expression = random.choice(variants_of_symbol)
    num_1 = random.randint(NUMBER_LOW, NUMBER_MAX)
    num_2 = random.randint(NUMBER_LOW, NUMBER_MAX)
    qwest_text = f'{num_1} {expression} {num_2}'
    result = calculate(num_1, num_2, expression)
    return qwest_text, result
