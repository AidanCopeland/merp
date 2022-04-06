#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Lists all wounds taken by a character.

Classes:
    Wounds
"""
import sys
from console.character.wound import Wound
import trace_log as trace

sys.path.append('../../')


class Wounds:
    """
    Information about all the wounds taken by a character.

    Methods:
        __init__(self)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self):
        trace.entry()

        # Total damage taken by a character.
        self.total_damage = Wound()

        # List of individual wounds taken by a character.  For information
        # only; individual wounds are not used to calculate total damage.
        # Optionally, removing a wound can be made to reduce the total
        # damage by the same amount.
        self.wound_list = list()
        trace.exit()
