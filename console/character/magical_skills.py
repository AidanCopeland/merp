#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Imports character magical skills information from JSON and stores it in a key, value format.

Functions:
    init_magical_skills(magical_skills_json_object)
"""
import string
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
SKILL_ARTIFACT_LORE = "Artifact Lore"
JSON_ARTIFACT_LORE = "artifact-lore"
SKILL_CHANNELING = "Channeling"
JSON_CHANNELING = "channeling"
SKILL_CIRCLE_LORE = "Circle Lore"
JSON_CIRCLE_LORE = "circle-lore"
SKILL_DIVINATION = "Divination"
JSON_DIVINATION = "divination"
SKILL_DIVINATION_LORE = "Divination Lore"
JSON_DIVINATION_LORE = "divination-lore"
SKILL_MAGIC_RITUAL = "Magic Ritual"
JSON_MAGIC_RITUAL = "magic-ritual"
SKILL_MAGICAL_LORE = "Magical Lore"
JSON_MAGICAL_LORE = "magical-lore"
SKILL_MAGICAL_PREDICTION = "Magical Predication"
JSON_MAGICAL_PREDICTION = "magical-prediction"
SKILL_MENTAL_CONTROL = "Mental Control"
JSON_MENTAL_CONTROL = "mental-control"
SKILL_POWER_PERCEPTION = "Power Perception"
JSON_POWER_PERCEPTION = "power-perception"
SKILL_SANITY_HEALING = "Sanity Healing"
JSON_SANITY_HEALING = "sanity-healing"
SKILL_SPELL_ARTISTRY = "Spell Artistry"
JSON_SPELL_ARTISTRY = "spell-artistry"
SKILL_SPELL_CONCENTRATION = "Spell Concentration"
JSON_SPELL_CONCENTRATION = "spell-concentration"
SKILL_SPELL_LORE = "Spell Lore"
JSON_SPELL_LORE = "spell-lore"
SKILL_SPELL_MASTERY = "Spell Mastery"
JSON_SPELL_MASTERY = "spell-mastery"
SKILL_SPELL_TRICKERY = "Spell Trickery"
JSON_SPELL_TRICKERY = "spell-trickery"
SKILL_SUMMONING = "Summoning"
JSON_SUMMONING = "summoning"
SKILL_SYMBOL_LORE = "Symbol Lore"
JSON_SYMBOL_LORE = "symbol-lore"
SKILL_TRANSCEND_ARMOUR = "Transcend Armour"
JSON_TRANSCEND_ARMOUR = "transcend-armour"
SKILL_WARDING_LORE = "Warding Lore"
JSON_WARDING_LORE = "warding-lore"

json_input_map = {
    JSON_READ_RUNES: SKILL_READ_RUNES,
    JSON_USE_ITEMS: SKILL_USE_ITEMS,
    JSON_DIRECTED_SPELLS: SKILL_DIRECTED_SPELLS,
    JSON_ARTIFACT_LORE: SKILL_ARTIFACT_LORE,
    JSON_CHANNELING: SKILL_CHANNELING,
    JSON_CIRCLE_LORE: SKILL_CIRCLE_LORE,
    JSON_DIVINATION: SKILL_DIVINATION,
    JSON_DIVINATION_LORE: SKILL_DIVINATION_LORE,
    JSON_MAGIC_RITUAL: SKILL_MAGIC_RITUAL,
    JSON_MAGICAL_LORE: SKILL_MAGICAL_LORE,
    JSON_MAGICAL_PREDICTION: SKILL_MAGICAL_PREDICTION,
    JSON_MENTAL_CONTROL: SKILL_MENTAL_CONTROL,
    JSON_POWER_PERCEPTION: SKILL_POWER_PERCEPTION,
    JSON_SANITY_HEALING: SKILL_SANITY_HEALING,
    JSON_SPELL_ARTISTRY: SKILL_SPELL_ARTISTRY,
    JSON_SPELL_CONCENTRATION: SKILL_SPELL_CONCENTRATION,
    JSON_SPELL_LORE: SKILL_SPELL_LORE,
    JSON_SPELL_MASTERY: SKILL_SPELL_MASTERY,
    JSON_SPELL_TRICKERY: SKILL_SPELL_TRICKERY,
    JSON_SUMMONING: SKILL_SUMMONING,
    JSON_SYMBOL_LORE: SKILL_SYMBOL_LORE,
    JSON_TRANSCEND_ARMOUR: SKILL_TRANSCEND_ARMOUR,
    JSON_WARDING_LORE: SKILL_WARDING_LORE
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
    if magical_skills_json_object is not None:
        for json_skill in list(magical_skills_json_object.keys()):
            skill_value = magical_skills_json_object[json_skill]
            skill_name = json_input_map.get(json_skill)
            if skill_name is None:
                trace.flow("Unexpected skill %s, convert JSON name" % json_skill)
                skill_words = json_skill.split('-')
                skill_name_lc = (' '.join(skill_words))
                skill_name = string.capwords(skill_name_lc)
            magical_skills[skill_name] = skill_value

    trace.exit()
    return magical_skills
