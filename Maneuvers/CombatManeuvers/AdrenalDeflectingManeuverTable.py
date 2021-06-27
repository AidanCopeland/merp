# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.MovingManeuverTable import MovingManeuverTable, EXTREMELY_HARD, SHEER_FOLLY, \
    maneuver_difficulty_table_columns, FMB

import FrameUtils
import trace_log as trace

from tkinter import StringVar, RAISED, LEFT, RIGHT, BOTH
from tkinter.ttk import Frame, Label, OptionMenu
standard_library.install_aliases()

sys.path.append('../')

WEAPON_PROMPT = "Type of weapon faced"
THROWN_WEAPON_TEXT = "Thrown"
MISSILE_WEAPON_TEXT = "Missile"

weapon_options = (
    THROWN_WEAPON_TEXT,
    MISSILE_WEAPON_TEXT)

weapon_difficulties = {
    THROWN_WEAPON_TEXT: EXTREMELY_HARD,
    MISSILE_WEAPON_TEXT: SHEER_FOLLY
}


class AdrenalDeflectingManeuverTable(MovingManeuverTable):

    def __init__(self, **kwargs):
        trace.entry()
        super(MovingManeuverTable, self).__init__(**kwargs)
        self.weapon_type = StringVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=WEAPON_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = weapon_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.weapon_type,
                MISSILE_WEAPON_TEXT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        difficulty = weapon_difficulties[self.weapon_type.get()]
        return maneuver_difficulty_table_columns[difficulty]

    def maneuver_resolution(self, roll):
        """
        Resolve the maneuver based on the modified roll.
        This method may carry out side-effects based on the resolution of the maneuver.
        :param roll: The modified roll.
        :return: A ManeuverResult containing the text output of the resolution and
        statistics about the effectiveness of the maneuver.
        """
        from Maneuvers.ManeuverTable import ManeuverResult

        result_row = self.get_result_row(roll)

        column = self.difficulty_table_column()
        result = result_row[column]
        fumble = False

        if result == FMB:
            text = "Maneuver failed"
            fumble = True
        else:
            text = "Subtract %d from attack" % result

        return ManeuverResult(text, 100, 1, 0, fumble)
