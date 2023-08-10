#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_prime import prime, QWEST_PRIME


def main():
    run_game(QWEST_PRIME, prime)


if __name__ == '__main__':
    main()
