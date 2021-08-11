#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character general skills information from JSON and stores it in a key, value format.

Functions:
    init_general_skills(general_skills_json_object)
"""
import string
import sys
from collections import OrderedDict
import trace_log as trace

sys.path.append('../../')

SKILL_CLIMB = "Climb"
JSON_CLIMB = "climb"
SKILL_RIDE = "Ride"
JSON_RIDE = "ride"
SKILL_SWIM = "Swim"
JSON_SWIM = "swim"
SKILL_TRACK = "Track"
JSON_TRACK = "track"
SKILL_ACROBATICS = "Acrobatics"
JSON_ACROBATICS = "acrobatics"
SKILL_ANIMAL_MASTERY = "Animal Mastery"
JSON_ANIMAL_MASTERY = "animal-mastery"
SKILL_CAVING = "Caving"
JSON_CAVING = "caving"
SKILL_DIVING = "Diving"
JSON_DIVING = "diving"
SKILL_DIRECTION_SENSE = "Direction Sense"
JSON_DIRECTION_SENSE = "direction-sense"
SKILL_FLYING = "Flying/gliding"
JSON_FLYING = "flying"
SKILL_FORAGING = "Foraging"
JSON_FORAGING = "foraging"
SKILL_HERB_LORE = "Herb Lore"
JSON_HERB_LORE = "herb-lore"
SKILL_HUNTING = "Hunting"
JSON_HUNTING = "hunting"
SKILL_NAVIGATION = "Navigation"
JSON_NAVIGATION = "navigation"
SKILL_POLE_VAULTING = "Pole-vaulting"
JSON_POLE_VAULTING = "pole-vaulting"
SKILL_PREPARING_HERBS = "Preparing Herbs"
JSON_PREPARING_HERBS = "preparing-herbs"
SKILL_RAPPELLING = "Rappelling"
JSON_RAPPELLING = "rappelling"
SKILL_READING_TRACKS = "Reading Tracks"
JSON_READING_TRACKS = "reading-tracks"
SKILL_ROWING = "Rowing"
JSON_ROWING = "rowing"
SKILL_SAILING = "Sailing"
JSON_SAILING = "sailing"
SKILL_SCALING = "Scaling"
JSON_SCALING = "scaling"
SKILL_SKIING = "Skiing"
JSON_SKIING = "skiing"
SKILL_STAR_GAZING = "Star-gazing"
JSON_STAR_GAZING = "star-gazing"
SKILL_SURVIVAL = "Survival"
JSON_SURVIVAL = "survival"
SKILL_TIGHTROPE_WALKING = "Tightrope-walking"
JSON_TIGHTROPE_WALKING = "tightrope-walking"
SKILL_TRAPPING = "Trapping"
JSON_TRAPPING = "trapping"
SKILL_WEATHER_WATCHING = "Weather Watching"
JSON_WEATHER_WATCHING = "weather-watching"

json_input_map = {
    JSON_CLIMB: SKILL_CLIMB,
    JSON_RIDE: SKILL_RIDE,
    JSON_SWIM: SKILL_SWIM,
    JSON_TRACK: SKILL_TRACK,
    JSON_ACROBATICS: SKILL_ACROBATICS,
    JSON_ANIMAL_MASTERY: SKILL_ANIMAL_MASTERY,
    JSON_CAVING: SKILL_CAVING,
    JSON_DIVING: SKILL_DIVING,
    JSON_DIRECTION_SENSE: SKILL_DIRECTION_SENSE,
    JSON_FLYING: SKILL_FLYING,
    JSON_FORAGING: SKILL_FORAGING,
    JSON_HERB_LORE: SKILL_HERB_LORE,
    JSON_HUNTING: SKILL_HUNTING,
    JSON_NAVIGATION: SKILL_NAVIGATION,
    JSON_POLE_VAULTING: SKILL_POLE_VAULTING,
    JSON_PREPARING_HERBS: SKILL_PREPARING_HERBS,
    JSON_RAPPELLING: SKILL_RAPPELLING,
    JSON_READING_TRACKS: SKILL_READING_TRACKS,
    JSON_ROWING: SKILL_ROWING,
    JSON_SAILING: SKILL_SAILING,
    JSON_SCALING: SKILL_SCALING,
    JSON_SKIING: SKILL_SKIING,
    JSON_STAR_GAZING: SKILL_STAR_GAZING,
    JSON_SURVIVAL: SKILL_SURVIVAL,
    JSON_TIGHTROPE_WALKING: SKILL_TIGHTROPE_WALKING,
    JSON_TRAPPING: SKILL_TRAPPING,
    JSON_WEATHER_WATCHING: SKILL_WEATHER_WATCHING
}

# Add the profession bonus for each profession and level
# Add the stat bonus for each stat: map from stat name to stat bonus?
# Need to recognise if skills haven't been set.
# List of non-standard skills to loop through and check?


def init_general_skills(general_skills_json_object):
    """
    Populate a set of general skills in an Abilities object.
    :param general_skills_json_object: JSON object containing general skills information.
    :return: Parsed general skills information.
    """
    trace.entry()
    general_skills = OrderedDict()
    if general_skills_json_object is not None:
        for json_skill in list(general_skills_json_object.keys()):
            skill_value = general_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name_lc = (' '.join(skill_words))
                skill_name = string.capwords(skill_name_lc)
            general_skills[skill_name] = skill_value

    trace.exit()
    return general_skills
