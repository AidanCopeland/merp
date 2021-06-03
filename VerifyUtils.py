#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import trace_log as trace

sys.path.append('../')


def verify_int_value(value_to_check, default, minimum=-sys.maxint - 1, maximum=sys.maxint):
    """
    Function to check that a StringVar contains a number.
    :param value_to_check: The value to check.
    :param default: The default to apply if a number is not contained.
    :param minimum: The minimum value that is allowed.
    :param maximum: The maximum value that is allowed.
    :return: The value to set.
    """
    try:
        test = int(value_to_check.get())
        if test < minimum:
            trace.flow("Value reset to minimum: %d" % int(minimum))
            value_to_check.set(minimum)
        elif test > maximum:
            trace.flow("Value reset to maximum: %d" % int(maximum))
        else:
            trace.detail("Value set to %d" % test)
    except ValueError:
        value_to_check.set(default)
        trace.detail("Value reset to %d" % int(default))

    pass