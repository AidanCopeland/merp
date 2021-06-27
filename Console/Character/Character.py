#!/usr/bin/python
# -*- coding: utf-8 -*-
from builtins import object
import sys
import trace_log as trace
from .Abilities import Abilities
from .BasicStats import BasicStats

sys.path.append('../../')


class Stat(object):
    def __init__(self, stat_object):
        trace.entry()
        self.value = stat_object.get("value")
        self.bonus = stat_object.get("bonus")
        trace.exit()


class Character(object):
    def __init__(self, character_object):
        trace.entry()
        self.name = character_object.get("name")

        basic_stats_object = character_object.get("basic-stats")
        self.basic_stats = BasicStats(basic_stats_object)

        self.stats = {}
        self.init_stats(character_object.get("stats"))

        abilities_object = character_object.get("abilities")
        self.abilities = Abilities(abilities_object)

        self.locked = False
        trace.exit()

    def init_stats(self, stats_object):
        trace.entry()

        self.stats = {
            "ST": Stat(stats_object.get("ST")),
            "AG": Stat(stats_object.get("AG")),
            "CO": Stat(stats_object.get("CO")),
            "IG": Stat(stats_object.get("IG")),
            "IT": Stat(stats_object.get("IT")),
            "PR": Stat(stats_object.get("PR"))
        }
