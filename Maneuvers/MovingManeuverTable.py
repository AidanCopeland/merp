# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from future import standard_library
from builtins import object
from past.utils import old_div
import sys

from tkinter import LEFT, RIGHT, BOTH, RAISED, StringVar, IntVar
from tkinter.ttk import Frame, Label, OptionMenu
from collections import namedtuple

import dice
import trace_log as trace
import FrameUtils

from Tables.MovingManeuverFumbleTable import MovingManeuverFumbleTable
standard_library.install_aliases()

sys.path.append('../')


MANEUVER_DIFFICULTY_LABEL_TEXT = "Maneuver difficulty: "
LIMB_OUT_TEXT = "Character has one limb out"
DOWN_TEXT = "Character is down"
PARTIAL_COMPLETION_TEXT = "Maneuver can be partially completed"

ManeuverDifficulty = namedtuple("ManeuverDifficulty", "text_string table_column")

ROUTINE = "Routine"
EASY = "Easy"
LIGHT = "Light"
MEDIUM = "Medium"
HARD = "Hard"
VERY_HARD = "Very Hard"
EXTREMELY_HARD = "Extremely Hard"
SHEER_FOLLY = "Sheer Folly"
ABSURD = "Absurd"

DIFFICULTY_DEFAULT = MEDIUM

maneuver_difficulty_options = (
    ROUTINE, EASY, LIGHT, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD)

maneuver_difficulty_table_columns = {
    ROUTINE: 0,
    EASY: 1,
    LIGHT: 2,
    MEDIUM: 3,
    HARD: 4,
    VERY_HARD: 5,
    EXTREMELY_HARD: 6,
    SHEER_FOLLY: 7,
    ABSURD: 8
}

maneuver_fumble_bonuses = {
    ROUTINE: -50,
    EASY: -35,
    LIGHT: -20,
    MEDIUM: -10,
    HARD: 0,
    VERY_HARD: 5,
    EXTREMELY_HARD: 10,
    SHEER_FOLLY: 15,
    ABSURD: 20
}

FMB = -99


