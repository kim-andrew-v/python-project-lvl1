#!/usr/bin/env python3

"""Game for calculation."""
import operator
import random

import prompt

positive = ['YES', 'yes', 'Yes']
negative = ['no', 'NO', 'No']
operations = {'*': operator.mul, '-': operator.sub, '+': operator.add}


def main():
    """Brain game for calc main logic."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    correct = 0
    while correct < 3:
        if is_correct():
            correct = correct + 1
            continue
        else:
            print("Let's try again {}".format(name))
            correct = 0
    print('Congratulations, {}!'.format(name))


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
    print(
        "'{}' is wrong answer ;(. Correct answer was '{}'.".
        format(answer, res),
    )
    return False


if __name__ == '__main__':
    main()
