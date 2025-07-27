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
        self.hits: int = 0
        self.bleeding: int = 0
        self.stun: int = 0
        self.penalty: int = 0
        self.temporary: bool = False
        self.duration_remain: int = 0
        self.rounds_to_death: int = 0
        self.location: str = ""
        self.severity: str = ""
        self.incapacitation: str = ""
        trace.exit()
