#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.scripts.games.brain_progression import progression, qwest_progression


def main():
    run_game(qwest_progression, progression)


if __name__ == '__main__':
    main()
