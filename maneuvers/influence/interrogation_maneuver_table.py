# -*- coding: utf-8 -*-
"""
The Interrogation static maneuver table.

Classes:
    InterrogationManeuverTable
"""
import sys
from tkinter import StringVar

from maneuvers.influence_maneuver_table import InfluenceManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


DISCOMFORT_PROMPT = """Causing "discomfort" to target?"""

NO_DISCOMFORT_TEXT = "No"
MILD_DISCOMFORT_TEXT = "Mild"
SEVERE_DISCOMFORT_TEXT = "Severe"
DISCOMFORT_OPTIONS = (NO_DISCOMFORT_TEXT, MILD_DISCOMFORT_TEXT, SEVERE_DISCOMFORT_TEXT)

MILD_DISCOMFORT_BONUS = 10
SEVERE_DISCOMFORT_BONUS = 25


class InterrogationManeuverTable(InfluenceManeuverTable):
    """
    Interrogation static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.discomfort_level = StringVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_discomfort_frame():
            """
            Create a frame with an OptionMenu specifying the level of discomfort caused to target
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               DISCOMFORT_PROMPT,
                                               NO_DISCOMFORT_TEXT,
                                               self.discomfort_level,
                                               *DISCOMFORT_OPTIONS)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_discomfort_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        discomfort_level = self.discomfort_level.get()
        if discomfort_level == MILD_DISCOMFORT_TEXT:
            trace.flow("Mild discomfort: +10")
            bonus += MILD_DISCOMFORT_BONUS
        elif discomfort_level == SEVERE_DISCOMFORT_TEXT:
            trace.flow("Severe discomfort: +25")
            bonus += SEVERE_DISCOMFORT_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
