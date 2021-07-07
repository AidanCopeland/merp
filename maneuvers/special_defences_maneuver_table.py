# -*- coding: utf-8 -*-
"""
The Special Defences static maneuver table.

Classes:
    SpecialDefencesManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS

sys.path.append('../')


class SpecialDefencesManeuverTable(StaticManeuverTable):
    """
    Special Defences static maneuver table.

    Methods:
        select_special_defences_table(maneuver_type)
    """
    MANEUVER_ADRENAL_TOUGHNESS = "Adrenal Toughness"

    maneuver_type_options = (
        MANEUVER_ADRENAL_TOUGHNESS,
    )

    maneuver_result_text = {
        BLUNDER:
            "You are so disorientated that you not only fail, you are stunned for "
            "two rounds.  Due to your shattered self-confidence, future attempts to "
            "use this skill will receive a -30 modification (non-cumulative) until you "
            "achieve a result of Absolute Success on this table.",
        ABSOLUTE_FAILURE:
            "Bad form!  You are poorly positioned, and automatically receive an 'A' "
            "Impact critical (or raise the severity of any critical received by one, if "
            "applicable).  Your teacher is turning in his grave.",
        FAILURE:
            "You fail to summon the inner focus necessary for this feat, and receive "
            "no benefit or effects from your attempt.  Well, it worked in the dojo...",
        PARTIAL_SUCCESS:
            "You are distracted at the critical moment.  If not in combat, you may abort "
            "your attempt and try again next round.  Perhaps you should switch to decaff.",
        NEAR_SUCCESS:
            "Darn toothache!  If in combat, you fail.  If not in combat, you may "
            "immediately make another roll at +10 to achieve full concentration.",
        SUCCESS:
            "Ommmmmmmmm.  You receive the full benefits of your maneuver.  Good work, "
            "Grasshopper.",
        ABSOLUTE_SUCCESS:
            "You may attempt this skill again next round without preparation (i.e., you "
            "may operate at 100% activity this round and still use this skill next "
            "round).  Your friends are impressed."
    }

    maneuver_result_stats = {
        BLUNDER: (-30, 2, -20),
        ABSOLUTE_FAILURE: (-15, 1, -10),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (30, 1.25, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.75, 30)
    }

    @staticmethod
    def select_special_defences_table():
        """
        Set the current SpecialDefences maneuver table to use.
        :return: The maneuver table.
        """
        return SpecialDefencesManeuverTable()
