# -*- coding: utf-8 -*-
"""
The Spatial Location Awareness static maneuver table.

Classes:
    SLAManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.awareness_senses_maneuver_table import AwarenessSensesManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


BLIND_TEXT = "Is character effectively blind?"

BLIND_BONUS = -100


class SLAManeuverTable(AwarenessSensesManeuverTable):
    """
    Spatial Location Awareness static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.blind = IntVar()

        trace.exit()

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
            frame_utils.setup_checkbox_frame(parent_frame, BLIND_TEXT, self.blind)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
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
