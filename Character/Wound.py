#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

import trace_log as trace

class Wound(object):
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
