# -*- coding: utf-8 -*-
"""
The Subterfuge/Stealth static maneuver table.

Classes:
    SubterfugeStealthManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.subterfuge_skills import \
    SKILL_STALK_HIDE, SKILL_PICK_POCKETS, SKILL_TRICKERY, SKILL_DUPING
import trace_log as trace

sys.path.append('../')


class SubterfugeStealthManeuverTable(StaticManeuverTable):
    """
    Subterfuge/Stealth static maneuver table.

    Methods:
        select_subterfuge_stealth_table(maneuver_type)
    """
    MANEUVER_HIDE = "Hide"
    MANEUVER_PICK_POCKETS = "Pick Pockets"
    MANEUVER_STALK = "Stalk"
    MANEUVER_TRICKERY = "Trickery"

    maneuver_type_options = (
        MANEUVER_HIDE, MANEUVER_PICK_POCKETS, MANEUVER_STALK, MANEUVER_TRICKERY
    )

    maneuver_result_text = {
        BLUNDER:
            "The 'O' of surprise you have on your face might be endearing in other "
            "circumstances.  At the present time, however, you are going to have to "
            "work mighty fast to avoid the consequences of your ineptitude.  "
            "If you are within range, your quarry may take a melee attack on your with "
            "modifiers for position and surprise.  In any case, you are seen by all "
            "within range.  Your reputation is shot.",
        ABSOLUTE_FAILURE:
            "You fall, and instinctively try to catch yourself on the nearest object "
            "or person (up to and including your target).  It's pretty obvious what you "
            "were trying to do.  After taking your +10 Fall/Crush attack, you'll have "
            "to deal with your target.",
        FAILURE:
            "You stand out like a sore thumb.  Your maneuver fails, and your quarry is "
            "staring right at you.  What now?",
        PARTIAL_SUCCESS:
            "Your target spots you, but doesn't immediately suspect you of any "
            "wrongdoing.  If you talk fast, you might even get out of this alive.",
        NEAR_SUCCESS:
            "It's one of those moments that freezes your heart.  Your target has "
            "paused, thinking something seems wrong.  Roll again with a modification of "
            "+10 to successfully ride out this harrying moment.",
        SUCCESS:
            "Aren't we the nimble one?  You succeed in your maneuver.",
        ABSOLUTE_SUCCESS:
            "Surely your quarry must be blind!  You may make another maneuver under "
            "cover of your impenetrable aura of stealth, so long as the maneuver does "
            "not take more than 50% activity.  Regardless of the success of that "
            "maneuver, this one succeeds brilliantly."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -30),
        ABSOLUTE_FAILURE: (-25, 1.75, -10),
        FAILURE: (0, 1.5, 0),
        PARTIAL_SUCCESS: (30, 1.25, 5),
        NEAR_SUCCESS: (70, 1.5, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.5, 30)
    }

    @staticmethod
    def select_subterfuge_stealth_table(maneuver_type):
        """
        Set the current SubterfugeStealth maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.subterfuge_stealth.hide_maneuver_table import HideManeuverTable
        from maneuvers.subterfuge_stealth.stalk_maneuver_table import StalkManeuverTable

        if maneuver_type == SubterfugeStealthManeuverTable.MANEUVER_HIDE:
            trace.flow("Hide")
            return HideManeuverTable()
        elif maneuver_type == SubterfugeStealthManeuverTable.MANEUVER_STALK:
            trace.flow("Stalk")
            return StalkManeuverTable()
        else:
            trace.flow("Subterfuge/Stealth")
            return SubterfugeStealthManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            SubterfugeStealthManeuverTable.MANEUVER_HIDE:
                [SKILL_STALK_HIDE, ],
            SubterfugeStealthManeuverTable.MANEUVER_PICK_POCKETS:
                [SKILL_PICK_POCKETS, ],
            SubterfugeStealthManeuverTable.MANEUVER_STALK:
                [SKILL_STALK_HIDE, ],
            SubterfugeStealthManeuverTable.MANEUVER_TRICKERY:
                [SKILL_TRICKERY, SKILL_DUPING]
        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
