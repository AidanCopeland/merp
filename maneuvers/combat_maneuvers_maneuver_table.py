# -*- coding: utf-8 -*-
"""
The Combat Maneuvers static maneuver table.

Classes:
    CombatManeuversManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
import trace_log as trace

sys.path.append('../')


class CombatManeuversManeuverTable(StaticManeuverTable):
    """
    Combat Maneuvers static maneuver table.

    Methods:
        select_combat_maneuvers_table(maneuver_type)
        setup_maneuver_table_frames(self, parent_frame)
        table_bonus(self)
    """
    MANEUVER_ADRENAL_DEFLECTING = "Adrenal Deflecting"
    MANEUVER_QUICKDRAW = "Quickdraw"
    MANEUVER_SWASHBUCKLING = "Swashbuckling"

    maneuver_type_options = (
        MANEUVER_ADRENAL_DEFLECTING, MANEUVER_QUICKDRAW, MANEUVER_SWASHBUCKLING
    )

    maneuver_result_text = {
        BLUNDER:
            "Are you on drugs?  Your opponent actually laughs as you fall all over "
            "yourself, dealing yourself a +30 Fall/Crush attack and a ""Medium"" Bone "
            "(-30 penalty) injury to a random location.  You are stunned for two rounds.  "
            "You'd better hope this was just for show...",
        ABSOLUTE_FAILURE:
            "It's unfortunate that you didn't listen to your first instinct, which was "
            "_not to try this!!_  You deal yourself an injury (i.e., Critical) appropriate "
            "to the maneuver you were attempting (GM's discretion), and hopefully gain a "
            "little wisdom.",
        FAILURE:
            "What do you think this is, a game?  You're not capable of that kind of maneuver.  "
            "You fail.",
        PARTIAL_SUCCESS:
            "Well, perhaps practice will eventually make perfect.  If not in combat, you may "
            "abort your maneuver and try again next round.  Otherwise, you're in for a pretty "
            "hairy round of combat.",
        NEAR_SUCCESS:
            "You almost had it!  An involuntary curse escapes your lips in frustration.  If "
            "appropriate, you may make another attempt next round with a +10 modification.",
        SUCCESS:
            "Your long training pays off as you step through your maneuver with an almost "
            "instinctual ease.",
        ABSOLUTE_SUCCESS:
            "There's a rhythm to everything, and you have caught the rhythm of this maneuver.  "
            "You may operate at a modification of +20 (non-cumulative) to this skill until "
            "you receive a result of Absolute Failure or Blunder on this table."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -30),
        ABSOLUTE_FAILURE: (-25, 1.5, -15),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (20, 1.25, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.75, 30)
    }

    @staticmethod
    def select_combat_maneuvers_table(maneuver_type):
        """
        Set the current combat maneuvers maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from .combat_maneuvers.adrenal_deflecting_maneuver_table import \
            AdrenalDeflectingManeuverTable
        from .combat_maneuvers.quickdraw_maneuver_table import QuickdrawManeuverTable

        if maneuver_type == CombatManeuversManeuverTable.MANEUVER_ADRENAL_DEFLECTING:
            trace.flow("Adrenal Deflecting maneuver")
            return AdrenalDeflectingManeuverTable()
        elif maneuver_type == CombatManeuversManeuverTable.MANEUVER_QUICKDRAW:
            trace.flow("Quickdraw maneuver")
            return QuickdrawManeuverTable()
        else:
            trace.flow("Combat maneuvers")
            return CombatManeuversManeuverTable()
