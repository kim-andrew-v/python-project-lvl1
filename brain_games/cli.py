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


def congrats(username):
    """Congrats user.

    Args:
        username: string username
    """
    print('Congratulations, {}!'.format(username))


def your_answer_is_wrong(user_answer, correct_answer):
    """Print notice about wrong answer.

    Args:
        user_answer: answer that user enters
        correct_answer: answer that is correct
    """
    print(
        "'{}' is wrong answer ;(. Correct answer was '{}'.".
        format(user_answer, correct_answer),
    )
