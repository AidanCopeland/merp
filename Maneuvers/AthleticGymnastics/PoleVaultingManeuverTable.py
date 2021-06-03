# -*- coding: utf-8 -*-
import sys

from Maneuvers.MovingManeuverTable import MovingManeuverTable, ROUTINE, EASY, LIGHT, MEDIUM, HARD, \
    VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD, maneuver_difficulty_table_columns

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar, RAISED, LEFT, RIGHT, BOTH
from ttk import Frame, Label, OptionMenu

sys.path.append('../')

HEIGHT_PROMPT = "Height or width to vault"
FOUR_FEET_TEXT = "4'"
SIX_FEET_TEXT = "6'"
EIGHT_FEET_TEXT = "8'"
TEN_FEET_TEXT = "10'"
TWELVE_FEET_TEXT = "12'"
FIFTEEN_FEET_TEXT = "15'"
EIGHTEEN_FEET_TEXT = "18'"
TWENTY_TWO_FEET_TEXT = "22'"
TWENTY_FIVE_FEET_TEXT = "25'"

height_options = (
    FOUR_FEET_TEXT,
    SIX_FEET_TEXT,
    EIGHT_FEET_TEXT,
    TEN_FEET_TEXT,
    TWELVE_FEET_TEXT,
    FIFTEEN_FEET_TEXT,
    EIGHTEEN_FEET_TEXT,
    TWENTY_TWO_FEET_TEXT,
    TWENTY_FIVE_FEET_TEXT)

height_difficulties = {
    FOUR_FEET_TEXT: ROUTINE,
    SIX_FEET_TEXT: EASY,
    EIGHT_FEET_TEXT: LIGHT,
    TEN_FEET_TEXT: MEDIUM,
    TWELVE_FEET_TEXT: HARD,
    FIFTEEN_FEET_TEXT: VERY_HARD,
    EIGHTEEN_FEET_TEXT: EXTREMELY_HARD,
    TWENTY_TWO_FEET_TEXT: SHEER_FOLLY,
    TWENTY_FIVE_FEET_TEXT: ABSURD
}


class PoleVaultingManeuverTable(MovingManeuverTable):

    def __init__(self, **kwargs):
        trace.entry()
        super(MovingManeuverTable, self).__init__(**kwargs)
        self.vault_height = StringVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=HEIGHT_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = height_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.vault_height,
                TEN_FEET_TEXT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        difficulty = height_difficulties[self.vault_height.get()]
        return maneuver_difficulty_table_columns[difficulty]
