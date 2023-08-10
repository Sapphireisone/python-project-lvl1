import random


QWEST_GCD = str('Find the greatest common divisor of given numbers.')


def gcd():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    qwest_num = f'{num1} {num2}'
    num = 0
    if num1 > num2:
        num = num2
    else:
        num = num1
    i = 1
    result = 1
    while i <= num:
        if num1 % i == 0 and num2 % i == 0:
            result = i
            i += 1
        else:
            result
            i += 1
    return qwest_num, result
