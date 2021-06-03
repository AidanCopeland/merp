# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.AwarenessSensesManeuverTable import AwarenessSensesManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

BLIND_TEXT = "Is character effectively blind?"

BLIND_BONUS = -100


class SLAManeuverTable(AwarenessSensesManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_blind_frame():
            """
            Create a frame with a Checkbox indicating whether the character is effectively
            blind.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, BLIND_TEXT, self.blind)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.blind = IntVar()
        setup_blind_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.blind.get() == 1:
            trace.flow("Blind: -100")
            bonus += BLIND_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
