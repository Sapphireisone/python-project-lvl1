#!/usr/bin/env python3
from brain_games.engine import main
import random


def make_qwestion():
    letter = '+-*'
    symbol = random.choices(letter)
    symbol = symbol[0]
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    print(f'Question: {num1} {symbol} {num2}')
    if symbol == '+':
        result = num1 + num2
    elif symbol == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return result


qwestion = str('What is the result of the expression?')


if __name__ == '__main__':
    main(qwestion, make_qwestion())
