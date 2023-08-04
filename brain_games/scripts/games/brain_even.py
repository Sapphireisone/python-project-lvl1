import random


def even():
    num = random.randint(1, 99)
    print(f'Question: {num}')
    right_answer = ''
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer


qwest_even = 'Answer "yes" if the number is even, otherwise answer "no".'
