#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character subterfuge skills information from JSON and stores it in a key, value format.

Functions:
    init_subterfuge_skills(subterfuge_skills_json_object)
"""
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_AMBUSH = "Ambush"
JSON_AMBUSH = "ambush"
SKILL_STALK_HIDE = "Stalk/Hide"
JSON_STALK_HIDE = "stalk-hide"
SKILL_PICK_LOCK = "Pick Lock"
JSON_PICK_LOCK = "pick-lock"
SKILL_DISARM_TRAP = "Disarm Trap"
JSON_DISARM_TRAP = "disarm-trap"
SKILL_BRIBERY = "Bribery"
JSON_BRIBERY = "bribery"
SKILL_CAMOUFLAGE = "Camouflage"
JSON_CAMOUFLAGE = "camouflage"
SKILL_CONTACTING_SUBTERFUGE = "Contacting"
JSON_CONTACTING_SUBTERFUGE = "contacting"
SKILL_COUNTERFEITING = "Counterfeiting"
JSON_COUNTERFEITING = "counterfeiting"
SKILL_DISGUISE = "Disguise"
JSON_DISGUISE = "disguise"
SKILL_DUPING = "Duping"
JSON_DUPING = "duping"
SKILL_FORGERY = "Forgery"
JSON_FORGERY = "forgery"
SKILL_HIDING_ITEMS = "Hiding Items"
JSON_HIDING_ITEMS = "hiding-items"
SKILL_INTERROGATION = "Interrogation"
JSON_INTERROGATION = "interrogation"
SKILL_LIE_PERCEPTION = "Lie Perception"
JSON_LIE_PERCEPTION = "lie-perception"
SKILL_LOCK_LORE = "Lock Lore"
JSON_LOCK_LORE = "lock-lore"
SKILL_PICK_POCKETS = "Pick Pockets"
JSON_PICK_POCKETS = "pick-pockets"
SKILL_POISON_LORE = "Poison Lore"
JSON_POISON_LORE = "poison-lore"
SKILL_POISON_PERCEPTION = "Poison Perception"
JSON_POISON_PERCEPTION = "poison-perception"
SKILL_PREPARING_POISONS = "Preparing Poisons"
JSON_PREPARING_POISONS = "preparing-poisons"
SKILL_SETTING_TRAPS = "Setting Traps"
JSON_SETTING_TRAPS = "setting-traps"
SKILL_SILENT_SKILL = "Silent Kill"
JSON_SILENT_KILL = "silent-kill"
SKILL_STREETWISE = "Streetwise"
JSON_STREETWISE = "streetwise"
SKILL_SURVEILLANCE = "Surveillance"
JSON_SURVEILLANCE = "surveillance"
SKILL_TRAP_BUILDING = "Trap Building"
JSON_TRAP_BUILDING = "trap-building"
SKILL_TRICKERY = "Trickery"
JSON_TRICKERY = "trickery"
SKILL_USE_REMOVE_POISON = "Use/Remove Poison"
JSON_USE_REMOVE_POISON = "use-remove-poison"

json_input_map = {
    JSON_AMBUSH: SKILL_AMBUSH,
    JSON_STALK_HIDE: SKILL_STALK_HIDE,
    JSON_PICK_LOCK: SKILL_PICK_LOCK,
    JSON_DISARM_TRAP: SKILL_DISARM_TRAP,
    JSON_BRIBERY: SKILL_BRIBERY,
    JSON_CAMOUFLAGE: SKILL_CAMOUFLAGE,
    JSON_CONTACTING_SUBTERFUGE: SKILL_CONTACTING_SUBTERFUGE,
    JSON_COUNTERFEITING: SKILL_COUNTERFEITING,
    JSON_DISGUISE: SKILL_DISGUISE,
    JSON_DUPING: SKILL_DUPING,
    JSON_FORGERY: SKILL_FORGERY,
    JSON_HIDING_ITEMS: SKILL_HIDING_ITEMS,
    JSON_INTERROGATION: SKILL_INTERROGATION,
    JSON_LIE_PERCEPTION: SKILL_LIE_PERCEPTION,
    JSON_LOCK_LORE: SKILL_LOCK_LORE,
    JSON_PICK_POCKETS: SKILL_PICK_POCKETS,
    JSON_POISON_LORE: SKILL_POISON_LORE,
    JSON_POISON_PERCEPTION: SKILL_POISON_PERCEPTION,
    JSON_PREPARING_POISONS: SKILL_PREPARING_POISONS,
    JSON_SETTING_TRAPS: SKILL_SETTING_TRAPS,
    JSON_SILENT_KILL: SKILL_SILENT_SKILL,
    JSON_STREETWISE: SKILL_STREETWISE,
    JSON_SURVEILLANCE: SKILL_SURVEILLANCE,
    JSON_TRAP_BUILDING: SKILL_TRAP_BUILDING,
    JSON_TRICKERY: SKILL_TRICKERY,
    JSON_USE_REMOVE_POISON: SKILL_USE_REMOVE_POISON
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_subterfuge_skills(subterfuge_skills_json_object):
    """
    Populate a set of subterfuge skills in an Abilities object.
    :param subterfuge_skills_json_object: JSON object containing subterfuge skills information.
    :return: Parsed subterfuge skills information.
    """
    trace.entry()
    subterfuge_skills = OrderedDict()
    if subterfuge_skills_json_object is not None:
        for json_skill in list(subterfuge_skills_json_object.keys()):
            skill_value = subterfuge_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name = ' '.join(skill_words)
                skill_name = skill_name.capitalize()
            subterfuge_skills[skill_name] = skill_value

    trace.exit()
    return subterfuge_skills
