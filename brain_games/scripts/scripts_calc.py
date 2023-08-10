#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_calc import calc, QWEST_CALC


def main():
    run_game(QWEST_CALC, calc)


if __name__ == '__main__':
    main()
