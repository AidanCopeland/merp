#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character body development skills information from JSON and stores it in a key, value
format.

Functions:
    init_body_development_skills(body_development_skills_json_object)
"""
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_ADRENAL_TOUGHNESS = "Adrenal Toughness"
JSON_ADRENAL_TOUGHNESS = "adrenal-toughness"

json_input_map = {
    JSON_ADRENAL_TOUGHNESS: SKILL_ADRENAL_TOUGHNESS
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_body_development_skills(body_development_skills_json_object):
    """
    Populate a set of body development skills in an Abilities object.
    :param body_development_skills_json_object: JSON object containing body development skills
    information.
    :return: Parsed body development skills information.
    """
    trace.entry()
    body_development_skills = OrderedDict()
    if body_development_skills_json_object is not None:
        for json_skill in list(body_development_skills_json_object.keys()):
            skill_value = body_development_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name = ' '.join(skill_words)
                skill_name = skill_name.capitalize()
            body_development_skills[skill_name] = skill_value

    trace.exit()
    return body_development_skills
