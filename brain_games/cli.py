"""cli.py created to welcome users via command line interface."""
import prompt


def welcome_user():
    """Asking user a name, and then does hello."""
    name = prompt.string('May I have your name?')
    print('Hello {}'.format(name))
