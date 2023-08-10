#!/usr/bin/env python3
import prompt


ATTEMPT_RATE = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')
    return name


def run_game(qwest, func):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(qwest)
    counter = ATTEMPT_RATE
    while counter > 0:
        qwest_num, result = func()
        print(f'Question: {qwest_num}')
        answer = input('You answer: ')
        if str(answer) != str(result):
            print(f"""{answer} is wrong answer ;(. Correct answer was
 {result}. Let's try again, {name}!""")
            break
        else:
            print('Correct!')
            counter -= 1
    if counter == 0:
        print(f'Congratulations, {name}!')
