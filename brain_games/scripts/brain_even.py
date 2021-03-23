#!/usr/bin/env python3

"""Game for odd vs even."""
from brain_games import cli, game_logic


def main():
    """Brain game for odd even main logic."""
    cli.welcome()
    name = cli.get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_logic.logic('even', name)


if __name__ == '__main__':
    main()
