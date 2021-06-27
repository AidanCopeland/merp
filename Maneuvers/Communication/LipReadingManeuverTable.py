# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.CommunicationManeuverTable import CommunicationManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


RANGE_TEXT = "Distance from target (feet)?"

CANNOT_SEE_BONUS = -30
CANNOT_HEAR_BONUS = -50
UNFAMILIAR_BONUS = -25
FAMILIAR_BONUS = 10
KNOWS_WELL_BONUS = 25
NO_LANGUAGE_BONUS = -40
POOR_LANGUAGE_BONUS = -20


class LipReadingManeuverTable(CommunicationManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(CommunicationManeuverTable, self).__init__(**kwargs)
        self.range = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_range_frame():
            """
            Create a frame with an Entry indicating the range from the character to the
            target.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, RANGE_TEXT, self.range)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_range_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.range.get():
            trace.flow("Set range bonus")
            range_val = self.range.get()

            if range_val > 20:
                trace.flow("Over 20'")
                bonus -= (2 * (range_val - 20))

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
