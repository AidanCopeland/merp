#!/usr/bin/python
# -*- coding: utf-8 -*-
from builtins import object
import sys
import trace_log as trace
import Wound

sys.path.append('../../')


class Wounds(object):
    def __init__(self):
        trace.entry()
        self.wound_list = list()
        self.total_damage = Wound()
        trace.exit()
