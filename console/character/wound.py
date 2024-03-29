#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Describes a wound taken by a character.

Classes:
    Wound
"""
import sys
import trace_log as trace

sys.path.append('../../')


class Wound:
    """
    Information about a wound taken by a character.

    Methods:
        __init__(self)
    """
    # pylint: disable = too-few-public-methods
    def __init__(self):
        trace.entry()
        self.hits = 0
        self.bleeding = 0
        self.stun = 0
        self.penalty = 0
        self.temporary = False
        self.duration_remain = 0
        self.rounds_to_death = 0
        self.location = ""
        self.severity = ""
        self.incapacitation = ""
        trace.exit()
