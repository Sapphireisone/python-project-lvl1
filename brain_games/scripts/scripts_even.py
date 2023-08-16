#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_even import is_even, DESCRIPTION


def main():
    run_game(DESCRIPTION, is_even)


if __name__ == '__main__':
    main()
