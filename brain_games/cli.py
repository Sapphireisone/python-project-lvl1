import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')


def welcome_user():
    print('Welcome to the Brain Games!')


def know_name():
    name = ''
    while name == '':
        print('May I have your name? ', end='')
        name = input()
    if name:
        return name
