import random


DESCRIPTION = str('Find the greatest common divisor of given numbers.')
DIAPASONE_FROM = 1
DIAPASONE_TO = 99


def is_gcd():
    num_1 = random.randint(DIAPASONE_FROM, DIAPASONE_TO)
    num_2 = random.randint(DIAPASONE_FROM, DIAPASONE_TO)
    qwest_text = f'{num_1} {num_2}'
    num = min(num_2, num_1)
    for i in range(1, num+1):
        if num_1 % i == 0 and num_2 % i == 0:
            result = i
        result
    return qwest_text, result
