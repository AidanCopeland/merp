#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This module handles information about a character.

Classes:
    Stat
    character
"""
import sys
from typing import Union

import trace_log as trace
from .abilities import Abilities
from .basic_stats import BasicStats
from .stats import Stats

sys.path.append('../../')


class Stat:
    """Stat class is used to store information about a primary stat value.

    Methods:
        __init__(self, stat_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, stat_object: dict[str, int]):
        trace.entry()
        self.value: int = stat_object.get("value")
        self.bonus: int = stat_object.get("bonus")
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
        self.name: str = character_object.get("name")

        basic_stats_object: dict[str, Union[str, list, int]] = character_object.get("basic-stats")
        self.basic_stats: BasicStats = BasicStats(basic_stats_object)

        stats_object: dict[str, dict[str, int]] = character_object.get("stats")
        if stats_object is not None:
            self.stats: Stats = Stats(stats_object)

        abilities_object: dict[str, dict[str, int]] = character_object.get("abilities", {})
        self.abilities: Abilities = Abilities(abilities_object)

        self.locked = False
        trace.exit()
