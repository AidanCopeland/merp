# -*- coding: utf-8 -*-
"""
The Rappelling moving maneuver table.

Classes:
    RappellingManeuverTable
"""
import sys
from tkinter import IntVar, StringVar, RAISED, LEFT, RIGHT, BOTH
from tkinter.ttk import Frame, Label, OptionMenu

from maneuvers.moving_maneuver_table import MovingManeuverTable, LIGHT, MEDIUM, HARD, \
    VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, maneuver_difficulty_table_columns

import frame_utils
import trace_log as trace



sys.path.append('../')

PACE_PROMPT = "Desired pace to descend"
WALK_TEXT = "Walking"
FAST_WALK_TEXT = "Fast walk/jog"
RUN_TEXT = "Run"
FAST_RUN_TEXT = "Fast run/sprint"
FAST_SPRINT_TEXT = "Fast sprint"
DASH_TEXT = "Dash"

pace_options = (
    WALK_TEXT,
    FAST_WALK_TEXT,
    RUN_TEXT,
    FAST_RUN_TEXT,
    FAST_SPRINT_TEXT,
    DASH_TEXT)

pace_difficulties = {
    WALK_TEXT: LIGHT,
    FAST_WALK_TEXT: MEDIUM,
    RUN_TEXT: HARD,
    FAST_RUN_TEXT: VERY_HARD,
    FAST_SPRINT_TEXT: EXTREMELY_HARD,
    DASH_TEXT: SHEER_FOLLY
}

GEAR_TEXT = "Does character have climbing gear (as well as a rope)?"
GEAR_BONUS = 20
GEAR_PENALTY = 15


class RappellingManeuverTable(MovingManeuverTable):
    """
    Rappelling moving maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        difficulty_table_column(self)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.descent_pace = StringVar()
        self.gear = IntVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=PACE_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = pace_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.descent_pace,
                WALK_TEXT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_gear_frame():
            """
            Create a frame with a Checkbox indicating whether the character has climbing gear.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, GEAR_TEXT, self.gear)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_gear_frame()

        trace.exit()

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        difficulty = pace_difficulties[self.descent_pace.get()]
        return maneuver_difficulty_table_columns[difficulty]

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.gear.get() == 1:
            trace.flow("Has gear")
            bonus += GEAR_BONUS
        else:
            trace.flow("Does not have gear")
            bonus -= GEAR_PENALTY

        trace.exit()
        return bonus
