# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.AwarenessSearchingManeuverTable import AwarenessSearchingManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

SPECIFIC_ITEM_TEXT = "Searching for a specific item?"
LOCATION_DESCRIBED_TEXT = "Location described in detail?"

SPECIFIC_ITEM_BONUS = 10
LOCATION_DESCRIBED_BONUS = 20


class LocateHiddenManeuverTable(AwarenessSearchingManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_specific_item_frame():
            """
            Create a frame with a Checkbox indicating whether the character is searching
            for a specific item.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, SPECIFIC_ITEM_TEXT, self.specific_item)
            trace.exit()

        def setup_location_described_frame():
            """
            Create a frame with a Checkbox indicating whether the location of the thing being
            sought has been described in detail.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, LOCATION_DESCRIBED_TEXT, self.location_described)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.specific_item = IntVar()
        self.location_described = IntVar()
        setup_specific_item_frame()
        setup_location_described_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.specific_item.get() == 1:
            trace.flow("Specific item: +10")
            bonus += SPECIFIC_ITEM_BONUS

        if self.location_described.get() == 1:
            trace.flow("Location described: +20")
            bonus += LOCATION_DESCRIBED_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
