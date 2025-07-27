#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module handles a characters basic statistics.

Classes:
    MeleeOb
    BasicStats
"""
import sys
from typing import Union

import trace_log as trace

sys.path.append('../../')


class MeleeOb:
    """MeleeOb class is used to hold information about a single melee attack type.

    Methods:
        __init__(self, melee_ob_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, melee_ob_object: dict[str, Union[str, int]]):
        trace.entry()
        self.ob: int = melee_ob_object.get("ob")
        self.ob_type: str = melee_ob_object.get("ob-type")
        trace.exit()


class BasicStats:
    """BasicStats class is used to hold basic character statistics.

    Methods:
        __init__(self, basic_stats_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, basic_stats_object: dict[str, Union[int, str, list[dict[str, Union[str, int]]]]]):
        trace.entry()
        self.level: int = basic_stats_object.get("level")
        self.hits: int = basic_stats_object.get("body-development")
        self.at: int = basic_stats_object.get("armour-type")
        self.db: int = basic_stats_object.get("defensive-bonus")
        self.shield: int = basic_stats_object.get("shield-bonus")

        self.melee_obs: list[MeleeOb] = []
        ob_objects_list: list[dict[str, Union[str, int]]] = basic_stats_object.get("melee-obs")
        for ob_object in ob_objects_list:
            melee_ob: MeleeOb = MeleeOb(ob_object)
            self.melee_obs.append(melee_ob)

        self.missile_ob: int = basic_stats_object.get("missile-ob")
        self.missile_type_ob: str = basic_stats_object.get("missile-ob-type")
        self.mm: int = basic_stats_object.get("movement-speed")
        self.criticals: str = basic_stats_object.get("size", "medium")

        trace.exit()
