import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
DIAPASONE_FROM = 1
DIAPASONE_TO = 99


def is_even():
    num = random.randint(DIAPASONE_FROM, DIAPASONE_TO)
    qwest_text = f'{num}'
    right_answer = 'yes' if num % 2 == 0 else 'no'
    return qwest_text, right_answer
