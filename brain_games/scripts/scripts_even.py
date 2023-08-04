#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.scripts.games.brain_even import even, qwest_even


def main():
    run_game(qwest_even, even)


if __name__ == '__main__':
    main()
