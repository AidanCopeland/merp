# -*- coding: utf-8 -*-
"""
The Jumping moving maneuver table.

Classes:
    JumpingManeuverTable
"""
import sys
from tkinter import IntVar, StringVar, RAISED, LEFT, RIGHT, BOTH
from tkinter.ttk import Frame, Label, OptionMenu

from maneuvers.moving_maneuver_table import \
    MovingManeuverTable, ROUTINE, EASY, LIGHT, MEDIUM, HARD, \
    VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD, maneuver_difficulty_table_columns
from maneuvers import maneuver_utils

import frame_utils
import trace_log as trace

sys.path.append('../')

LENGTH_PROMPT = "Desired jump length"
LENGTH_NORMAL_TEXT = "Base jump length"
LENGTH_1_5_TEXT = "1.5 x base jump length"
LENGTH_2_TEXT = "2 x base jump length"
LENGTH_2_5_TEXT = "2.5 x base jump length"
LENGTH_3_TEXT = "3 x base jump length"
LENGTH_3_5_TEXT = "3.5 x base jump length"
LENGTH_4_TEXT = "4 x base jump length"
LENGTH_4_5_TEXT = "4.5 x base jump length"
LENGTH_5_TEXT = "5 x base jump length"
length_options = (
    LENGTH_NORMAL_TEXT,
    LENGTH_1_5_TEXT,
    LENGTH_2_TEXT,
    LENGTH_2_5_TEXT,
    LENGTH_3_TEXT,
    LENGTH_3_5_TEXT,
    LENGTH_4_TEXT,
    LENGTH_4_5_TEXT,
    LENGTH_5_TEXT)

length_difficulties = {
    LENGTH_NORMAL_TEXT: ROUTINE,
    LENGTH_1_5_TEXT: EASY,
    LENGTH_2_TEXT: LIGHT,
    LENGTH_2_5_TEXT: MEDIUM,
    LENGTH_3_TEXT: HARD,
    LENGTH_3_5_TEXT: VERY_HARD,
    LENGTH_4_TEXT: EXTREMELY_HARD,
    LENGTH_4_5_TEXT: SHEER_FOLLY,
    LENGTH_5_TEXT: ABSURD
}

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class JumpingManeuverTable(MovingManeuverTable):
    """
    Jumping moving maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        difficulty_table_column(self)
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.desired_length = StringVar()
        self.equipment_bonus = IntVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=LENGTH_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = length_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.desired_length,
                LENGTH_2_5_TEXT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        difficulty = length_difficulties[self.desired_length.get()]
        return maneuver_difficulty_table_columns[difficulty]

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        maneuver_utils.setup_maneuver_table_frames_for_equipment(self, parent_frame)

    def skill_type_bonus(self):
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
