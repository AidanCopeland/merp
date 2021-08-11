#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character weapon skills information from JSON and stores it in a key, value format.

Functions:
    init_weapon_skills(weapon_skills_json_object)
"""
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_1HE = "One Handed Edged"
JSON_1HE = "1h-edged"
SKILL_1HC = "One Handed Concussion"
JSON_1HC = "1h-concussion"
SKILL_2H = "Two Handed"
JSON_2H = "2-handed"
SKILL_THROWN = "Thrown"
JSON_THROWN = "thrown"
SKILL_MISSILE = "Missile"
JSON_MISSILE = "missile"
SKILL_POLE_ARMS = "Pole Arms"
JSON_POLE_ARMS = "pole-arms"

json_input_map = {
    JSON_1HE: SKILL_1HE,
    JSON_1HC: SKILL_1HC,
    JSON_2H: SKILL_2H,
    JSON_THROWN: SKILL_THROWN,
    JSON_MISSILE: SKILL_MISSILE,
    JSON_POLE_ARMS: SKILL_POLE_ARMS
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_weapon_skills(weapon_skills_json_object):
    """
    Populate a set of weapon skills in an Abilities object.
    :param weapon_skills_json_object: JSON object containing weapon skills information.
    :return: Parsed weapon skills information.
    """
    trace.entry()
    weapon_skills = OrderedDict()
    for json_skill in list(weapon_skills_json_object.keys()):
        skill_value = weapon_skills_json_object[json_skill]
        skill_name = json_input_map.get(json_skill)
        if skill_name is None:
            trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
            skill_words = json_skill.split('-')
            skill_name = ' '.join(skill_words)
            skill_name = skill_name.capitalize()
        weapon_skills[skill_name] = skill_value

    trace.exit()
    return weapon_skills
