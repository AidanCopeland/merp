#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module handles a characters basic statistics.

Classes:
    MeleeOb
    BasicStats
"""
import sys
import trace_log as trace

sys.path.append('../../')


class MeleeOb:
    """MeleeOb class is used to hold information about a single melee attack type.

    Methods:
        __init__(self, melee_ob_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, melee_ob_object):
        trace.entry()
        self.ob = melee_ob_object.get("ob")
        self.ob_type = melee_ob_object.get("ob-type")
        trace.exit()


class BasicStats:
    """BasicStats class is used to hold basic character statistics.

    Methods:
        __init__(self, basic_stats_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, basic_stats_object):
        trace.entry()
        self.level = basic_stats_object.get("level")
        self.hits = basic_stats_object.get("body-development")
        self.at = basic_stats_object.get("armour-type")
        self.db = basic_stats_object.get("defensive-bonus")
        self.shield = basic_stats_object.get("shield-bonus")

        self.melee_obs = []
        ob_objects_list = basic_stats_object.get("melee-obs")
        for ob_object in ob_objects_list:
            melee_ob = MeleeOb(ob_object)
            self.melee_obs.append(melee_ob)

        self.missile_ob = basic_stats_object.get("missile-ob")
        self.missile_type_ob = basic_stats_object.get("missile-ob-type")
        self.mm = basic_stats_object.get("movement-speed")
        self.criticals = basic_stats_object.get("size", "medium")

        trace.exit()

    def set_hits(self, hits):
        """
        Set the total number of hits that the character can take.
        :param hits: The number of hits that the character can take.
        """
        trace.entry()
        self.hits = hits
        trace.exit()

    def add_hits(self, hits):
        """
        Updates the number of hits that the character can take, ensuring
        that the number of hits is greater than or equal to 0.
        :param rounds: The number of rounds to add.
        """
        trace.entry()
        self.hits += hits
        self.hits = max(0, self.hits)
        trace.detail(
            "Added {} hits, total hits {}".format(
                hits,
                self.hits))
        trace.exit()
