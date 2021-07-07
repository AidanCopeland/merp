# -*- coding: utf-8 -*-
"""
The Athletic/Endurance static maneuver table.

Classes:
    AthleticEnduranceManeuverTable
"""
from __future__ import absolute_import
import sys
from tkinter import IntVar

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from maneuvers import maneuver_utils
import trace_log as trace

sys.path.append('../')

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class AthleticEnduranceManeuverTable(StaticManeuverTable):
    """
    Athletic/Endurance static maneuver table.

    Methods:
        select_athletic_endurance_table(maneuver_type)
        setup_maneuver_table_frames(self, parent_frame)
        table_bonus(self)
    """
    MANEUVER_ATHLETIC_GAMES_ENDURANCE = "Athletic Games (Endurance)"
    MANEUVER_DISTANCE_RUNNING = "Distance Running"
    MANEUVER_ROWING = "Rowing"
    MANEUVER_SCALING = "Scaling"
    MANEUVER_SPRINTING = "Sprinting"
    MANEUVER_SWIMMING = "Swimming"

    maneuver_type_options = (
        MANEUVER_ATHLETIC_GAMES_ENDURANCE,
        MANEUVER_DISTANCE_RUNNING,
        MANEUVER_ROWING,
        MANEUVER_SCALING,
        MANEUVER_SPRINTING,
        MANEUVER_SWIMMING
    )

    maneuver_result_text = {
        BLUNDER:
            "You've seriously injured yourself through muscle stress and severe fatigue.  "
            "Take a Medium muscular injury in an appropriate muscle group (GM's discretion to "
            "location and penalty). "
            "Good luck, buddy,",
        ABSOLUTE_FAILURE:
            "You're in trouble!  You expend 2x normal exhaustion points due to a virus you've been "
            "fighting, and find yourself in danger (whether a bad fall or slipping while climbing, "
            "etc.). "
            "Any maneuver you make to extricate yourself from the situation will be at a -10 "
            "modification.",
        FAILURE:
            "Exhaustion claims you.  You utterly mismanage your resources, and expend 1.5x the "
            "normal exhaustion points, as well as failing in your maneuver. You do manage to reach "
            "safety, if it is nearby and necessary.",
        PARTIAL_SUCCESS:
            "A good start, but you've misjudged the length of time necessary to finish.",
        NEAR_SUCCESS:
            "You've reached the wall... keep going!  If appropriate, roll next round at a +10 "
            "modification to get your second wind.",
        SUCCESS:
            "Good wind, a cool sweat... you look marvellous, darling.",
        ABSOLUTE_SUCCESS:
            "Your incredible body control leaves you stamina to spare at the end of your "
            "endeavour. You're ready for the Decathlon."
    }

    maneuver_result_stats = {
        BLUNDER: (5, 1.75, -20),
        ABSOLUTE_FAILURE: (10, 1.5, -10),
        FAILURE: (25, 1.5, -10),
        PARTIAL_SUCCESS: (30, 1.25, 0),
        NEAR_SUCCESS: (80, 0.8, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.equipment_bonus = IntVar()

        trace.exit()

    @staticmethod
    def select_athletic_endurance_table(maneuver_type):
        """
        Set the current athletic/endurance maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.athletic_endurance.swimming_maneuver_table import SwimmingManeuverTable
        from maneuvers.athletic_endurance.athletic_endurance_moving_maneuver_table import \
            AthleticEnduranceMovingManeuverTable

        if maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_ATHLETIC_GAMES_ENDURANCE:
            trace.flow("Athletic Games maneuver")
            trace.exit()
            return AthleticEnduranceManeuverTable()

        elif maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_DISTANCE_RUNNING:
            trace.flow("Distance Running maneuver")
            trace.exit()
            return AthleticEnduranceMovingManeuverTable()

        elif maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_ROWING:
            trace.flow("Rowing maneuver")
            trace.exit()
            return AthleticEnduranceMovingManeuverTable()

        elif maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_SCALING:
            trace.flow("Scaling maneuver")
            trace.exit()
            return AthleticEnduranceMovingManeuverTable()

        elif maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_SPRINTING:
            trace.flow("Sprinting maneuver")
            trace.exit()
            return AthleticEnduranceMovingManeuverTable()

        else:
            trace.flow("Swimming maneuver")
            assert maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_SWIMMING
            trace.exit()
            return SwimmingManeuverTable()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        maneuver_utils.setup_maneuver_table_frames_for_equipment(self, parent_frame)

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        return maneuver_utils.table_bonus_from_equipment(self)
