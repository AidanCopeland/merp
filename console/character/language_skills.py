#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character language skills information from JSON and stores it in a key, value format.

Functions:
    init_language_skills(language_skills_json_object)
"""
import string
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_LIP_READING = "Lip Reading"
JSON_LIP_READING = "lip-reading"
SKILL_SIGNALLING = "Signalling"
JSON_SIGNALLING = "signalling"

json_input_map = {
    JSON_LIP_READING: SKILL_LIP_READING,
    JSON_SIGNALLING: SKILL_SIGNALLING
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_language_skills(language_skills_json_object):
    """
    Populate a set of language skills in an Abilities object.
    :param language_skills_json_object: JSON object containing language skills information.
    :return: Parsed language skills information.
    """
    trace.entry()
    language_skills = OrderedDict()
    if language_skills_json_object is not None:
        for json_skill in list(language_skills_json_object.keys()):
            skill_value = language_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name_lc = (' '.join(skill_words))
                skill_name = string.capwords(skill_name_lc)
            language_skills[skill_name] = skill_value

    trace.exit()
    return language_skills
