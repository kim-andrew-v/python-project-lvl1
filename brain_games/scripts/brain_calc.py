#!/usr/bin/env python3

"""Game for calculation."""
from brain_games import cli, game_logic


def main():
    """Brain game for calc main logic."""
    cli.welcome()
    name = cli.get_name()
    print('What is the result of the expression?')
    game_logic.logic('calc', name)


if __name__ == '__main__':
    main()
