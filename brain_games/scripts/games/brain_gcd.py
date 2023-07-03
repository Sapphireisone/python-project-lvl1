#!/usr/bin/env python3
from brain_games.cli import welcome_user
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


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 3
    while i > 0:
        result = make_qwestion()
        answer = input('You answer: ')
        if str(answer) != str(result):
            print(f"""{answer} is wrong answer ;(. Correct answer was
 {result}. Let's try again, {name}!""")
            break
        else:
            print('Correct!')
            i -= 1
    if i == 0:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_gcd()
