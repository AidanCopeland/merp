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
        self.wound_list = list()
        self.total_damage = Wound()
        trace.exit()
