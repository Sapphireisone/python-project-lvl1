#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.brain_progression import get_question_and_answer, \
    DESCRIPTION


def main():
    run_game(DESCRIPTION, get_question_and_answer)


if __name__ == '__main__':
    main()
