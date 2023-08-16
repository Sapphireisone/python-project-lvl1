import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
DIAPASONE_FROM = 1
DIAPASONE_TO = 99


def is_prime():
    num = random.randint(DIAPASONE_FROM, DIAPASONE_TO)
    qwest_text = f'{num}'
    counter = 0
    if num == 1:
        result = 'no'
    else:
        for i in range(2, num):
            if num % i == 0:
                counter += 1
                break
        result = 'no' if counter > 0 else 'yes'
    return qwest_text, result
