#!/usr/bin/python
# -*- coding: utf-8 -*-
from builtins import object
import sys
import trace_log as trace

sys.path.append('../../')


class Stat(object):
    def __init__(self, stat_object):
        trace.entry()
        self.value = stat_object.get("value")
        self.bonus = stat_object.get("bonus")
        trace.exit()


class Stats(object):
    def __init__(self, stats_object):
        trace.entry()
        self.stats = {
            "ST": Stat(stats_object.get("ST")),
            "AG": Stat(stats_object.get("AG")),
            "CO": Stat(stats_object.get("CO")),
            "IG": Stat(stats_object.get("IG")),
            "IT": Stat(stats_object.get("IT")),
            "PR": Stat(stats_object.get("PR"))
        }
        trace.exit()
