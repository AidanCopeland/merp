# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Maneuvers.StaticManeuverTable import *

sys.path.append('../')


class SpecialAttacksManeuverTable(StaticManeuverTable):
    MANEUVER_COMBAT_DECEPTION = "Combat Deception"
    MANEUVER_DISARM_FOE = "Disarm Foe"
    MANEUVER_JOUSTING = "Jousting"

    maneuver_type_options = (
        MANEUVER_COMBAT_DECEPTION, MANEUVER_DISARM_FOE, MANEUVER_JOUSTING
    )

    maneuver_result_text = {
        BLUNDER:
            "Doom, despair and agony on you!  You fracture your weapon hand ("
            "a ""Medium"" Bone wound), and drop your weapon if you have one.  I hope "
            "you learned to use that backup weapon with your off hand?  No?  You "
            "don't even HAVE a backup weapon?  Gee, that's a shame.",
        ABSOLUTE_FAILURE:
            "Ho!  Ha!  Turn!  Spin!  Parry!  WHACK!  You deal yourself an 'A' Crush"
            "Critical after getting too fancy for your own good.",
        FAILURE:
            "You move with the grace of a beached manatee.  You fail your maneuver "
            "miserably.",
        PARTIAL_SUCCESS:
            "You were all lined up for a perfect textbook maneuver... too bad your "
            "opponent read the same textbook.",
        NEAR_SUCCESS:
            "Horseshoes and fireballs, buddy.  Perhaps if you tried to convince your "
            "opponent that you were really close that time, and that he should just "
            "give up...",
        SUCCESS:
            "With a deft flick of the meaty forearm, you complete your maneuver.  Nobody "
            "bothers YOU.",
        ABSOLUTE_SUCCESS:
            "Holy Shmokes, mon!  You complete your maneuver using at most 40% of the "
            "activity for this round!  Why, with a little more derring-do, you might "
            "make another attack this round!"
    }

    maneuver_result_stats = {
        BLUNDER: (-35, 1.5, -30),
        ABSOLUTE_FAILURE: (-20, 1, -15),
        FAILURE: (0, 1, -10),
        PARTIAL_SUCCESS: (20, 0.75, 0),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (160, 0.4, 30)
    }

    @staticmethod
    def select_special_attacks_table():
        """
        Set the current SpecialAttacks maneuver table to use.
        :return: The maneuver table.
        """
        return SpecialAttacksManeuverTable()
