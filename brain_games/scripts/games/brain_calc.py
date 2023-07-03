#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.cli import hello_user
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


def main():
    hello_user()
    name = welcome_user()
    print('What is the result of the expression?')
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
    main()
