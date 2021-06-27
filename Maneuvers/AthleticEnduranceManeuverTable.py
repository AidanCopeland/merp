# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Maneuvers.StaticManeuverTable import *

import trace_log as trace
from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class AthleticEnduranceManeuverTable(StaticManeuverTable):
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
        BLUNDER: "You've seriously injured yourself through muscle stress and severe fatigue.  Take a Medium muscular "
                 "injury in an appropriate muscle group (GM's discretion to location and penalty). "
                 "Good luck, buddy,",
        ABSOLUTE_FAILURE: "You're in trouble!  You expend 2x normal exhaustion points due to a virus you've been "
                          "fighting, and find yourself in danger (whether a bad fall or slipping while "
                          "climbing, etc.). "
                          "Any maneuver you make to extricate yourself from the situation will be at a -10 "
                          "modification.",
        FAILURE: "Exhaustion claims you.  You utterly mismanage your resources, and expend 1.5x the normal "
                 "exhaustion points, as well as failing in your maneuver.  You do manage to reach safety, if "
                 "it is nearby and necessary.",
        PARTIAL_SUCCESS: "A good start, but you've misjudged the length of time necessary to finish.",
        NEAR_SUCCESS: "You've reached the wall... keep going!  If appropriate, roll next round at a +10 "
                      "modification to get your second wind.",
        SUCCESS: "Good wind, a cool sweat... you look marvellous, darling.",
        ABSOLUTE_SUCCESS: "Your incredible body control leaves you stamina to spare at the end of your endeavour.  "
                          "You're ready for the Decathlon."
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
        super(StaticManeuverTable, self).__init__(**kwargs)
        self.equipment_bonus = IntVar()

        trace.exit()

    @staticmethod
    def select_athletic_endurance_table(maneuver_type):
        """
        Set the current athletic/endurance maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        from Maneuvers.AthleticEndurance.SwimmingManeuverTable import SwimmingManeuverTable
        from Maneuvers.AthleticEndurance.AthleticEnduranceMovingManeuverTable import \
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

        elif maneuver_type == AthleticEnduranceManeuverTable.MANEUVER_SWIMMING:
            trace.flow("Swimming maneuver")
            trace.exit()
            return SwimmingManeuverTable()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_equipment_frame():
            """
            Create a frame with an Entry indicating whether proper equipment is missing.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, EQUIPMENT_TEXT, self.equipment_bonus)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.equipment_bonus.set(0)
        setup_equipment_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        trace.detail("Equipment bonus: %d" % self.equipment_bonus.get())
        bonus += self.equipment_bonus.get()

        trace.exit()
        return bonus
