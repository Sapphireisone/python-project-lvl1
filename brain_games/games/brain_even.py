import random


QWEST_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    num = random.randint(1, 99)
    qwest_num = f'{num}'
    right_answer = ''
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return qwest_num, right_answer
