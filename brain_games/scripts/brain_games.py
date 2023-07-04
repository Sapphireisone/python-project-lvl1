#!/usr/bin/env python3

def main():
    print('Welcome to the Brain Games!')
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    else:
        print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