class MovingManeuverTable(object):

    result_row_index_lookup = [
        0,  # -150 down; -31; 0
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # -149 to -100; -30 to -21; 1 to 10
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  # -99 to -50; -20 to -11; 11 to 20
        3, 3, 3, 3, 3,  # -49 to -25; -10 to -6; 21 to 25
        4, 4, 4, 4, 4,  # -24 to 0; -5 to -1; 26 to 30
        5, 5, 5, 5,  # 1 to 20; 0 to 3; 31 to 34
        6, 6, 6, 6,  # 21 to 40; 4 to 7; 35 to 38
        7, 7, 7,  # 41 to 55; 8 to 10; 39 to 41
        8, 8,  # 56 to 65; 11 to 12; 42 to 43
        9, 9,  # 66 to 75; 13 to 14; 44 to 45
        10, 10,  # 76 to 85; 15 to 16; 46 to 47
        11, 11,  # 86 to 95; 17 to 18; 48 to 49
        12, 12,  # 96 to 105; 19 to 20; 50 to 51
        13, 13,  # 106 to 115; 21 to 22; 52 to 53
        14, 14,  # 116 to 125; 23 to 24; 54 to 55
        15, 15,  # 126 to 135; 25 to 26; 56 to 57
        16, 16,  # 136 to 145; 27 to 28; 58 to 59
        17, 17,  # 146 to 155; 29 to 30; 60 to 61
        18, 18,  # 156 to 165; 31 to 32; 62 to 63
        19, 19, 19, 19,  # 166 to 185; 33 to 36; 64 to 67
        20, 20, 20, 20, 20, 20, 20, 20,  # 186 to 225; 37 to 44; 68 to 75
        21, 21, 21, 21, 21, 21, 21, 21, 21, 21,  # 226 to 275; 45 to 54; 76 to 85
        22,  # 276 up; 55; 86
    ]

    maneuver_table_entries = [
        (FMB, FMB, FMB, FMB, FMB, FMB, FMB, FMB, FMB),  # -150 down
         (10, FMB, FMB, FMB, FMB, FMB, FMB, FMB, FMB),  # -149 to -100
         (30,  10, FMB, FMB, FMB, FMB, FMB, FMB, FMB),  # -99 to -50
         (50,  30,  10, FMB, FMB, FMB, FMB, FMB, FMB),  # -49 to -25
         (70,  50,  30,   5, FMB, FMB, FMB, FMB, FMB),  # -24 to 0
         (80,  60,  50,  10,   5, FMB, FMB, FMB, FMB),  # 1 to 20
         (90,  70,  60,  20,  10,   5, FMB, FMB, FMB),  # 21 to 40
        (100,  80,  70,  30,  20,  10,   5, FMB, FMB),  # 41 to 55
        (100,  90,  80,  40,  30,  20,  10, FMB, FMB),  # 56 to 65
        (100, 100,  90,  50,  40,  30,  20,   5, FMB),  # 66 to 75
        (100, 100, 100,  60,  50,  40,  30,  10, FMB),  # 76 to 85
        (100, 100, 100,  70,  60,  50,  40,  20,   5),  # 86 to 95
        (110, 100, 100,  80,  70,  60,  50,  25,  10),  # 96 to 105
        (110, 110, 100,  90,  80,  70,  60,  30,  20),  # 106 to 115
        (120, 110, 110, 100,  90,  80,  70,  40,  30),  # 116 to 125
        (120, 120, 110, 100, 100,  90,  80,  50,  40),  # 126 to 135
        (130, 120, 120, 110, 100, 100,  90,  60,  50),  # 136 to 145
        (130, 130, 120, 110, 110, 100, 100,  70,  60),  # 146 to 155
        (140, 130, 130, 120, 110, 110, 100,  80,  70),  # 156 to 165
        (140, 140, 130, 120, 120, 110, 110,  90,  80),  # 166 to 185
        (150, 140, 140, 130, 120, 120, 110, 100,  90),  # 186 to 225
        (150, 150, 140, 130, 130, 120, 120, 100, 100),  # 226 to 275
        (160, 150, 150, 140, 130, 130, 120, 110, 110),  # 276 up
    ]

    def __init__(self, **kwargs):
        trace.entry()
        dice.randomize()
        self.maneuver_difficulty = StringVar()
        self.maneuver_difficulty_options = maneuver_difficulty_options
        self.maneuver_difficulty_selector = \
            OptionMenu(
                None,
                self.maneuver_difficulty,
                MEDIUM,
                *self.maneuver_difficulty_options)
        self.maneuver_type = kwargs.get('maneuver_type', None)
        self.limb_out = IntVar()
        self.down = IntVar()
        self.partial_completion = IntVar()
        self.fumble_roll = StringVar()

        trace.exit()

    def get_result_row(self, dice_result):
        """
        Converts the dice result into the row to read the result from in the Moving
        Maneuver Table.
        Note that the results this gives differ from the standard Moving Maneuver
        Table for negative results.  For simplicity, the upper end of the band boundaries
        are at multiples of 5 (-25, -50, -100, -150) instead of at the stated values
        (-26, -51, -101, -151)
        :param dice_result: The dice result, including any modifiers.
        :return: The index of the row to read from.
        """
        trace.entry()

        trace.detail("Original result %d" % dice_result)

        # The range of possible results is -150 to 276.
        stage_1_dice_result = min(max(-150, dice_result), 276)
        trace.detail("Stage 1 result %d" % stage_1_dice_result)

        # Subtract 1 then divide the result by 5 (using integer division) to reduce the number of results to handle.
        # This is Python 2, so any fractions are discarded (rounding down).
        stage_2_dice_result = old_div((stage_1_dice_result - 1), 5)
        trace.detail("Stage 2 result %d" % stage_2_dice_result)

        # Update the result so that zero represents the lowest possible result.
        stage_3_dice_result = stage_2_dice_result + 31
        trace.detail("Stage 3 result %d" % stage_3_dice_result)
        assert(stage_3_dice_result >= 0)
        assert(stage_3_dice_result <= 86)

        # Obtain the index of the row to read
        result_row_index = self.result_row_index_lookup[stage_3_dice_result]

        trace.exit()
        return self.maneuver_table_entries[result_row_index]

    def setup_difficulty_frame(self, parent_frame):
        """
        Creates a frame to allow selection of the maneuver difficulty using an OptionMenu widget.
        """
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=MANEUVER_DIFFICULTY_LABEL_TEXT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = maneuver_difficulty_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                MEDIUM,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        trace.entry()

        def setup_limb_out_frame():
            """
            Create a frame with a Checkbox indicating whether the character has
            one limb out.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, LIMB_OUT_TEXT, self.limb_out)
            trace.exit()

        def setup_down_frame():
            """
            Create a frame with a Checkbox indicating whether the character is down.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, DOWN_TEXT, self.down)
            trace.exit()

        def setup_partial_completion_frame():
            """
            Create a frame with a Checkbox indicating whether the maneuver can be partially
            completed.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, PARTIAL_COMPLETION_TEXT, self.partial_completion)
            trace.exit()

        FrameUtils.destroy_frame_objects(parent_frame)

        self.partial_completion.set(True)
        setup_limb_out_frame()
        setup_down_frame()
        setup_partial_completion_frame()
        parent_frame.pack()

        trace.exit()

    @staticmethod
    def setup_maneuver_skill_frames(parent_frame):
        """
        Set up the frames specific to the chosen skill.
        """
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        parent_frame.pack()

        trace.exit()

    @staticmethod
    def setup_maneuver_fumble_frame(parent_frame):
        """
        Set up the frames used for resolving fumbles.
        """
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        parent_frame.pack()

        trace.exit()

    @staticmethod
    def difficulty_bonus():
        """
        Returns zero because moving maneuvers do not use a difficulty bonus.
        """
        return 0

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        trace.detail("Limb out? %r" % self.limb_out.get())
        if self.limb_out.get() == 1:
            trace.flow("Limb out: -30")
            bonus -= 30

        if self.down.get() == 1:
            trace.flow("Character down: -70")
            bonus -= 70

        trace.detail("Bonus to skill is %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def skill_type_bonus():
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        trace.exit()
        return 0

    def maneuver_resolution(self, roll):
        """
        Resolve the maneuver based on the modified roll.
        This method may carry out side-effects based on the resolution of the maneuver.
        :param roll: The modified roll.
        :return: A ManeuverResult containing the text output of the resolution and
        statistics about the effectiveness of the maneuver.
        """
        from .ManeuverTable import ManeuverResult

        result_row = self.get_result_row(roll)

        column = self.difficulty_table_column()
        result = result_row[column]
        fumble = False

        if result == FMB:
            text = "Maneuver failed"
            fumble = True
        elif result >= 100:
            text = "Maneuver succeeded"
            if self.partial_completion.get() == 1 and result > 100:
                text += ", normal result exceeded by %d percent" % (result - 100)
        else:
            if self.partial_completion.get() == 1:
                text = "Maneuver partially completed, %d percent complete" % result
            else:
                partial_success = dice.d100()
                trace.detail("Rolled %d, result was %d" % (partial_success, result))
                if partial_success <= result:
                    text = "Maneuver succeeded"
                else:
                    text = "Maneuver failed"

        return ManeuverResult(text, 100, 1, 0, fumble)

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        return maneuver_difficulty_table_columns[self.maneuver_difficulty.get()]

    def resolve_fumble(self, roll):
        """
        Resolve a fumble for a moving maneuver.
        :param roll: The fumble roll made.
        :return: The text to return.
        """
        fumble_table = MovingManeuverFumbleTable()
        return fumble_table.resolve_fumble(roll, self.maneuver_difficulty.get())
