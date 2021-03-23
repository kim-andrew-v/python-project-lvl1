"""cli.py created to welcome users via command line interface."""
import prompt


def welcome():
    """Welcome new user."""
    print('Welcome to the Brain Games!')


def get_name():
    """Asking player a name, and then does hello."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
