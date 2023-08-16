#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_prime import is_prime, DESCRIPTION


def main():
    run_game(DESCRIPTION, is_prime)


if __name__ == '__main__':
    main()
