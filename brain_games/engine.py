from brain_games.cli import print_qwest, welcome_user, hello_user


def main(qwest):
    hello_user()
    name = welcome_user()
    print_qwest(qwest)
    i = 3
    while i > 0:
        # result = func
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
