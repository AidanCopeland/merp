# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.MovingManeuverTable import MovingManeuverTable, ROUTINE, EASY, LIGHT, MEDIUM, HARD, \
    VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD, maneuver_difficulty_table_columns

import FrameUtils
import trace_log as trace

from tkinter import IntVar, StringVar, RAISED, LEFT, RIGHT, BOTH
from tkinter.ttk import Frame, Label, OptionMenu
standard_library.install_aliases()

sys.path.append('../')

WIDTH_PROMPT = "Width of surface"
THREE_FEET_TEXT = "3 feet"
TWO_FEET_TEXT = "2 feet"
ONE_FOOT_TEXT = "1 foot"
SIX_INCHES_TEXT = "6 inches"
THREE_INCHES_TEXT = "3 inches"
ONE_INCH_TEXT = "1 inch"
HALF_INCH_TEXT = "0.5 inches"
POINT_TWO_INCH_TEXT = "0.2 inches"
POINT_ONE_INCH_TEXT = "0.1 inches"

width_options = (
    THREE_FEET_TEXT,
    TWO_FEET_TEXT,
    ONE_FOOT_TEXT,
    SIX_INCHES_TEXT,
    THREE_INCHES_TEXT,
    ONE_INCH_TEXT,
    HALF_INCH_TEXT,
    POINT_TWO_INCH_TEXT,
    POINT_ONE_INCH_TEXT)

width_difficulties = {
    THREE_FEET_TEXT: ROUTINE,
    TWO_FEET_TEXT: EASY,
    ONE_FOOT_TEXT: LIGHT,
    SIX_INCHES_TEXT: MEDIUM,
    THREE_INCHES_TEXT: HARD,
    ONE_INCH_TEXT: VERY_HARD,
    HALF_INCH_TEXT: EXTREMELY_HARD,
    POINT_TWO_INCH_TEXT: SHEER_FOLLY,
    POINT_ONE_INCH_TEXT: ABSURD}

WIND_TEXT = "Set bonus of 0 to -70 based on wind (no wind to hurricane force)"
SURFACE_TEXT = "Set bonus of +30 to -70 based on surface (sticky to icy slick)"
BALANCING_POLE_TEXT = "Does character have a balancing pole?"
TIGHTROPE_SOLE_SHOES_TEXT = "Does character have tightrope sole shoes?"
BALANCING_POLE_BONUS = 10
TIGHTROPE_SOLE_SHOES_BONUS = 10


class TightropeWalkingManeuverTable(MovingManeuverTable):

    def __init__(self, **kwargs):
        trace.entry()
        super(MovingManeuverTable, self).__init__(**kwargs)
        self.surface_width = StringVar()
        self.wind_bonus = IntVar()
        self.surface_bonus = IntVar()
        self.balancing_pole = IntVar()
        self.tightrope_sole_shoes = IntVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=WIDTH_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = width_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.surface_width,
                SIX_INCHES_TEXT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_wind_frame():
            """
            Create a frame with an Entry indicating penalty based on the wind.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, WIND_TEXT, self.wind_bonus)
            trace.exit()

        def setup_surface_frame():
            """
            Create a frame with an Entry indicating bonus or penalty based on the surface.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, SURFACE_TEXT, self.surface_bonus)
            trace.exit()

        def setup_balancing_pole_frame():
            """
            Create a frame with a Checkbox indicating whether the character has a balancing pole.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, BALANCING_POLE_TEXT, self.balancing_pole)
            trace.exit()

        def setup_tightrope_sole_shoes_frame():
            """
            Create a frame with a Checkbox indicating whether the character has tightrope sole shoes.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, TIGHTROPE_SOLE_SHOES_TEXT, self.tightrope_sole_shoes)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.wind_bonus.set(0)
        self.surface_bonus.set(0)
        setup_wind_frame()
        setup_surface_frame()
        setup_balancing_pole_frame()
        setup_tightrope_sole_shoes_frame()

        trace.exit()

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        difficulty = width_difficulties[self.surface_width.get()]
        return maneuver_difficulty_table_columns[difficulty]

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        trace.detail("Wind bonus: %d" % self.wind_bonus.get())
        bonus += self.wind_bonus.get()

        trace.detail("Surface bonus: %d" % self.surface_bonus.get())
        bonus += self.surface_bonus.get()

        if self.balancing_pole.get() == 1:
            trace.flow("Balancing pole")
            bonus += BALANCING_POLE_BONUS

        if self.tightrope_sole_shoes.get() == 1:
            trace.flow("Tightrope sole shoes")
            bonus += TIGHTROPE_SOLE_SHOES_BONUS

        trace.exit()
        return bonus
