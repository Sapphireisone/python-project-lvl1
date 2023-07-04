#!/usr/bin/env python3
from brain_games.cli import welcome_user, hello_user
import random


def find_prime():
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
        if res > 0:
            result = 'no'
        else:
            result = 'yes'
    return result


def main():
    hello_user()
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 30
    while i > 0:
        result = find_prime()
        answer = input('You answer: ')
        if str(answer) != str(result):
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
