# -*- coding: utf-8 -*-
import sys

from StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')


class CraftsManeuverTable(StaticManeuverTable):
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
        Set the current Crafts maneuver table to use.
        :return: The maneuver table.
        """
        return CraftsManeuverTable()


