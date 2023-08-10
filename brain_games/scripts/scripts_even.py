#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_even import even, QWEST_EVEN


def main():
    run_game(QWEST_EVEN, even)


if __name__ == '__main__':
    main()
