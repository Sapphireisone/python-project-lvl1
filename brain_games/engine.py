#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')
    return name


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(qwest)
    i = 3
    while i > 0:
        result = func()
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
