import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_LOW = 1
NUMBER_MAX = 99


def prime(num):
    counter = 0
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                counter += 1
                break
    return False if counter > 0 else True


def get_question_and_answer():
    num = random.randint(NUMBER_LOW, NUMBER_MAX)
    question = f'{num}'
    if prime(num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
