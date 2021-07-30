# -*- coding: utf-8 -*-
"""
The Rapid Fire moving maneuver table.

Classes:
    RapidFireManeuverTable
"""
import sys
from tkinter import StringVar, RAISED, LEFT, RIGHT, BOTH
from tkinter.ttk import Frame, Label, OptionMenu

from maneuvers.moving_maneuver_table import MovingManeuverTable, HARD, EXTREMELY_HARD, \
    maneuver_difficulty_table_columns, FMB

import frame_utils
import trace_log as trace

sys.path.append('../')

WEAPON_PROMPT = "Type of weapon used"

WEAPON_SLING_TEXT = "Sling"
WEAPON_SHORT_BOW_TEXT = "Short Bow"
WEAPON_COMPOSITE_BOW_TEXT = "Composite Bow"
WEAPON_LONGBOW_TEXT = "Longbow"
WEAPON_LIGHT_CROSSBOW_TEXT = "Light crossbow"
WEAPON_HEAVY_CROSSBOW_TEXT = "Heavy crossbow"

weapon_options = (
    WEAPON_SLING_TEXT, WEAPON_SHORT_BOW_TEXT, WEAPON_COMPOSITE_BOW_TEXT, WEAPON_LONGBOW_TEXT,
    WEAPON_LIGHT_CROSSBOW_TEXT, WEAPON_HEAVY_CROSSBOW_TEXT)

RATE_OF_FIRE_PROMPT = "Desired rate of fire"
ROF_3_RND_TEXT = "Every 3 rounds"
ROF_2_RND_TEXT = "Every 2 rounds"
ROF_1_RND_TEXT = "Every round"
ROF_TWICE_TEXT = "Twice a round"


class RapidFireManeuverTable(MovingManeuverTable):
    """
    Rapid Fire moving maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        difficulty_table_column(self)
        maneuver_resolution(self, roll)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.weapon_type = StringVar()
        self.weapon_type.set(WEAPON_SHORT_BOW_TEXT)
        self.rate_of_fire = StringVar()
        self.rate_of_fire.set(ROF_1_RND_TEXT)
        self.rate_of_fire_options = (ROF_1_RND_TEXT, ROF_TWICE_TEXT)
        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to this skill.
        :param parent_frame: The owning frame.
        """
        trace.entry()

        def setup_weapon_frame():
            """
            Create a frame with an OptionMenu indicating the weapon selected.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(
                parent_frame,
                WEAPON_PROMPT,
                WEAPON_SHORT_BOW_TEXT,
                self.weapon_type,
                *weapon_options)
            trace.exit()

        def setup_rate_of_fire_frame():
            """
            Create a frame with an OptionMenu indicating the desired rate of fire.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(
                parent_frame,
                RATE_OF_FIRE_PROMPT,
                ROF_1_RND_TEXT,
                self.rate_of_fire,
                *self.rate_of_fire_options)
            trace.exit()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_weapon_frame()
        setup_rate_of_fire_frame()
        self.weapon_type.trace("w", self.weapon_type_update_callback)
        parent_frame.pack()

        trace.exit()

    def weapon_type_update_callback(self, *_args):
        """
        Callback when the weapon type has changed to update the possible rates of fire.
        """
        trace.entry()

        self.redraw_maneuver_skill_frames(self.perception_type.get())

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
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.maneuver_table import ManeuverResult

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
