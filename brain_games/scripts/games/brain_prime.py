#!/usr/bin/env python3
from brain_games.cli import welcome_user, hello_user
import random


def find_prime():
    num = random.randint(1, 99)
    print(f'Question: {num}')
    i = 2
    res = 0
    result = ''
    while i < num:
        if num % i != 0:
            i += 1
        else:
            res += 1
            break
    if res > 0:
        result = 'No'
    else:
        result = 'Yes'
    return result


def main():
    hello_user()
    name = welcome_user()
    print('What is the result of the expression?')
    i = 3
    while i > 0:
        result = find_prime()
        answer = input('You answer: ')
        if str(answer.lower()) != str(result.lower()):
            print(f"""{answer} is wrong answer ;(. Correct answer was
 {result}. Let's try again, {name}!""")
            break
        else:
            print('Correct!')
            i -= 1
    if i == 0:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
