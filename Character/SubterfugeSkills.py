#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import trace_log as trace
sys.path.append('../')

SKILL_AMBUSH = "Ambush"
JSON_AMBUSH = "ambush"
SKILL_STALK_HIDE = "Stalk/Hide"
JSON_STALK_HIDE = "stalk-hide"
SKILL_PICK_LOCK = "Pick Lock"
JSON_PICK_LOCK = "pick-lock"
SKILL_DISARM_TRAP = "Disarm Trap"
JSON_DISARM_TRAP = "disarm-trap"

json_input_map = {
    JSON_AMBUSH: SKILL_AMBUSH,
    JSON_STALK_HIDE: SKILL_STALK_HIDE,
    JSON_PICK_LOCK: SKILL_PICK_LOCK,
    JSON_DISARM_TRAP: SKILL_DISARM_TRAP
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.  List of non-standard skills to loop through and check?


def init_subterfuge_skills(subterfuge_skills_json_object):
    trace.entry()
    subterfuge_skills = {}
    for json_skill in subterfuge_skills_json_object.keys():
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
