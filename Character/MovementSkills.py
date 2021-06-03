#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import trace_log as trace
sys.path.append('../')

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

json_input_map = {
    JSON_NO_ARMOUR: SKILL_NO_ARMOUR,
    JSON_SOFT_LEATHER: SKILL_SOFT_LEATHER,
    JSON_RIGID_LEATHER: SKILL_RIGID_LEATHER,
    JSON_CHAIN: SKILL_CHAIN,
    JSON_PLATE: SKILL_PLATE
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.  List of non-standard skills to loop through and check?


def init_movement_skills(movement_skills_json_object):
    trace.entry()
    movement_skills = {}
    for json_skill in movement_skills_json_object.keys():
        skill_value = movement_skills_json_object[json_skill]
        skill_name = json_input_map.get(json_skill)
        if skill_name is None:
            trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
            skill_words = json_skill.split('-')
            skill_name = ' '.join(skill_words)
            skill_name = skill_name.capitalize()
        movement_skills[skill_name] = skill_value

    trace.exit()
    return movement_skills
