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
SKILL_ADRENAL_DEFLECTING = "Adrenal Deflecting"
JSON_ADRENAL_DEFLECTING = "adrenal-deflecting"
SKILL_ADRENAL_EVASION = "Adrenal Evasion"
JSON_ADRENAL_EVASION = "adrenal-evasion"
SKILL_ADRENAL_QUICKDRAW = "Adrenal Quickdraw"
JSON_ADRENAL_QUICKDRAW = "adrenal-quickdraw"
SKILL_ADRENAL_STABILIZATION = "Adrenal Stabilization"
JSON_ADRENAL_STABILIZATION = "adrenal-stabilization"
SKILL_ADRENAL_STRENGTH = "Adrenal Strength"
JSON_ADRENAL_STRENGTH = "adrenal-strength"
SKILL_COMBAT_AWARENESS = "Combat Awareness"
JSON_COMBAT_AWARENESS = "combat-awareness"
SKILL_COMBAT_DECEPTION = "Combat Deception"
JSON_COMBAT_DECEPTION = "combat-deception"
SKILL_DISARM_FOE = "Disarm Foe"
JSON_DISARM_FOE = "disarm-foe"
SKILL_FRENZY = "Frenzy"
JSON_FRENZY = "frenzy"
SKILL_JOUSTING = "Jousting"
JSON_JOUSTING = "jousting"
SKILL_POWER_STRIKING = "Power-striking"
JSON_POWER_STRIKING = "power-striking"
SKILL_POWER_THROWING = "Power-throwing"
JSON_POWER_THROWING = "power-throwing"
SKILL_QUICKDRAW = "Quickdraw"
JSON_QUICKDRAW = "Quickdraw"
SKILL_RAPID_FIRE = "Rapid Fire"
JSON_RAPID_FIRE = "rapid-fire"
SKILL_BLINDFIGHTING = "Blindfighting/SLA"
JSON_BLINDFIGHTING = "blindfighting"
SKILL_STUNNED_MANEUVERING = "Stunned Maneuvering"
JSON_STUNNED_MANEUVERING = "stunned-maneuvering"
SKILL_SUBDUAL = "Subdual"
JSON_SUBDUAL = "subdual"
SKILL_SWASHBUCKLING = "Swashbuckling"
JSON_SWASHBUCKLING = "swashbuckling"

json_input_map = {
    JSON_1HE: SKILL_1HE,
    JSON_1HC: SKILL_1HC,
    JSON_2H: SKILL_2H,
    JSON_THROWN: SKILL_THROWN,
    JSON_MISSILE: SKILL_MISSILE,
    JSON_POLE_ARMS: SKILL_POLE_ARMS,
    JSON_ADRENAL_DEFLECTING: SKILL_ADRENAL_DEFLECTING,
    JSON_ADRENAL_EVASION: SKILL_ADRENAL_EVASION,
    JSON_ADRENAL_QUICKDRAW: SKILL_ADRENAL_QUICKDRAW,
    JSON_ADRENAL_STABILIZATION: SKILL_ADRENAL_STABILIZATION,
    JSON_ADRENAL_STRENGTH: SKILL_ADRENAL_STRENGTH,
    JSON_COMBAT_AWARENESS: SKILL_COMBAT_AWARENESS,
    JSON_COMBAT_DECEPTION: SKILL_COMBAT_DECEPTION,
    JSON_DISARM_FOE: SKILL_DISARM_FOE,
    JSON_FRENZY: SKILL_FRENZY,
    JSON_JOUSTING: SKILL_JOUSTING,
    JSON_POWER_STRIKING: SKILL_POWER_STRIKING,
    JSON_POWER_THROWING: SKILL_POWER_THROWING,
    JSON_QUICKDRAW: SKILL_QUICKDRAW,
    JSON_RAPID_FIRE: SKILL_RAPID_FIRE,
    JSON_BLINDFIGHTING: SKILL_BLINDFIGHTING,
    JSON_STUNNED_MANEUVERING: SKILL_STUNNED_MANEUVERING,
    JSON_SUBDUAL: SKILL_SUBDUAL,
    JSON_SWASHBUCKLING: SKILL_SWASHBUCKLING
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
    if weapon_skills_json_object is not None:
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
