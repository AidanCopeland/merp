#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character magical skills information from JSON and stores it in a key, value format.

Functions:
    init_magical_skills(magical_skills_json_object)
"""
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_READ_RUNES = "Read Runes"
JSON_READ_RUNES = "read-runes"
SKILL_USE_ITEMS = "Use Items"
JSON_USE_ITEMS = "use-items"
SKILL_DIRECTED_SPELLS = "Directed Spells"
JSON_DIRECTED_SPELLS = "directed-spells"

json_input_map = {
    JSON_READ_RUNES: SKILL_READ_RUNES,
    JSON_USE_ITEMS: SKILL_USE_ITEMS,
    JSON_DIRECTED_SPELLS: SKILL_DIRECTED_SPELLS
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_magical_skills(magical_skills_json_object):
    """
    Populate a set of magical skills in an Abilities object.
    :param magical_skills_json_object: JSON object containing magical skills information.
    :return: Parsed magical skills information.
    """
    trace.entry()
    magical_skills = OrderedDict()
    for json_skill in list(magical_skills_json_object.keys()):
        skill_value = magical_skills_json_object[json_skill]
        skill_name = json_input_map.get(json_skill)
        if skill_name is None:
            trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
            skill_words = json_skill.split('-')
            skill_name = ' '.join(skill_words)
            skill_name = skill_name.capitalize()
        magical_skills[skill_name] = skill_value

    trace.exit()
    return magical_skills
