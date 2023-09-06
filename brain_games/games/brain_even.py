import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_LOW = 1
NUMBER_MAX = 99


def get_question_and_answer():
    num = random.randint(NUMBER_LOW, NUMBER_MAX)
    question = f'{num}'
    right_answer = 'yes' if num % 2 == 0 else 'no'
    return question, right_answer
