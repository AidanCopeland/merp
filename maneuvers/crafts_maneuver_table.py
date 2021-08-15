# -*- coding: utf-8 -*-
"""
The Crafts static maneuver table.

Classes:
    CraftsManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.secondary_skills import \
    SKILL_COOKING, SKILL_DRAFTING, SKILL_FLETCHING, SKILL_HORTICULTURE, SKILL_LEATHER_CRAFTS, \
    SKILL_METAL_CRAFTS, SKILL_ROPE_MASTERY, SKILL_SCRIBING, SKILL_SERVICE, SKILL_SEWING_WEAVING, \
    SKILL_SKINNING, SKILL_STONE_CRAFTS, SKILL_WOOD_CRAFTS, SKILL_SMITHING
from console.character.general_skills import \
    SKILL_TRAPPING, SKILL_HERB_LORE, SKILL_SURVIVAL, SKILL_READING_TRACKS, SKILL_TRACK
from console.character.subterfuge_skills import SKILL_TRAP_BUILDING

import trace_log as trace

sys.path.append('../')


class CraftsManeuverTable(StaticManeuverTable):
    """
    crafts static maneuver table.

    Methods:
        select_crafts_table(maneuver_type)
    """
    MANEUVER_COOKING = "Cooking"
    MANEUVER_DRAFTING = "Drafting"
    MANEUVER_FLETCHING = "Fletching"
    MANEUVER_HORTICULTURE = "Horticulture"
    MANEUVER_LEATHER_CRAFTS = "Leather-crafts"
    MANEUVER_METAL_CRAFTS = "Metal-crafts"
    MANEUVER_ROPE_MASTERY = "Rope Mastery"
    MANEUVER_SCRIBING = "Scribing"
    MANEUVER_SERVICE = "Service duties"
    MANEUVER_SEWING_WEAVING = "Sewing/weaving"
    MANEUVER_SKINNING = "Skinning"
    MANEUVER_STONE_CRAFTS = "Stone-crafts"
    MANEUVER_TRAPPING = "Trapping"
    MANEUVER_WOOD_CRAFTS = "Wood-crafts"

    maneuver_type_options = (
        MANEUVER_COOKING, MANEUVER_DRAFTING, MANEUVER_FLETCHING,
        MANEUVER_HORTICULTURE, MANEUVER_LEATHER_CRAFTS, MANEUVER_METAL_CRAFTS,
        MANEUVER_ROPE_MASTERY, MANEUVER_SCRIBING, MANEUVER_SEWING_WEAVING,
        MANEUVER_SKINNING, MANEUVER_STONE_CRAFTS, MANEUVER_TRAPPING,
        MANEUVER_WOOD_CRAFTS
    )

    maneuver_result_text = {
        BLUNDER:
            "You have failed miserably in your craft.  However, you are so oblivious and "
            "self-absorbed that you are convinced that you have, in fact, succeeded "
            "admirably.  You have misplaced, misused or broken some or all of the people, "
            "tools or materials used in this task.  You will defend yourself until "
            "irrefutable evidence is presented to you that you have failed.",
        ABSOLUTE_FAILURE:
            "In your haste, you have actually created extra work for yourself.  You have "
            "misplaced, misused or broken some or all of the people, tools or materials "
            "used in this task.  You may not try again until 24 hours have passed, and "
            "that attempt will then be at a modification of -20.",
        FAILURE:
            "Your skills have deserted you, and you have wasted your effort.  "
            "Hurts, doesn't it?",
        PARTIAL_SUCCESS:
            "You know what you want to accomplish, but it just keeps falling short.  "
            "Perhaps a different approach.  Wait a full day before attempting this skill "
            "again.",
        NEAR_SUCCESS:
            "You aren't quite on, it seems.  The small details keep escaping you, but you may "
            "yet manage to catch up.  It takes a bit longer, but you may roll again with a "
            "+10 modification to finish your maneuver.",
        SUCCESS:
            "Your hands are sure, and your work is precise and artful.  You got the knack.",
        ABSOLUTE_SUCCESS:
            "Your diligence is rewarded with your latest masterwork!  Everyone can see the "
            "remarkable quality of your work, and your abilities will be more highly "
            "regarded than ever."
    }

    maneuver_result_stats = {
        BLUNDER: (-100, 2.5, -50),
        ABSOLUTE_FAILURE: (-50, 1.5, -30),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (30, 1.75, 5),
        NEAR_SUCCESS: (80, 1.5, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_crafts_table():
        """
        Set the current crafts maneuver table to use.
        :return: The maneuver table.
        """
        return CraftsManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            CraftsManeuverTable.MANEUVER_COOKING:
                [SKILL_COOKING, ],
            CraftsManeuverTable.MANEUVER_DRAFTING:
                [SKILL_DRAFTING, ],
            CraftsManeuverTable.MANEUVER_FLETCHING:
                [SKILL_FLETCHING, ],
            CraftsManeuverTable.MANEUVER_HORTICULTURE:
                [SKILL_HORTICULTURE, SKILL_HERB_LORE],
            CraftsManeuverTable.MANEUVER_LEATHER_CRAFTS:
                [SKILL_LEATHER_CRAFTS, SKILL_SEWING_WEAVING],
            CraftsManeuverTable.MANEUVER_METAL_CRAFTS:
                [SKILL_METAL_CRAFTS, SKILL_SMITHING],
            CraftsManeuverTable.MANEUVER_ROPE_MASTERY:
                [SKILL_ROPE_MASTERY, ],
            CraftsManeuverTable.MANEUVER_SCRIBING:
                [SKILL_SCRIBING, ],
            CraftsManeuverTable.MANEUVER_SERVICE:
                [SKILL_SERVICE, ],
            CraftsManeuverTable.MANEUVER_SEWING_WEAVING:
                [SKILL_SEWING_WEAVING, SKILL_LEATHER_CRAFTS],
            CraftsManeuverTable.MANEUVER_SKINNING:
                [SKILL_SKINNING, SKILL_SURVIVAL],
            CraftsManeuverTable.MANEUVER_STONE_CRAFTS:
                [SKILL_STONE_CRAFTS, ],
            CraftsManeuverTable.MANEUVER_TRAPPING:
                [SKILL_TRAPPING, SKILL_READING_TRACKS, SKILL_TRACK, SKILL_TRAP_BUILDING],
            CraftsManeuverTable.MANEUVER_WOOD_CRAFTS:
                [SKILL_WOOD_CRAFTS]

        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
