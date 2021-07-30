# -*- coding: utf-8 -*-
"""
The Poison Tolerance static maneuver table.

Classes:
    PoisonToleranceManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE, PARTIAL_SUCCESS, \
    NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from maneuvers.self_control_maneuver_table import SelfControlManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')

BONUS_TEXT = "Bonus to roll: 30 - amount by which original Resistance Roll was failed"


class PoisonToleranceManeuverTable(SelfControlManeuverTable):
    """
    Poison Tolerance static maneuver table.

    Methods:
        setup_maneuver_table_frames(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        setup_difficulty_frame(self, parent_frame)
        skill_type_bonus
    """

    maneuver_result_text = {
        BLUNDER:
            "The poison takes its normal effect.",
        ABSOLUTE_FAILURE:
            "The poison takes its normal effect.",
        FAILURE:
            "The poison takes its normal effect.",
        PARTIAL_SUCCESS:
            "The poison takes its normal effect.",
        NEAR_SUCCESS:
            "The effect of the poison is reduced by 1 level.  "
            "This may result in the poison having no effect.",
        SUCCESS:
            "The effect of the poison is reduced by 2 levels.  "
            "This may result in the poison having no effect.",
        ABSOLUTE_SUCCESS:
            "The effect of the poison is reduced by 3 levels.  "
            "This may result in the poison having no effect.",
    }

    maneuver_result_stats = {
        BLUNDER: (0, 1, 0),
        ABSOLUTE_FAILURE: (0, 1, 0),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (0, 1, 0),
        NEAR_SUCCESS: (0, 1, 0),
        SUCCESS: (0, 1, 0),
        ABSOLUTE_SUCCESS: (0, 1, 0)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.resistance_failure_bonus = IntVar()

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
        def setup_bonus_frame():
            """
            Create a frame with an Entry to specify the bonus based on the amount the
            Resistance Roll was failed by.
            """
            frame_utils.setup_entry_frame(parent_frame, BONUS_TEXT, self.resistance_failure_bonus)

        frame_utils.destroy_frame_objects(parent_frame)
        self.resistance_failure_bonus.set(0)

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

        bonus += self.resistance_failure_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
