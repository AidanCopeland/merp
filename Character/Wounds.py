#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

import trace_log as trace

class Wounds(object):
    def __init__(self):
        trace.entry()
        self.wound_list = list()
        self.total_damage = Wound()
        trace.exit()
