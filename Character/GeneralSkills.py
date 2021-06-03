#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import trace_log as trace
sys.path.append('../')

SKILL_CLIMB = "Climb"
JSON_CLIMB = "climb"
SKILL_RIDE = "Ride"
JSON_RIDE = "ride"
SKILL_SWIM = "Swim"
JSON_SWIM = "swim"
SKILL_TRACK = "Track"
JSON_TRACK = "track"

json_input_map = {
    JSON_CLIMB: SKILL_CLIMB,
    JSON_RIDE: SKILL_RIDE,
    JSON_SWIM: SKILL_SWIM,
    JSON_TRACK: SKILL_TRACK
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.  List of non-standard skills to loop through and check?


def init_general_skills(general_skills_json_object):
    trace.entry()
    general_skills = {}
    for json_skill in general_skills_json_object.keys():
        skill_value = general_skills_json_object[json_skill]
        skill_name = json_input_map.get(json_skill)
        if skill_name is None:
            trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
            skill_words = json_skill.split('-')
            skill_name = ' '.join(skill_words)
            skill_name = skill_name.capitalize()
        general_skills[skill_name] = skill_value

    trace.exit()
    return general_skills
