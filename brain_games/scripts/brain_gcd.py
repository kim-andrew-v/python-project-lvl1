#!/usr/bin/env python3

"""Game for greatest common divider."""
from brain_games import cli, game_logic


def main():
    """Brain game for common divider."""
    cli.welcome()
    name = cli.get_name()
    print('Find the greatest common divisor of given numbers.')
    game_logic.logic('gcd', name)


if __name__ == '__main__':
    main()
