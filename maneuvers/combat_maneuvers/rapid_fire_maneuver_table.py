# -*- coding: utf-8 -*-
"""
The Rapid Fire moving maneuver table.

Classes:
    RapidFireManeuverTable
"""
import sys
from tkinter import StringVar

from maneuvers.moving_maneuver_table import MovingManeuverTable, ROUTINE, MEDIUM, HARD, VERY_HARD, \
    EXTREMELY_HARD, SHEER_FOLLY, ABSURD, maneuver_difficulty_table_columns, FMB

import frame_utils
import trace_log as trace

sys.path.append('../')

WEAPON_PROMPT = "Type of weapon used"

WEAPON_SHORT_BOW_TEXT = "Short Bow"
WEAPON_COMPOSITE_BOW_TEXT = "Composite Bow"
WEAPON_LONGBOW_TEXT = "Longbow"
WEAPON_LIGHT_CROSSBOW_TEXT = "Light crossbow"
WEAPON_HEAVY_CROSSBOW_TEXT = "Heavy crossbow"

weapon_options = (
    WEAPON_SHORT_BOW_TEXT, WEAPON_COMPOSITE_BOW_TEXT, WEAPON_LONGBOW_TEXT,
    WEAPON_LIGHT_CROSSBOW_TEXT, WEAPON_HEAVY_CROSSBOW_TEXT)

RELOAD_TIME_PROMPT = "Desired reload time"
RELOAD_2_RND_TEXT = "2 rounds"
RELOAD_1_RND_TEXT = "1 round"
RELOAD_1_RND_UNSKILLED_TEXT = "1 round (unskilled)"
RELOAD_0_RND_TEXT = "Fire every round"
RELOAD_0_RND_UNSKILLED_TEXT = "Fire every round (unskilled)"
RELOAD_TWICE_RND_TEXT = "Fire twice a round"
RELOAD_TWICE_RND_UNSKILLED_TEXT = "Fire twice a round (unskilled)"

short_bow_options = (
    RELOAD_0_RND_TEXT, RELOAD_0_RND_UNSKILLED_TEXT, RELOAD_TWICE_RND_TEXT,
    RELOAD_TWICE_RND_UNSKILLED_TEXT)

composite_bow_options = (
    RELOAD_0_RND_TEXT, RELOAD_0_RND_UNSKILLED_TEXT, RELOAD_TWICE_RND_TEXT,
    RELOAD_TWICE_RND_UNSKILLED_TEXT)

longbow_options = (RELOAD_0_RND_TEXT, RELOAD_0_RND_UNSKILLED_TEXT, RELOAD_TWICE_RND_TEXT,
                   RELOAD_TWICE_RND_UNSKILLED_TEXT)

light_crossbow_options = (RELOAD_1_RND_TEXT, RELOAD_1_RND_UNSKILLED_TEXT, RELOAD_0_RND_TEXT)

heavy_crossbow_options = (RELOAD_1_RND_TEXT, RELOAD_1_RND_UNSKILLED_TEXT, RELOAD_0_RND_TEXT,
                          RELOAD_0_RND_UNSKILLED_TEXT)

SHORT_BOW_DEFAULT = RELOAD_0_RND_TEXT
COMPOSITE_BOW_DEFAULT = RELOAD_0_RND_TEXT
LONGBOW_DEFAULT = RELOAD_0_RND_TEXT
LIGHT_CROSSBOW_DEFAULT = RELOAD_1_RND_TEXT
HEAVY_CROSSBOW_DEFAULT = RELOAD_1_RND_TEXT

weapon_reload_options = {
    WEAPON_SHORT_BOW_TEXT: short_bow_options,
    WEAPON_COMPOSITE_BOW_TEXT: composite_bow_options,
    WEAPON_LONGBOW_TEXT: longbow_options,
    WEAPON_LIGHT_CROSSBOW_TEXT: light_crossbow_options,
    WEAPON_HEAVY_CROSSBOW_TEXT: heavy_crossbow_options}

weapon_reload_defaults = {
    WEAPON_SHORT_BOW_TEXT: SHORT_BOW_DEFAULT,
    WEAPON_COMPOSITE_BOW_TEXT: COMPOSITE_BOW_DEFAULT,
    WEAPON_LONGBOW_TEXT: LONGBOW_DEFAULT,
    WEAPON_LIGHT_CROSSBOW_TEXT: LIGHT_CROSSBOW_DEFAULT,
    WEAPON_HEAVY_CROSSBOW_TEXT: HEAVY_CROSSBOW_DEFAULT}

