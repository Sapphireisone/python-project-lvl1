#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.scripts.games.brain_gcd import gcd, qwest_gcd


def main():
    run_game(qwest_gcd, gcd)


if __name__ == '__main__':
    main()
