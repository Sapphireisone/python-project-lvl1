#!/usr/bin/env python3
import random


def calc():
    letter = '+-*'
    symbol = random.choices(letter)
    symbol = symbol[0]
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    print(f'Question: {num1} {symbol} {num2}')
    if symbol == '+':
        result = num1 + num2
    elif symbol == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return result


def gcd():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    print(f'Question: {num1} {num2}')
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
    return result


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
    print(f'Question: {string}')
    return result


def even():
    num = random.randint(1, 99)
    print(f'Question: {num}')
    right_answer = ''
    if num % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
