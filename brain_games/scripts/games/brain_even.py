#!/usr/bin/env python3
from brain_games.engine import main
from brain_games.scripts.scripts import even


qwest = str('Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main(qwest, even)
