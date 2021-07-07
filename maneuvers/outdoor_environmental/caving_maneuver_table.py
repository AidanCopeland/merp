# -*- coding: utf-8 -*-
"""
The Caving static maneuver table.

Classes:
    CavingManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.outdoor_environmental_maneuver_table import OutdoorEnvironmentalManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


DWARF_TEXT = "Dwarf?"
DWARF_BONUS = 25


class CavingManeuverTable(OutdoorEnvironmentalManeuverTable):
    """
    Caving static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.dwarf = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_dwarf_frame():
            """
            Create a frame with a Checkbox indicating whether the character is a Dwarf.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, DWARF_TEXT, self.dwarf)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_dwarf_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.dwarf.get() == 1:
            trace.flow("Dwarf: +25")
            bonus += DWARF_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
