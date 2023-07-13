#!/usr/bin/env python3
from brain_games.engine import main
from brain_games.scripts.scripts import prime


qwest = str('Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main(qwest, prime)
