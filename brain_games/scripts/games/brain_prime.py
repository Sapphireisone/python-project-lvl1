import random


qwest_prime = str('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    num = random.randint(1, 99)
    print(f'Question: {num}')
    result = ''
    if num == 1:
        result = 'no'
    elif num == 2:
        result = 'yes'
    else:
        i = 2
        res = 0
        while i < num:
            if num % i != 0:
                i += 1
            else:
                res += 1
                break
        if res > 0:
            result = 'no'
        else:
            result = 'yes'
    return result
