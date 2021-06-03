# -*- coding: utf-8 -*-
import sys
from bisect import bisect_right
import trace_log as trace

sys.path.append('../')

merp_table_minimum_values = [0, 6, 21, 36, 51, 66, 80, 81, 87, 90, 91, 97, 100, 101, 107, 110, 111, 117, 120]


def find_table_row_index(table_minimum_values, roll):
    """
    Find the index of a row in a table, passing in a set of minimum values and the dice roll.
    :param table_minimum_values: The set of minimum values for entries in the table.
    :param roll: The resolved dice roll.
    :return: The index of the table row.
    """
    'Find rightmost value less than or equal to x'
    trace.detail("Roll is %d" % roll)
    index = bisect_right(table_minimum_values, roll)
    if index:
        return index - 1
    raise ValueError


def find_merp_table_row_entry(table, roll):
    """
    Find the row in a table, passing in the set of minimum values for each row and the dice roll.
    :param table: The table to check.
    :param table_minimum_values: The set of minimum values for entries in the table.
    :param roll: The resolved dice roll.
    :return: The row in the table.
    """
    index = find_table_row_index(merp_table_minimum_values, roll)
    trace.detail("Index is %d" % index)
    return table[index]
