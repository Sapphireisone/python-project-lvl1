import random


DESCRIPTION = str('What number is missing in the progression?')
DIAPASONE_FROM = 1
DIAPASONE_TO = 99
PROGRESSION_LENGTH = 10


def make_list(elem, step, length):
    progression = [elem]
    for el in range(1, length):
        elem += step
        progression.append(elem)
    return progression


def find_progress():
    first_element = random.randint(DIAPASONE_FROM, DIAPASONE_TO)
    step = random.randint(DIAPASONE_FROM, DIAPASONE_TO)
    progression = make_list(first_element, step, PROGRESSION_LENGTH)
    some = random.randint(0, 9)
    result = progression[some]
    progression[some] = '..'
    string = ''
    for n in progression:
        a = str(n)
        string = string + a + ' '
    string.strip()
    qwest_text = f'{string}'
    return qwest_text, result
