#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.scripts.games.brain_prime import prime, qwest_prime


def main():
    run_game(qwest_prime, prime)


if __name__ == '__main__':
    main()
