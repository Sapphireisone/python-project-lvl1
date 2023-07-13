#!/usr/bin/env python3
from brain_games.engine import main
from brain_games.scripts.scripts import progression


qwest = str('What number is missing in the progression?')


if __name__ == '__main__':
    main(qwest, progression)
