#!/usr/bin/env python3
from brain_games.engine import main
from brain_games.scripts.scripts import gcd


qwest = str('Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main(qwest, gcd)
