
# def welcome_user():
#     name = ''
#     while name == '':
#         print('May I have your name? ', end='')
#         name = input()
#     if name:
#         print(f'Hello, {name}!')

import prompt

def welcome_user():
   name = prompt.string('May I have your name? ')
   if name:
      print(f'Hello, {name}!')