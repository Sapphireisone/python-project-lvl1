import random


DESCRIPTION = str('Find the greatest common divisor of given numbers.')
NUMBER_LOW = 1
NUMBER_MAX = 99


def gcd(num, num_1, num_2):
    for i in range(1, num + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            result = i
    return result


def get_question_and_answer():
    num_1 = random.randint(NUMBER_LOW, NUMBER_MAX)
    num_2 = random.randint(NUMBER_LOW, NUMBER_MAX)
    question = f'{num_1} {num_2}'
    num = min(num_2, num_1)
    right_answer = gcd(num, num_1, num_2)
    return question, right_answer
