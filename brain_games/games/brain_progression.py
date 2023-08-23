import random


DESCRIPTION = str('What number is missing in the progression?')
NUMBER_LOW = 1
NUMBER_MAX = 99
PROGRESSION_LENGTH = 10


def make_list(elem, step, length):
    progression = [str(elem)]
    for el in range(1, length):
        elem += step
        progression.append(str(elem))
    return progression


def get_question_and_answer():
    first_element = random.randint(NUMBER_LOW, NUMBER_MAX)
    step = random.randint(NUMBER_LOW, NUMBER_MAX)
    progression = make_list(first_element, step, PROGRESSION_LENGTH)
    some = random.randint(0, PROGRESSION_LENGTH)
    result = int(progression[some])
    progression[some] = '..'
    qwest_text = " ".join(progression)
    return qwest_text, result
