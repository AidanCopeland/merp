# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.MovingManeuverTable import MovingManeuverTable, MEDIUM, HARD, \
    VERY_HARD, EXTREMELY_HARD, ABSURD, maneuver_difficulty_table_columns

import FrameUtils
import trace_log as trace

from tkinter import IntVar, StringVar, RAISED, LEFT, RIGHT, BOTH
from tkinter.ttk import Frame, Label, OptionMenu
standard_library.install_aliases()

sys.path.append('../')

ARMOUR_PROMPT = "Armour worn"
ARMOUR_CLOTHES_TEXT = "Clothes"
ARMOUR_SOFT_LEATHER_TEXT = "Soft Leather"
ARMOUR_RIGID_LEATHER_TEXT = "Rigid Leather"
ARMOUR_CHAIN_TEXT = "Chain"
ARMOUR_PLATE_TEXT = "Plate"

armour_options = (
    ARMOUR_CLOTHES_TEXT,
    ARMOUR_SOFT_LEATHER_TEXT,
    ARMOUR_RIGID_LEATHER_TEXT,
    ARMOUR_CHAIN_TEXT,
    ARMOUR_PLATE_TEXT)

armour_difficulties = {
    ARMOUR_CLOTHES_TEXT: MEDIUM,
    ARMOUR_SOFT_LEATHER_TEXT: HARD,
    ARMOUR_RIGID_LEATHER_TEXT: VERY_HARD,
    ARMOUR_CHAIN_TEXT: EXTREMELY_HARD,
    ARMOUR_PLATE_TEXT: ABSURD
}

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class SwimmingManeuverTable(MovingManeuverTable):

    def __init__(self, **kwargs):
        trace.entry()
        super(MovingManeuverTable, self).__init__(**kwargs)
        self.armour_worn = StringVar()
        self.equipment_bonus = IntVar()
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=ARMOUR_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = armour_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.armour_worn,
                ARMOUR_CLOTHES_TEXT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_equipment_frame():
            """
            Create a frame with an Entry indicating whether proper equipment is missing.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, EQUIPMENT_TEXT, self.equipment_bonus)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.equipment_bonus.set(0)
        setup_equipment_frame()

        trace.exit()

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        difficulty = armour_difficulties[self.armour_worn.get()]
        return maneuver_difficulty_table_columns[difficulty]