reload_time_difficulties = {
    WEAPON_SHORT_BOW_TEXT:
        {RELOAD_0_RND_TEXT: MEDIUM,
         RELOAD_0_RND_UNSKILLED_TEXT: ROUTINE,
         RELOAD_TWICE_RND_TEXT: VERY_HARD,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: ROUTINE},
    WEAPON_COMPOSITE_BOW_TEXT:
        {RELOAD_0_RND_TEXT: HARD,
         RELOAD_0_RND_UNSKILLED_TEXT: ROUTINE,
         RELOAD_TWICE_RND_TEXT: VERY_HARD,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: ROUTINE},
    WEAPON_LONGBOW_TEXT:
        {RELOAD_0_RND_TEXT: VERY_HARD,
         RELOAD_0_RND_UNSKILLED_TEXT: ROUTINE,
         RELOAD_TWICE_RND_TEXT: EXTREMELY_HARD,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: MEDIUM},
    WEAPON_LIGHT_CROSSBOW_TEXT:
        {RELOAD_1_RND_TEXT: MEDIUM,
         RELOAD_1_RND_UNSKILLED_TEXT: ROUTINE,
         RELOAD_0_RND_TEXT: EXTREMELY_HARD},
    WEAPON_HEAVY_CROSSBOW_TEXT:
        {RELOAD_1_RND_TEXT: EXTREMELY_HARD,
         RELOAD_1_RND_UNSKILLED_TEXT: VERY_HARD,
         RELOAD_0_RND_TEXT: ABSURD,
         RELOAD_0_RND_UNSKILLED_TEXT: SHEER_FOLLY}
}

self_inflicted_modifiers = {
    WEAPON_SHORT_BOW_TEXT:
        {RELOAD_0_RND_TEXT: 0,
         RELOAD_0_RND_UNSKILLED_TEXT: -10,
         RELOAD_TWICE_RND_TEXT: -30,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: -60},
    WEAPON_COMPOSITE_BOW_TEXT:
        {RELOAD_0_RND_TEXT: 0,
         RELOAD_0_RND_UNSKILLED_TEXT: -20,
         RELOAD_TWICE_RND_TEXT: -40,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: -70},
    WEAPON_LONGBOW_TEXT:
        {RELOAD_0_RND_TEXT: 0,
         RELOAD_0_RND_UNSKILLED_TEXT: -30,
         RELOAD_TWICE_RND_TEXT: -40,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: -70},
    WEAPON_LIGHT_CROSSBOW_TEXT:
        {RELOAD_1_RND_TEXT: 0,
         RELOAD_1_RND_UNSKILLED_TEXT: -20,
         RELOAD_0_RND_TEXT: -40},
    WEAPON_HEAVY_CROSSBOW_TEXT:
        {RELOAD_1_RND_TEXT: 0,
         RELOAD_1_RND_UNSKILLED_TEXT: -20,
         RELOAD_0_RND_TEXT: -10,
         RELOAD_0_RND_UNSKILLED_TEXT: -30}
}

is_maneuver_required = {
    WEAPON_SHORT_BOW_TEXT:
        {RELOAD_0_RND_TEXT: True,
         RELOAD_0_RND_UNSKILLED_TEXT: False,
         RELOAD_TWICE_RND_TEXT: True,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: False},
    WEAPON_COMPOSITE_BOW_TEXT:
        {RELOAD_0_RND_TEXT: True,
         RELOAD_0_RND_UNSKILLED_TEXT: False,
         RELOAD_TWICE_RND_TEXT: True,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: False},
    WEAPON_LONGBOW_TEXT:
        {RELOAD_0_RND_TEXT: True,
         RELOAD_0_RND_UNSKILLED_TEXT: False,
         RELOAD_TWICE_RND_TEXT: True,
         RELOAD_TWICE_RND_UNSKILLED_TEXT: True},
    WEAPON_LIGHT_CROSSBOW_TEXT:
        {RELOAD_1_RND_TEXT: True,
         RELOAD_1_RND_UNSKILLED_TEXT: False,
         RELOAD_0_RND_TEXT: True},
    WEAPON_HEAVY_CROSSBOW_TEXT:
        {RELOAD_1_RND_TEXT: True,
         RELOAD_1_RND_UNSKILLED_TEXT: True,
         RELOAD_0_RND_TEXT: True,
         RELOAD_0_RND_UNSKILLED_TEXT: True}
}


