#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import trace_log as trace
sys.path.append('../')


class MeleeOb(object):
    def __init__(self, melee_ob_object):
        trace.entry()
        self.ob = melee_ob_object.get("ob")
        self.ob_type = melee_ob_object.get("ob-type")
        trace.exit()


class BasicStats(object):
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
