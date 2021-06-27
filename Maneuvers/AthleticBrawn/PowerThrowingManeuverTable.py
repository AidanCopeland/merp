# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.AthleticBrawnManeuverTable import AthleticBrawnManeuverTable
from Maneuvers.StaticManeuverTable import \
    maneuver_difficulty_bonuses, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD

import FrameUtils
import trace_log as trace

from tkinter import StringVar
standard_library.install_aliases()
sys.path.append('../')

TARGET_BONUS_PROMPT = "Desired bonus to range"
TARGET_BONUS_10_TEXT = "+10% (Medium)"
TARGET_BONUS_25_TEXT = "+25% (Hard)"
TARGET_BONUS_50_TEXT = "+50% (Very Hard)"
TARGET_BONUS_75_TEXT = "+75% (Extremely Hard)"
TARGET_BONUS_100_TEXT = "+100% (Sheer Folly)"
TARGET_BONUS_125_TEXT = "+125% (Absurd)"
TARGET_BONUS_OPTIONS = (
    TARGET_BONUS_10_TEXT, 
    TARGET_BONUS_25_TEXT,
    TARGET_BONUS_50_TEXT,
    TARGET_BONUS_75_TEXT,
    TARGET_BONUS_100_TEXT,
    TARGET_BONUS_125_TEXT)


class PowerThrowingManeuverTable(AthleticBrawnManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(AthleticBrawnManeuverTable, self).__init__(**kwargs)
        self.target_bonus = StringVar()

        trace.exit()

    @staticmethod
    def setup_difficulty_frame(parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_target_bonus_frame():
            """
            Create a frame with an OptionMenu specifying the desired bonus
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, TARGET_BONUS_PROMPT, TARGET_BONUS_10_TEXT, self.target_bonus, *TARGET_BONUS_OPTIONS)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_target_bonus_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        target_bonus = self.target_bonus.get()
        if target_bonus == TARGET_BONUS_10_TEXT:
            trace.flow("Medium: +0")
            bonus += maneuver_difficulty_bonuses[MEDIUM]
        elif target_bonus == TARGET_BONUS_25_TEXT:
            trace.flow("Hard: -10")
            bonus += maneuver_difficulty_bonuses[HARD]
        elif target_bonus == TARGET_BONUS_50_TEXT:
            trace.flow("Very Hard: -20")
            bonus += maneuver_difficulty_bonuses[VERY_HARD]
        elif target_bonus == TARGET_BONUS_75_TEXT:
            trace.flow("Extremely Hard: -30")
            bonus += maneuver_difficulty_bonuses[EXTREMELY_HARD]
        elif target_bonus == TARGET_BONUS_100_TEXT:
            trace.flow("Sheer Folly: -50")
            bonus += maneuver_difficulty_bonuses[SHEER_FOLLY]
        elif target_bonus == TARGET_BONUS_125_TEXT:
            trace.flow("Absurd: -70")
            bonus += maneuver_difficulty_bonuses[ABSURD]

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
