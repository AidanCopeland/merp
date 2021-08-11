#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character movement skills information from JSON and stores it in a key, value format.

Functions:
    init_movement_skills(movement_skills_json_object)
"""
import string
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_NO_ARMOUR = "No Armour"
JSON_NO_ARMOUR = "no-armour"
SKILL_SOFT_LEATHER = "Soft Leather"
JSON_SOFT_LEATHER = "soft-leather"
SKILL_RIGID_LEATHER = "Rigid Leather"
JSON_RIGID_LEATHER = "rigid-leather"
SKILL_CHAIN = "Chain"
JSON_CHAIN = "chain"
SKILL_PLATE = "Plate"
JSON_PLATE = "plate"
SKILL_ADRENAL_BALANCE = "Adrenal Balance"
JSON_ADRENAL_BALANCE = "adrenal-balance"
SKILL_ADRENAL_LANDING = "Adrenal Landing"
JSON_ADRENAL_LANDING = "adrenal-landing"
SKILL_ADRENAL_LEAPING = "Adrenal Leaping"
JSON_ADRENAL_LEAPING = "adrenal-leaping"
SKILL_ADRENAL_SPEED = "Adrenal Speed"
JSON_ADRENAL_SPEED = "adrenal-speed"

json_input_map = {
    JSON_NO_ARMOUR: SKILL_NO_ARMOUR,
    JSON_SOFT_LEATHER: SKILL_SOFT_LEATHER,
    JSON_RIGID_LEATHER: SKILL_RIGID_LEATHER,
    JSON_CHAIN: SKILL_CHAIN,
    JSON_PLATE: SKILL_PLATE,
    JSON_ADRENAL_BALANCE: SKILL_ADRENAL_BALANCE,
    JSON_ADRENAL_LANDING: SKILL_ADRENAL_LANDING,
    JSON_ADRENAL_LEAPING: SKILL_ADRENAL_LEAPING,
    JSON_ADRENAL_SPEED: SKILL_ADRENAL_SPEED
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_movement_skills(movement_skills_json_object):
    """
    Populate a set of movement skills in an Abilities object.
    :param movement_skills_json_object: JSON object containing movement skills information.
    :return: Parsed movement skills information.
    """
    trace.entry()
    movement_skills = OrderedDict()
    if movement_skills_json_object is not None:
        for json_skill in list(movement_skills_json_object.keys()):
            skill_value = movement_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name_lc = (' '.join(skill_words))
                skill_name = string.capwords(skill_name_lc)
            movement_skills[skill_name] = skill_value

    trace.exit()
    return movement_skills
