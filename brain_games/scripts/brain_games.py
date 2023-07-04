#!/usr/bin/env python3
import prompt


def main():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')
    return name


if __name__ == '__main__':
    main()
    welcome_user()
