#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.scripts.games.brain_progression import progression, qwest_prog


def main():
    run_game(qwest_prog, progression)


if __name__ == '__main__':
    main()
