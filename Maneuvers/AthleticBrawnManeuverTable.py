# -*- coding: utf-8 -*-
import sys

from StaticManeuverTable import *
from Tkinter import IntVar

import trace_log as trace

sys.path.append('../')

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class AthleticBrawnManeuverTable(StaticManeuverTable):
    MANEUVER_ATHLETIC_GAMES_BRAWN = "Athletic Games (Brawn)"
    MANEUVER_JUMPING = "Jumping"
    MANEUVER_POWER_STRIKING = "Power-striking"
    MANEUVER_POWER_THROWING = "Power-throwing"
    MANEUVER_WEIGHT_LIFTING = "Weight-lifting"

    maneuver_type_options = (
        MANEUVER_ATHLETIC_GAMES_BRAWN, MANEUVER_JUMPING, MANEUVER_POWER_STRIKING, MANEUVER_POWER_THROWING, MANEUVER_WEIGHT_LIFTING
    )

    maneuver_result_text = {
        BLUNDER: "Agony!  Mere strength cannot overcome bad leverage; you may have snapped a bone or severed a muscle; "
                 "take a 'B' Crush or Slash critical and add 5 rounds of stun.  You will operate at a -25 modification "
                 "(-50 to this skill) until this ""Medium"" injury has fully healed.  "
                 "You failed the maneuver, by the way.",
        ABSOLUTE_FAILURE: "Sloppy, sloppy... you planted poorly and pulled a muscle; you will operate at a -20 "
                          "modification (-40 to this skill) until this ""Light"" injury has fully healed.  "
                          "Oh, and you failed.",
        FAILURE: "Who are you trying to impress?  You just sound constipated.  You failed your maneuver.",
        PARTIAL_SUCCESS: "You have potential... perhaps some kind of training regimen...? "
                         "Might solve that sand-in-the-face problem...",
        NEAR_SUCCESS: "Argh, so close!  If appropriate, you may make a roll to finish the maneuver next round at a +10 "
                      "modification.",
        SUCCESS: "Unnff!  Ah, nice work!  Your mighty thews have carried the day.  You feel the burn.",
        ABSOLUTE_SUCCESS: "You have a place waiting for you at the circus, Herc."
    }

    maneuver_result_stats = {
        BLUNDER: (5, 1.5, -25),
        ABSOLUTE_FAILURE: (10, 1.2, -15),
        FAILURE: (15, 1, -10),
        PARTIAL_SUCCESS: (30, 1, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_athletic_brawn_table(maneuver_type):
        """
        Set the current athletic/brawn maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        from Maneuvers.AthleticBrawn.JumpingManeuverTable import JumpingManeuverTable
        from Maneuvers.AthleticBrawn.PowerStrikingManeuverTable import PowerStrikingManeuverTable
        from Maneuvers.AthleticBrawn.PowerThrowingManeuverTable import PowerThrowingManeuverTable
        from Maneuvers.AthleticBrawn.WeightLiftingManeuverTable import WeightLiftingManeuverTable

        if maneuver_type == AthleticBrawnManeuverTable.MANEUVER_ATHLETIC_GAMES_BRAWN:
            trace.flow("Athletic Games maneuver")
            trace.exit()
            return AthleticBrawnManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_JUMPING:
            trace.flow("Jumping maneuver")
            trace.exit()
            return JumpingManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_POWER_STRIKING:
            trace.flow("Power-striking maneuver")
            trace.exit()
            return PowerStrikingManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_POWER_THROWING:
            trace.flow("Power-throwing maneuver")
            trace.exit()
            return PowerThrowingManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_WEIGHT_LIFTING:
            trace.flow("Weight-lifting maneuver")
            trace.exit()
            return WeightLiftingManeuverTable()

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
        self.equipment_bonus = IntVar()
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