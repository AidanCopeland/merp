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
    Information about one wound or all damage taken by a character.

    Methods:
        __init__(self)
        add_hits(self, hits)
        set_hits(self, hits)
        add_bleeding(self, bleeding)
        set_bleeding(self, bleeding)
        add_stun(self, stun)
        set_stun(self, stun)
        add_stun_no_parry(self, stun)
        set_stun_no_parry(self, stun)
        add_penalty(self, penalty)
        set_penalty(self, penalty)
        set_rounds_to_death(self, penalty)
    """
    # pylint: disable = too-few-public-methods
    def __init__(self):
        trace.entry()
        self.hits_per_round = 0
        self.subtraction_from_bonuses = 0
        trace.exit()

