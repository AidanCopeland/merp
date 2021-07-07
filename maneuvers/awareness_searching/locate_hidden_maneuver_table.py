# -*- coding: utf-8 -*-
"""
The Locate Hidden static maneuver table.

Classes:
    LocateHiddenManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.awareness_searching_maneuver_table import AwarenessSearchingManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


SPECIFIC_ITEM_TEXT = "Searching for a specific item?"
LOCATION_DESCRIBED_TEXT = "Location described in detail?"

SPECIFIC_ITEM_BONUS = 10
LOCATION_DESCRIBED_BONUS = 20


class LocateHiddenManeuverTable(AwarenessSearchingManeuverTable):
    """
    Locate Hidden static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.specific_item = IntVar()
        self.location_described = IntVar()

        trace.exit()

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
            frame_utils.setup_checkbox_frame(parent_frame, SPECIFIC_ITEM_TEXT, self.specific_item)
            trace.exit()

        def setup_location_described_frame():
            """
            Create a frame with a Checkbox indicating whether the location of the thing being
            sought has been described in detail.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame,
                                             LOCATION_DESCRIBED_TEXT,
                                             self.location_described)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

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
