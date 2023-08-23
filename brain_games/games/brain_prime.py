import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_LOW = 1
NUMBER_MAX = 99


def prime(num):
    counter = 0
    if num == 1:
        result = 'no'
    else:
        for i in range(2, num):
            if num % i == 0:
                counter += 1
                break
        result = 'no' if counter > 0 else 'yes'
    return result


def get_question_and_answer():
    num = random.randint(NUMBER_LOW, NUMBER_MAX)
    qwest_text = f'{num}'
    result = prime(num)
    return qwest_text, result
