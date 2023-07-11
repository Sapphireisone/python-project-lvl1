#!/usr/bin/env python3
from brain_games.engine import main
import random


def find_prime():
    num = random.randint(1, 99)
    print(f'Question: {num}')
    result = ''
    if num == 1:
        result = 'no'
    elif num == 2:
        result = 'yes'
    else:
        i = 2
        res = 0
        while i < num:
            if num % i != 0:
                i += 1
            else:
                res += 1
                break
        if res > 0:
            result = 'no'
        else:
            result = 'yes'
    return result


qwest = str('Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main(qwest, find_prime())
