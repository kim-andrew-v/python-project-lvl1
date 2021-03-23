#!/usr/bin/env python3

"""Game - find missing piece of progression."""
from brain_games import cli, game_logic


def main():
    """Brain game for missing piece of progression."""
    cli.welcome()
    name = cli.get_name()
    print('What number is missing in the progression?')
    game_logic.logic('progr', name)


if __name__ == '__main__':
    main()
