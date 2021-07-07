#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Classes handling a character's primary stats.

Classes:
    Stat
    Stats
"""
import sys
import trace_log as trace

sys.path.append('../../')


class Stat:
    """
    A primary stat object.

    Methods:
        __init__(self, stat_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, stat_object):
        trace.entry()
        self.value = stat_object.get("value")
        self.bonus = stat_object.get("bonus")
        trace.exit()


class Stats:
    """
    A character's primary stats.

    Methods:
        __init__(self, stats_object)
    """
    # pylint: disable=too-few-public-methods
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
