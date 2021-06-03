#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import trace_log as trace
from MovementSkills import init_movement_skills
from WeaponSkills import init_weapon_skills
from GeneralSkills import init_general_skills
from SubterfugeSkills import init_subterfuge_skills
from MagicalSkills import init_magical_skills
sys.path.append('../')


class Abilities(object):
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

