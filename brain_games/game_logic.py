"""Game logic."""
import operator
import random
import sys

import prompt

from brain_games import cli

positive = ['YES', 'yes', 'Yes']
negative = ['no', 'NO', 'No']
operations = {'*': operator.mul, '-': operator.sub, '+': operator.add}


def logic(game, username):
    """Loop logic for 3 right consequent answers.

    Args:
        game: string type of game
        username: string username
    """
    func = ''
    if game == 'calc':
        func = 'is_correct'
    elif game == 'even':
        func = 'is_even'
    elif game == 'gcd':
        func = 'is_gcd'
    correct = 0
    my_func = getattr(sys.modules[__name__], func)
    while correct < 3:
        if my_func():
            correct = correct + 1
            continue
        else:
            print("Let's try again {}".format(username))
            correct = 0
    cli.congrats(username)


def is_even():
    """Count if number is even or odd."""
    number = random.randint(1, 100)
    answer = prompt.string('Question: {} '.format(number))
    if answer in positive:
        opposite = random.choice(negative)
    else:
        opposite = random.choice(positive)
    print('Your answer: {}'.format(answer))
    if number % 2 == 0 and answer in positive:
        print('Correct!')
        return True
    elif number % 2 != 0 and answer in negative:
        print('Correct!')
        return True
    cli.your_answer_is_wrong(answer, opposite)
    return False


def is_correct():
    """Return if answer is correct result."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    oper = random.choice(list(operations.keys()))
    res = operations[oper](num1, num2)
    answer = prompt.string(
        'Question: {} '.
        format(str(num1) + ' ' + oper + ' ' + str(num2)),
    )
    print('Your answer: {}'.format(answer))
    if res == int(answer):
        print('Correct!')
        return True
    cli.your_answer_is_wrong(answer, res)
    return False


def is_gcd():
    """Return if gcd is correct."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    gcd = 1
    biggest = num2 if num2 > num1 else num1
    for iterable in range(2, biggest + 1):
        if num1 % iterable == 0 and num2 % iterable == 0:
            gcd = iterable
    answer = prompt.string(
        'Question: {} '.
        format(str(num1) + ' ' + str(num2) + ' '),
    )
    print('Your answer: {}'.format(answer))
    if gcd == int(answer):
        print('Correct!')
        return True
    cli.your_answer_is_wrong(answer, gcd)
    return False