class RapidFireManeuverTable(MovingManeuverTable):
    """
    Rapid Fire moving maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        setup_maneuver_table_frames(self, parent_frame)
        weapon_type_update_callback(self, *_args)
        reload_time_update_callback(self, *_args)
        difficulty_table_column(self)
        maneuver_resolution(self, roll)
    """
    def __init__(self, parent_maneuver_table, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.parent_frame = None
        self.parent_maneuver_table = parent_maneuver_table
        self.weapon_type = StringVar()
        self.weapon_type.set(WEAPON_SHORT_BOW_TEXT)
        self.reload_time = StringVar()
        self.reload_time.set(SHORT_BOW_DEFAULT)
        self.reload_time_options = short_bow_options
        self.maneuver_required = True
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to this skill.
        :param parent_frame: The owning frame.
        """
        trace.entry()

        self.parent_frame = parent_frame

        frame_utils.destroy_frame_objects(self.parent_frame)
        self.__setup_rate_of_fire_frame()
        self.__setup_weapon_frame()
        self.weapon_type.trace("w", self.weapon_type_update_callback)
        self.reload_time.trace("w", self.reload_time_update_callback)
        self.parent_frame.pack()

        trace.exit()

    def weapon_type_update_callback(self, *_args):
        """
        Callback when the weapon type has changed to update the possible rates of fire.
        """
        trace.entry()

        frame_utils.destroy_frame_objects(self.parent_frame)
        weapon_type = self.weapon_type.get()

        self.reload_time.set(weapon_reload_defaults.get(weapon_type))
        self.reload_time_options = (weapon_reload_options.get(weapon_type))
        trace.detail("Reload time is %r" % self.reload_time.get())
        trace.detail("Reload time options are %s" % str(self.reload_time_options))
        self.__setup_rate_of_fire_frame()

        trace.detail("Weapon type is %s" % self.weapon_type.get())
        self.__setup_weapon_frame()

        trace.exit()

    def __setup_weapon_frame(self):
        """
        Create a frame with an OptionMenu indicating the weapon selected.
        """
        trace.entry()
        frame_utils.setup_optionmenu_frame(
            self.parent_frame,
            WEAPON_PROMPT,
            self.weapon_type.get(),
            self.weapon_type,
            *weapon_options)
        trace.exit()

    def __setup_rate_of_fire_frame(self):
        """
        Create a frame with an OptionMenu indicating the desired rate of fire.
        """
        trace.entry()
        frame_utils.setup_optionmenu_frame(
            self.parent_frame,
            RELOAD_TIME_PROMPT,
            self.reload_time.get(),
            self.reload_time,
            *self.reload_time_options)
        trace.exit()

    def reload_time_update_callback(self, *_args):
        """
        If the reload time selected does not require a maneuver, update the output text
        accordingly.
        """
        if (is_maneuver_required[self.weapon_type.get()])[self.reload_time.get()]:
            trace.flow("Maneuver required")
            self.maneuver_required = True
            text = ""
            self.parent_maneuver_table.result_text_callback(text)
        else:
            trace.flow("Unskilled - maneuver not required")
            self.maneuver_required = False
            self_inflicted_modifier = \
                (self_inflicted_modifiers[self.weapon_type.get()])[self.reload_time.get()]
            text = "No maneuver required.\nTotal modifier to attack %d." % self_inflicted_modifier
            self.parent_maneuver_table.result_text_callback(text)

    def difficulty_table_column(self):
        """
        Determine the column in the difficulty table to use for resolution of the maneuver.
        """
        trace.entry()
        difficulty = (reload_time_difficulties[self.weapon_type.get()])[self.reload_time.get()]
        trace.detail("Difficulty %s" % difficulty)

        trace.exit()
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

        self_inflicted_modifier = \
            (self_inflicted_modifiers[self.weapon_type.get()])[self.reload_time.get()]

        if self.maneuver_required:
            result_row = self.get_result_row(roll)
            column = self.difficulty_table_column()
            result = result_row[column]
        else:
            result = 100

        maneuver_modifier = result - 100

        trace.detail("Maneuver result is %d" % result)
        trace.detail("Modifier to OB from maneuver result is %d" % maneuver_modifier)
        trace.detail("Self inflicted modifier is %d" % self_inflicted_modifier)
        trace.detail("Total modifier is %d" % (maneuver_modifier + self_inflicted_modifier))
        fumble = False

        if result == FMB:
            text = "Maneuver failed"
            fumble = True
        else:
            text = "Total modifier to attack %d" % (maneuver_modifier + self_inflicted_modifier)

        return ManeuverResult(text, 100, 1, 0, fumble)
