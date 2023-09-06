#!/usr/bin/env python3
import prompt


ATTEMPT_RATE = 3


def welcome_user():
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')
    return name


def run_game(qwest_description, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(qwest_description)
    for i in range(ATTEMPT_RATE):
        question, right_answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')
        if str(user_answer) != str(right_answer):
            print(f"""{user_answer} is wrong answer ;(. Correct answer was
 {right_answer}. Let's try again, {name}!""")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
