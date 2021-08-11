# -*- coding: utf-8 -*-
"""
The Outdoor/Environmental static maneuver table.

Classes:
    OutdoorEnvironmentalManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.general_skills import \
    SKILL_CAVING, SKILL_FORAGING, SKILL_HUNTING, SKILL_STAR_GAZING, SKILL_SURVIVAL, \
    SKILL_WEATHER_WATCHING, SKILL_NAVIGATION
from console.character.secondary_skills import \
    SKILL_REGION_LORE_WILD, SKILL_FLORA_LORE_WILD, SKILL_FAUNA_LORE_WILD

import trace_log as trace

sys.path.append('../')


class OutdoorEnvironmentalManeuverTable(StaticManeuverTable):
    """
    Outdoor/Environmental static maneuver table.

    Methods:
        select_outdoor_environmental_table(maneuver_type)
    """
    MANEUVER_CAVING = "Caving"
    MANEUVER_FORAGING = "Foraging"
    MANEUVER_HUNTING = "Hunting"
    MANEUVER_STAR_GAZING = "Star-gazing"
    MANEUVER_SURVIVAL = "Survival"
    MANEUVER_WEATHER_WATCHING = "Weather Watching"

    maneuver_type_options = (
        MANEUVER_CAVING, MANEUVER_FORAGING, MANEUVER_HUNTING,
        MANEUVER_STAR_GAZING, MANEUVER_SURVIVAL, MANEUVER_WEATHER_WATCHING
    )

    maneuver_result_text = {
        BLUNDER:
            "Now you're in trouble.  You manage to get yourself into an accident (GM's "
            "discretion, perhaps a bad fall, earthquake, animal attack, etc.).  You take "
            "at least an 'A' critical of an appropriate type, and must suffer the other "
            "consequences of the accident.  Hope you're using the buddy system...",
        ABSOLUTE_FAILURE:
            "Over the course of your maneuver, you have managed to get yourself hopelessly "
            "lost.  None of the landmarks are familiar, and your original task is "
            "forgotten as you begin to worry about your return.",
        FAILURE:
            "Apparently your last meal has come back to haunt you.  You feel nauseous, "
            "and fail to complete your maneuver, due to an inability to concentrate.",
        PARTIAL_SUCCESS:
            "You could swear someone keeps moving that landmark!  Well, perhaps a bit "
            "more familiarization with the area will cause it to settle down.",
        NEAR_SUCCESS:
            "Hmmm.  Well, you thought at first that this region was much like a place "
            "you knew in your youth.  The similarity threw you off for a bit, but "
            "another attempt at +20 may resolve the differences.",
        SUCCESS:
            "You know (or learn) this area like the back of your and, and completing your "
            "task is routing.",
        ABSOLUTE_SUCCESS:
            "Your insight into this region yields you extraordinary facility with "
            "activities in this area.  Any further activities undertaken in this area "
            "using any skill in this category gain a modification of +30 (until a "
            "period of six months has passed)."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -30),
        ABSOLUTE_FAILURE: (-50, 4, -15),
        FAILURE: (0, 2, -5),
        PARTIAL_SUCCESS: (20, 2, 0),
        NEAR_SUCCESS: (75, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (150, 0.75, 0)
    }

    @staticmethod
    def select_outdoor_environmental_table(maneuver_type):
        """
        Set the current OutdoorEnvironmental maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.outdoor_environmental.caving_maneuver_table import CavingManeuverTable

        if maneuver_type == OutdoorEnvironmentalManeuverTable.MANEUVER_CAVING:
            trace.flow("Caving maneuver")
            trace.exit()
            return CavingManeuverTable()
        else:
            return OutdoorEnvironmentalManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            OutdoorEnvironmentalManeuverTable.MANEUVER_CAVING:
                [SKILL_CAVING, SKILL_NAVIGATION],
            OutdoorEnvironmentalManeuverTable.MANEUVER_FORAGING:
                [SKILL_FORAGING,
                 SKILL_REGION_LORE_WILD,
                 SKILL_FLORA_LORE_WILD,
                 SKILL_FAUNA_LORE_WILD],
            OutdoorEnvironmentalManeuverTable.MANEUVER_HUNTING:
                [SKILL_HUNTING, SKILL_FAUNA_LORE_WILD],
            OutdoorEnvironmentalManeuverTable.MANEUVER_STAR_GAZING:
                [SKILL_STAR_GAZING, SKILL_NAVIGATION],
            OutdoorEnvironmentalManeuverTable.MANEUVER_SURVIVAL:
                [SKILL_SURVIVAL, ],
            OutdoorEnvironmentalManeuverTable.MANEUVER_WEATHER_WATCHING:
                [SKILL_WEATHER_WATCHING, ]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
