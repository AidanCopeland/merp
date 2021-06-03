# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.OutdoorEnvironmentalManeuverTable import OutdoorEnvironmentalManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

DWARF_TEXT = "Dwarf?"
DWARF_BONUS = 25

class CavingManeuverTable(OutdoorEnvironmentalManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_dwarf_frame():
            """
            Create a frame with a Checkbox indicating whether the character is a Dwarf.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, DWARF_TEXT, self.dwarf)
            trace.exit()


        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.dwarf = IntVar()
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
