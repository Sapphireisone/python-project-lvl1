#!/usr/bin/env python3
from brain_games.engine import main
import random


def find_element():
    diff = random.randint(1, 99)
    element = random.randint(1, 99)
    lis = [element]
    i = 1
    while i < 10:
        element += diff
        lis.append(element)
        i += 1
    some = random.randint(0, 9)
    result = lis[some]
    lis[some] = '..'
    string = ''
    for n in lis:
        a = str(n)
        string = string + a + ' '
    string.strip()
    print(f'Question: {string}')
    return result


qwest = str('What number is missing in the progression?')


if __name__ == '__main__':
    main(qwest, find_element())
