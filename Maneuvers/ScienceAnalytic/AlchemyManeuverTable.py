# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.ScienceAnalyticManeuverTable import ScienceAnalyticManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

EQUIPMENT_TEXT = "Reduction to bonus caused by lack of suitable equipment (up to -70)"

class AlchemyManeuverTable(ScienceAnalyticManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_equipment_penalty_frame():
            """
            Create a frame with an Entry indicating penalty caused by lack of supplies.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, EQUIPMENT_TEXT, self.equipment_penalty)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.equipment_penalty = IntVar()
        setup_equipment_penalty_frame()
        self.equipment_penalty.set(0)

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus -= self.equipment_penalty.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
