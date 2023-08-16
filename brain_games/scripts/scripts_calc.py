#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_calc import calculate, DESCRIPTION


def main():
    run_game(DESCRIPTION, calculate)


if __name__ == '__main__':
    main()
