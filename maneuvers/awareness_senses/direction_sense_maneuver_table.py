# -*- coding: utf-8 -*-
"""
The Direction Sense static maneuver table.

Classes:
    DirectionSenseManeuverTable
"""
import sys
from tkinter import IntVar, StringVar

from maneuvers.awareness_senses_maneuver_table import AwarenessSensesManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


MAGNETIC_FIELD_PROMPT = "Local magnetic field"
NORMAL_FIELD_TEXT = "Normal"
STRONG_NATURAL_FIELD_TEXT = "Strong natural field"
STRONG_UNNATURAL_FIELD_TEXT = "Strong unnatural field"
WEAK_NATURAL_FIELD_TEXT = "Weak natural field"
WEAK_UNNATURAL_FIELD_TEXT = "Weak unnatural field"
NEVER_BEEN_TEXT = "Never been in area before?"
MAGNETIC_FIELD_OPTIONS = (NORMAL_FIELD_TEXT, STRONG_NATURAL_FIELD_TEXT, STRONG_UNNATURAL_FIELD_TEXT,
                          WEAK_NATURAL_FIELD_TEXT, WEAK_UNNATURAL_FIELD_TEXT)

STRONG_NATURAL_FIELD_BONUS = 30
STRONG_UNNATURAL_FIELD_BONUS = -30
WEAK_NATURAL_FIELD_BONUS = -5
WEAK_UNNATURAL_FIELD_BONUS = -10
NEVER_BEEN_BONUS = -50


class DirectionSenseManeuverTable(AwarenessSensesManeuverTable):
    """
    Direction Sense static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.magnetic_field = StringVar()
        self.never_been = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_magnetic_field_frame():
            """
            Create a frame with an OptionMenu specifying the local magnetic field.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               MAGNETIC_FIELD_PROMPT,
                                               NORMAL_FIELD_TEXT,
                                               self.magnetic_field,
                                               *MAGNETIC_FIELD_OPTIONS)
            trace.exit()

        def setup_never_been_frame():
            """
            Create a frame with a Checkbox indicating whether the character has never been
            to the area before.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, NEVER_BEEN_TEXT, self.never_been)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_magnetic_field_frame()
        setup_never_been_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.never_been.get() == 1:
            trace.flow("Never been in area before: -50")
            bonus += NEVER_BEEN_BONUS

        magnetic_field = self.magnetic_field.get()
        if magnetic_field == STRONG_NATURAL_FIELD_TEXT:
            trace.flow("Strong natural field: +30")
            bonus += STRONG_NATURAL_FIELD_BONUS
        elif magnetic_field == STRONG_UNNATURAL_FIELD_TEXT:
            trace.flow("Strong unnatural field: -30")
            bonus += STRONG_UNNATURAL_FIELD_BONUS
        elif magnetic_field == WEAK_NATURAL_FIELD_TEXT:
            trace.flow("Weak natural field: -5")
            bonus += WEAK_NATURAL_FIELD_BONUS
        elif magnetic_field == WEAK_UNNATURAL_FIELD_TEXT:
            trace.flow("Weak unnatural field: -10")
            bonus += WEAK_UNNATURAL_FIELD_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
