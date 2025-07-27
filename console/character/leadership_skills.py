#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character leadership skills information from JSON and stores it in a key, value format.

Functions:
    init_leadership_skills(leadership_skills_json_object)
"""
import string
import sys
from collections import OrderedDict
from typing import Optional

import trace_log as trace

sys.path.append('../../')

SKILL_CONTACTING_LEADERSHIP = "Contacting"
JSON_CONTACTING_LEADERSHIP = "contacting"
SKILL_DIPLOMACY = "Diplomacy"
JSON_DIPLOMACY = "diplomacy"
SKILL_LEADERSHIP_LEADERSHIP = "Leadership"
JSON_LEADERSHIP_LEADERSHIP = "leadership"
SKILL_PUBLIC_SPEAKING_LEADERSHIP = "Public Speaking"
JSON_PUBLIC_SPEAKING_LEADERSHIP = "public-speaking"

json_input_map = {
    JSON_CONTACTING_LEADERSHIP: SKILL_CONTACTING_LEADERSHIP,
    JSON_DIPLOMACY: SKILL_DIPLOMACY,
    JSON_LEADERSHIP_LEADERSHIP: SKILL_LEADERSHIP_LEADERSHIP,
    JSON_PUBLIC_SPEAKING_LEADERSHIP: SKILL_PUBLIC_SPEAKING_LEADERSHIP
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_leadership_skills(leadership_skills_json_object: Optional[dict[str, int]]):
    """
    Populate a set of leadership skills in an Abilities object.
    :param leadership_skills_json_object: JSON object containing leadership skills information.
    :return: Parsed leadership skills information.
    """
    trace.entry()
    leadership_skills: OrderedDict = OrderedDict()
    if leadership_skills_json_object is not None:
        for json_skill in list(leadership_skills_json_object.keys()):
            skill_value: int = leadership_skills_json_object[json_skill]
            skill_name: Optional[str] = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words: list[str] = json_skill.split('-')
                skill_name_lc: str = (' '.join(skill_words))
                skill_name: str = string.capwords(skill_name_lc)
            leadership_skills[skill_name] = skill_value

    trace.exit()
    return leadership_skills
