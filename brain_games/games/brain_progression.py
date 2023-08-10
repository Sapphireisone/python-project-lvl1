import random


QWEST_PROGR = str('What number is missing in the progression?')


def progression():
    diff = random.randint(1, 99)
    element = random.randint(1, 99)
    lis = [element]
    i = 1
    while i < 10:
        element += diff
        lis.append(element)
        i += 1
    some = random.randint(0, 9)
    result = lis[some]
    lis[some] = '..'
    string = ''
    for n in lis:
        a = str(n)
        string = string + a + ' '
    string.strip()
    qwest_num = f'{string}'
    return qwest_num, result
