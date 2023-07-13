#!/usr/bin/env python3
from brain_games.engine import main
from brain_games.scripts.scripts import calc


qwest = str('What is the result of the expression?')


if __name__ == '__main__':
    main(qwest, calc)
