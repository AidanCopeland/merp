"""
Dice utility functions.

Functions:
    randomize()
    d100()
    d10()
    d100high()
    d100open()
    d1000()
    dcustom(dice_value, num_dice=1)
"""
from builtins import range
import random
import os
import trace_log as trace


def randomize():
    """
    Randomize the random number generator
    :return:
    """
    rand_seed = os.urandom(256)
    random.seed(rand_seed)


def d100():
    """
    Roll dice to return a random result between 1 and 100.
    :return: The result of the dice roll.
    """
    roll = random.randint(1, 100)
    trace.detail("Roll was %d" % roll)
    return roll


def d10():
    """
    Roll dice to return a random result between 1 and 10.
    :return: The result of the dice roll.
    """
    roll = random.randint(1, 10)
    trace.detail("Roll was %d" % roll)
    return roll


def d100high():
    """
    Roll dice to return an open-ended high d100 result.
    :return: The result of the dice roll.
    """
    total_roll = 0
    while True:
        roll = d100()
        total_roll += roll
        if roll < 96:
            break
    trace.detail("Roll was %d" % total_roll)
    return total_roll


def d100open():
    """
    Roll dice to return an open-ended d100 result.
    :return: The result of the dice roll.
    """
    roll = d100()
    if roll > 95:
        roll_up_roll = d100high()
        total_roll = roll + roll_up_roll
    elif roll < 6:
        roll_down_roll = d100high()
        total_roll = roll - roll_down_roll
    else:
        total_roll = roll
    trace.detail("Roll was %d" % total_roll)
    return total_roll


def d1000():
    """
    Roll dice to generate a random number between 1 and 1000
    :return: The result of the dice.
    """
    roll = random.randint(1, 1000)
    trace.detail("Roll was %d" % roll)
    return roll


def dcustom(dice_value, num_dice=1):
    """
    Roll a specified number of dice with a specified value.
    :param dice_value: The maximum value of each die.
    :param num_dice: The number of dice to roll.
    :return: The summed total of the dice.
    """
    total_roll = 0
    for _ in range(0, num_dice):
        roll = random.randint(1, dice_value)
        total_roll += roll
        trace.detail("Individual roll was %d, total %d" % (roll, total_roll))
    trace.detail("Roll was %d" % total_roll)
    return total_roll
