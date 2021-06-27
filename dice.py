from builtins import range
import random
import os
import trace_log as trace


def randomize():
    rand_seed = os.urandom(256)
    random.seed(rand_seed)


def d100():
    roll = random.randint(1, 100)
    trace.detail("Roll was %d" % roll)
    return roll


def d10():
    roll = random.randint(1, 10)
    trace.detail("Roll was %d" % roll)
    return roll


def d100high():
    total_roll = 0
    while True:
        roll = d100()
        total_roll += roll
        if roll < 96:
            break
    trace.detail("Roll was %d" % total_roll)
    return total_roll


def d100open():
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
    roll = random.randint(1, 1000)
    trace.detail("Roll was %d" % roll)
    return roll


def dcustom(dice_value, num_dice=1):
    total_roll = 0
    for i in range(0, num_dice):
        roll = random.randint(1, dice_value)
        total_roll += roll
        trace.detail("Individual roll was %d, total %d" % (roll, total_roll))
    trace.detail("Roll was %d" % total_roll)
    return total_roll
