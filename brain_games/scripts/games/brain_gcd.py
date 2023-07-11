#!/usr/bin/env python3
from brain_games.engine import main
import random


def make_qwestion():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    print(f'Question: {num1} {num2}')
    num = 0
    if num1 > num2:
        num = num2
    else:
        num = num1
    i = 1
    result = 1
    while i <= num:
        if num1 % i == 0 and num2 % i == 0:
            result = i
            i += 1
        else:
            result
            i += 1
    return result


qwest = str('Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main(qwest, make_qwestion())
