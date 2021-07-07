#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module handles character skill bonuses.

Classes: Abilities
"""
import sys
import trace_log as trace
from .movement_skills import init_movement_skills
from .weapon_skills import init_weapon_skills
from .general_skills import init_general_skills
from .subterfuge_skills import init_subterfuge_skills
from .magical_skills import init_magical_skills
sys.path.append('../../')


class Abilities:
    """Abilities class stores a characters skill bonuses.

    Methods:
        __init__(self, abilities_object)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, abilities_object):
        trace.entry()

        self.movement_skills = init_movement_skills(abilities_object.get("movement-skills"))
        trace.detail("Movement skills: %r" % self.movement_skills)

        self.weapon_skills = init_weapon_skills(abilities_object.get("weapon-skills"))
        trace.detail("Weapon skills: %r" % self.weapon_skills)

        self.general_skills = init_general_skills(abilities_object.get("general-skills"))
        trace.detail("General skills: %r" % self.general_skills)

        self.subterfuge_skills = init_subterfuge_skills(abilities_object.get("subterfuge-skills"))
        trace.detail("Subterfuge skills: %r" % self.subterfuge_skills)

        self.magical_skills = init_magical_skills(abilities_object.get("magical-skills"))
        trace.detail("Magical skills: %r" % self.magical_skills)

        trace.exit()
