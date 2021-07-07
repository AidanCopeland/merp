"""
The Power Throwing static maneuver table.

Classes:
    PowerThrowingManeuverTable
"""
# -*- coding: utf-8 -*-

import sys
from tkinter import StringVar

from maneuvers.athletic_brawn_maneuver_table import AthleticBrawnManeuverTable
from maneuvers.static_maneuver_table import \
    maneuver_difficulty_bonuses, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD

import frame_utils
import trace_log as trace

sys.path.append('../')

RANGE_BONUS_PROMPT = "Desired bonus to range"
RANGE_BONUS_10_TEXT = "+10% (Medium)"
RANGE_BONUS_25_TEXT = "+25% (Hard)"
RANGE_BONUS_50_TEXT = "+50% (Very Hard)"
RANGE_BONUS_75_TEXT = "+75% (Extremely Hard)"
RANGE_BONUS_100_TEXT = "+100% (Sheer Folly)"
RANGE_BONUS_125_TEXT = "+125% (Absurd)"
RANGE_BONUS_OPTIONS = (
    RANGE_BONUS_10_TEXT,
    RANGE_BONUS_25_TEXT,
    RANGE_BONUS_50_TEXT,
    RANGE_BONUS_75_TEXT,
    RANGE_BONUS_100_TEXT,
    RANGE_BONUS_125_TEXT)


class PowerThrowingManeuverTable(AthleticBrawnManeuverTable):
    """
    Power Throwing static maneuver table.

    Methods:
        setup_difficulty_frame(parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.range_bonus = StringVar()

        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_range_bonus_frame():
            """
            Create a frame with an OptionMenu specifying the desired bonus
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               RANGE_BONUS_PROMPT,
                                               RANGE_BONUS_10_TEXT,
                                               self.range_bonus,
                                               *RANGE_BONUS_OPTIONS)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_range_bonus_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        range_bonus = self.range_bonus.get()
        if range_bonus == RANGE_BONUS_10_TEXT:
            trace.flow("Medium: +0")
            bonus += maneuver_difficulty_bonuses[MEDIUM]
        elif range_bonus == RANGE_BONUS_25_TEXT:
            trace.flow("Hard: -10")
            bonus += maneuver_difficulty_bonuses[HARD]
        elif range_bonus == RANGE_BONUS_50_TEXT:
            trace.flow("Very Hard: -20")
            bonus += maneuver_difficulty_bonuses[VERY_HARD]
        elif range_bonus == RANGE_BONUS_75_TEXT:
            trace.flow("Extremely Hard: -30")
            bonus += maneuver_difficulty_bonuses[EXTREMELY_HARD]
        elif range_bonus == RANGE_BONUS_100_TEXT:
            trace.flow("Sheer Folly: -50")
            bonus += maneuver_difficulty_bonuses[SHEER_FOLLY]
        elif range_bonus == RANGE_BONUS_125_TEXT:
            trace.flow("Absurd: -70")
            bonus += maneuver_difficulty_bonuses[ABSURD]

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
