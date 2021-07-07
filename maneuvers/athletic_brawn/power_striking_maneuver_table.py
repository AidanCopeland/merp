# -*- coding: utf-8 -*-
"""
The Power Striking static maneuver table.

Classes:
    PowerStrikingManeuverTable
"""
import sys
from tkinter import StringVar

from maneuvers.athletic_brawn_maneuver_table import AthleticBrawnManeuverTable
from maneuvers.static_maneuver_table import \
    maneuver_difficulty_bonuses, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD
import frame_utils
import trace_log as trace

sys.path.append('../')


BLOW_BONUS_PROMPT = "Desired bonus to blow"
BLOW_BONUS_10_TEXT = "+10 (Medium)"
BLOW_BONUS_20_TEXT = "+20 (Hard)"
BLOW_BONUS_30_TEXT = "+30 (Very Hard)"
BLOW_BONUS_40_TEXT = "+40 (Extremely Hard)"
BLOW_BONUS_50_TEXT = "+50 (Sheer Folly)"
BLOW_BONUS_60_TEXT = "+60 (Absurd)"
BLOW_BONUS_OPTIONS = (
    BLOW_BONUS_10_TEXT,
    BLOW_BONUS_20_TEXT,
    BLOW_BONUS_30_TEXT,
    BLOW_BONUS_40_TEXT,
    BLOW_BONUS_50_TEXT,
    BLOW_BONUS_60_TEXT)


class PowerStrikingManeuverTable(AthleticBrawnManeuverTable):
    """
    Power Striking static maneuver table.

    Methods:
        select_difficulty_frame(parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.blow_bonus = StringVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_blow_bonus_frame():
            """
            Create a frame with an OptionMenu specifying the desired bonus
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               BLOW_BONUS_PROMPT,
                                               BLOW_BONUS_10_TEXT,
                                               self.blow_bonus,
                                               *BLOW_BONUS_OPTIONS)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_blow_bonus_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        blow_bonus = self.blow_bonus.get()
        if blow_bonus == BLOW_BONUS_10_TEXT:
            trace.flow("Medium: +0")
            bonus += maneuver_difficulty_bonuses[MEDIUM]
        elif blow_bonus == BLOW_BONUS_20_TEXT:
            trace.flow("Hard: -10")
            bonus += maneuver_difficulty_bonuses[HARD]
        elif blow_bonus == BLOW_BONUS_30_TEXT:
            trace.flow("Very Hard: -20")
            bonus += maneuver_difficulty_bonuses[VERY_HARD]
        elif blow_bonus == BLOW_BONUS_40_TEXT:
            trace.flow("Extremely Hard: -30")
            bonus += maneuver_difficulty_bonuses[EXTREMELY_HARD]
        elif blow_bonus == BLOW_BONUS_50_TEXT:
            trace.flow("Sheer Folly: -50")
            bonus += maneuver_difficulty_bonuses[SHEER_FOLLY]
        elif blow_bonus == BLOW_BONUS_60_TEXT:
            trace.flow("Absurd: -70")
            bonus += maneuver_difficulty_bonuses[ABSURD]

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
