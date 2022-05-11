#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sanity checking functions.

Functions:
    verify_int_value(value_to_check, minimum=-sys.maxsize - 1, maximum=sys.maxsize)
"""
import sys

import trace_log as trace

sys.path.append('../')


def verify_int_value(value_to_check, default, minimum=-sys.maxsize - 1, maximum=sys.maxsize):
    """
    Function to check that a StringVar contains a number.
    :param value_to_check: The value to check.
    :param default: The default to apply if a number is not contained.
    :param minimum: The minimum value that is allowed.
    :param maximum: The maximum value that is allowed.
    :return: The value to set.
    """
    try:
        trace.flow("Value is %r" % value_to_check.get())
        verify_minimum_maximum(value_to_check, minimum, maximum)
    except ValueError:
        value_to_check.set(default)
        trace.detail("Value reset to %d" % int(default))


def verify_int_value_or_empty(value_to_check, default, minimum=-sys.maxsize - 1, maximum=sys.maxsize):
    """
    Function to check that a StringVar contains a number or an empty string.
    :param value_to_check: The value to check.
    :param default: The default to apply if an illegal value is present.
    :param minimum: The minimum value that is allowed.
    :param maximum: The maximum value that is allowed.
    :return: The value to set.
    """
    if value_to_check.get() != '':
        try:
            trace.flow("Value is %r" % value_to_check.get())
            verify_minimum_maximum(value_to_check, minimum, maximum)
        except ValueError:
            value_to_check.set(default)
            trace.detail("Value reset to %r" % default)


def verify_minimum_maximum(value_to_check, minimum, maximum):
    """
    Verify that a value is within the range allowed.
    :param value_to_check: The value to check.
    :param minimum: The minimum value that is allowed.
    :param maximum: The maximum value that is allowed.
    :return: The updated value.
    """
    test = int(value_to_check.get())
    trace.flow("Test is %r, minimum is %r" % (test, minimum))
    if test < minimum:
        trace.flow("Value reset to minimum: %d" % int(minimum))
        value_to_check.set(minimum)
    elif test > maximum:
        trace.flow("Value reset to maximum: %d" % int(maximum))
        value_to_check.set(maximum)
    else:
        trace.detail("Value set to %d" % test)



