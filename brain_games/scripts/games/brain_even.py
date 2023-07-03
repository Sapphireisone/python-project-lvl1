#!/usr/bin/env python3
from brain_games.cli import welcome_user
import random


def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 3
    while i > 0:
        num = random.randint(1, 99)
        print(f'Question: {num}')
        answer = input('You answer: ')
        if num % 2 == 0 and answer != 'yes':
            right_answer = 'yes'
            print(f"""{answer} is wrong answer ;(. Correct answer was
 {right_answer}. Let's try again, {name}!""")
            break
        elif num % 2 != 0 and answer != 'no':
            right_answer = 'no'
            print(f"""{answer} is wrong answer ;(. Correct answer was
 {right_answer}. Let's try again, {name}!""")
            break
        else:
            print('Correct!')
            i -= 1
    if i == 0:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    game_even()
