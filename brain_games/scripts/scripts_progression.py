#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_progression import progression, QWEST_PROGR


def main():
    run_game(QWEST_PROGR, progression)


if __name__ == '__main__':
    main()
