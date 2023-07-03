#!/usr/bin/env python3
from brain_games.cli import welcome_user
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


def game_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    i = 3
    while i > 0:
        result = find_element()
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
    game_progression()
