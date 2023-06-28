#!/usr/bin/env python3
from brain_even import welcome_user
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


def know_name():
    name  = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    if name:
        return name

def game_calc():
    welcome_user()
    name = know_name()
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
        print(f'Congratulations, {name}!')

if __name__ == '__main__':
    game_calc()