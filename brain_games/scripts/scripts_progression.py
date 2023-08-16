#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_progression import find_progress, DESCRIPTION


def main():
    run_game(DESCRIPTION, find_progress)


if __name__ == '__main__':
    main()
