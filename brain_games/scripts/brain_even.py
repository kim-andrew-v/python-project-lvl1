#!/usr/bin/env python3

"""Game for odd vs even."""
import random

import prompt

positive = ['YES', 'yes', 'Yes']
negative = ['no', 'NO', 'No']


def main():
    """Brain game for odd even main logic."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 0
    while correct < 3:
        if is_even():
            correct = correct + 1
            continue
        else:
            print("Let's try again {}".format(name))
            correct = 0
    print('Congratulations, {}!'.format(name))


def is_even():
    """Count if number is even or odd.

    :returns:
        bool
    """
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
    print(
        "'{}' is wrong answer ;(. Correct answer was '{}'.".
        format(answer, opposite),
    )
    return False


if __name__ == '__main__':
    main()
