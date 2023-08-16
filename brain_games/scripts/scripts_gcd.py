#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_gcd import is_gcd, DESCRIPTION


def main():
    run_game(DESCRIPTION, is_gcd)


if __name__ == '__main__':
    main()
