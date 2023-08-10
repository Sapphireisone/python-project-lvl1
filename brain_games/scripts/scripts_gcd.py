#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_gcd import gcd, QWEST_GCD


def main():
    run_game(QWEST_GCD, gcd)


if __name__ == '__main__':
    main()