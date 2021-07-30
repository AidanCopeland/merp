# -*- coding: utf-8 -*-
"""
The Drug Tolerance static maneuver table.

Classes:
    DrugToleranceManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE, PARTIAL_SUCCESS, \
    NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from maneuvers.self_control_maneuver_table import SelfControlManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')

ADDICTION_LEVEL_TEXT = "Addiction level:"
BONUS_TEXT = "Bonus to roll: 20 + bonuses from previous rolls - " \
             "amount by which original addiction roll was failed"


class DrugToleranceManeuverTable(SelfControlManeuverTable):
    """
    Drug Tolerance static maneuver table.

    Methods:
        setup_maneuver_table_frames(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        setup_difficulty_frame(self, parent_frame)
        skill_type_bonus(self)
    """

    maneuver_result_text = {
        BLUNDER:
            "Your level of addiction is unchanged.",
        ABSOLUTE_FAILURE:
            "Your level of addiction is unchanged.",
        FAILURE:
            "Your level of addiction is unchanged.",
        PARTIAL_SUCCESS:
            "Your level of addiction is unchanged.",
        NEAR_SUCCESS:
            "Re-roll with a one-off bonus of +20.",
        SUCCESS:
            "Your level of addiction is unchanged.  "
            "Roll all subsequent withdrawal rolls with a (cumulative) bonus of +20 until you have "
            "completed withdrawal from this drug.",
        ABSOLUTE_SUCCESS:
            "Your level of addiction to this drug has reduced by 1.  "
            "Roll all subsequent withdrawal rolls with a (cumulative) bonus of +20 until you have "
            "completed withdrawal from this drug."
    }

    maneuver_result_stats = {
        BLUNDER: (0, 1, -20),
        ABSOLUTE_FAILURE: (0, 1, -20),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (0, 1, 0),
        NEAR_SUCCESS: (0, 1, 20),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (100, 1, 20)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.addiction_level = IntVar()
        self.previous_roll_bonus = IntVar()

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up frames specific to the skill category.
        This overrides the skill category base: this skill does not use the skill category frames.
        """
        frame_utils.destroy_frame_objects(parent_frame)

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """
        def setup_addiction_level_frame():
            """
            Create a frame with an Entry to specify the character's addiction level.
            """
            frame_utils.setup_entry_frame(parent_frame, ADDICTION_LEVEL_TEXT, self.addiction_level)

        def setup_bonus_frame():
            """
            Create a frame with an Entry to specify the bonus based on previous rolls.
            """
            frame_utils.setup_entry_frame(parent_frame, BONUS_TEXT, self.previous_roll_bonus)

        frame_utils.destroy_frame_objects(parent_frame)
        self.addiction_level.set(0)
        self.previous_roll_bonus.set(0)

        setup_addiction_level_frame()
        setup_bonus_frame()

    def setup_difficulty_frame(self, parent_frame):
        """
        Set up frames used to determine the maneuver difficulty.  There are no frames.
        """
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += self.previous_roll_bonus.get() - self.addiction_level.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
