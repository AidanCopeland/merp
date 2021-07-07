#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module handles information about a character.

Classes:
    Stat
    character
"""
import sys
import trace_log as trace
from .abilities import Abilities
from .basic_stats import BasicStats

sys.path.append('../../')


class Stat:
    """Stat class is used to store information about a primary stat value.

    Methods:
        __init__(self, stat_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, stat_object):
        trace.entry()
        self.value = stat_object.get("value")
        self.bonus = stat_object.get("bonus")
        trace.exit()


class Character:
    """Character class is used to store all information about a character.

    Methods:
        __init__(self, character_object)
        init_stats(self, stats_object)
    """
    # pylint: disable=too-few-public-methods
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
        """This method stores a characters primary stats.

        Input arguments: stats_object contains the character's primary stats.
        """
        trace.entry()

        self.stats = {
            "ST": Stat(stats_object.get("ST")),
            "AG": Stat(stats_object.get("AG")),
            "CO": Stat(stats_object.get("CO")),
            "IG": Stat(stats_object.get("IG")),
            "IT": Stat(stats_object.get("IT")),
            "PR": Stat(stats_object.get("PR"))
        }
