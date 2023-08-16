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
    count = 0
    for i in range(ATTEMPT_RATE):
        qwest_text, result = func()
        print(f'Question: {qwest_text}')
        answer = input('You answer: ')
        if str(answer) != str(result):
            print(f"""{answer} is wrong answer ;(. Correct answer was
 {result}. Let's try again, {name}!""")
            break
        else:
            print('Correct!')
            count += 1
            if count == ATTEMPT_RATE:
                print(f'Congratulations, {name}!')
