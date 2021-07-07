# -*- coding: utf-8 -*-
"""
The Subterfuge/Attack static maneuver table.

Classes:
    SubterfugeAttackManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS

sys.path.append('../')


class SubterfugeAttackManeuverTable(StaticManeuverTable):
    """
    Subterfuge/Attack static maneuver table.

    Methods:
        select_subterfuge_attack_table(maneuver_type)
    """
    MANEUVER_AMBUSH = "Ambush"
    MANEUVER_SILENT_KILL = "Silent Kill"

    maneuver_type_options = (
        MANEUVER_AMBUSH, MANEUVER_SILENT_KILL
    )

    maneuver_result_text = {
        BLUNDER:
            "This will all seem funny years from now, if you survive.  "
            "Not only do you alert your target, you fumble your weapon.  Your target "
            "may make an attack with full bonuses for surprise in addition to "
            "whatever penalties you accrue for the fumble result.  Next time you'll "
            "think about a stand-up fight, won't you?",
        ABSOLUTE_FAILURE:
            "Way to go, O Nimble One!  Not only do you alert your target, you fumble "
            "your weapon.  Roll on the appropriate column of the appropriate Fumble "
            "table.",
        FAILURE:
            "Subterfuge is apparently an alien concept to you.  You fail utterly in "
            "your maneuver.",
        PARTIAL_SUCCESS:
            "As you begin your attack, you fail to mask the sound of your approach.  "
            "Your target may make an Alertness (or Situational Awareness or Sense "
            "Ambush if appropriate) static maneuver modified by +30 to sense your "
            "approach.  If you are noticed, your maneuver will fail.",
        NEAR_SUCCESS:
            "As you are nearly upon your target, something warns him.  You may make a "
            "Moving Maneuver (modified by AG bonus + 10) to close with your target and "
            "succeed in your maneuver before he can react.  If you fail this MM, your "
            "maneuver will fail.",
        SUCCESS:
            "Now you have him, Cato!  Your maneuver works perfectly.  Be gentle.",
        ABSOLUTE_SUCCESS:
            "You strike like a viper, out of shadow.  You may operate as if you had 5 "
            "more ranks in this skill for the length of this maneuver.  Make them "
            "count."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 1.5, -30),
        ABSOLUTE_FAILURE: (-20, 1.5, -15),
        FAILURE: (0, 1.5, 0),
        PARTIAL_SUCCESS: (30, 0.7, 0),
        NEAR_SUCCESS: (80, 1, 5),
        SUCCESS: (100, 1, 10),
        ABSOLUTE_SUCCESS: (120, 0.8, 20)
    }

    @staticmethod
    def select_subterfuge_attack_table():
        """
        Set the current SubterfugeAttack maneuver table to use.
        :return: The maneuver table.
        """
        return SubterfugeAttackManeuverTable()
