#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.scripts.games.brain_calc import calc, qwest_calc


def main():
    run_game(qwest_calc, calc)


if __name__ == '__main__':
    main()
