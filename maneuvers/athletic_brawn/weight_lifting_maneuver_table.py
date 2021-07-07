# -*- coding: utf-8 -*-
"""
The Weight Lifting static maneuver table.

Classes:
    WeightLiftingStaticManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.athletic_brawn_maneuver_table import AthleticBrawnManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')

FLAT_SURFACE_TEXT = "Is the surface flat and level?"
UNEVEN_TEXT = "Is the weight unevenly distributed?"
HAND_HOLDS_TEXT = "Are there easy hand-holds?"
EXTRA_PREP_TEXT = "Have there been at least 2 rounds prep?"

FLAT_SURFACE_BONUS = 5
UNEVEN_PENALTY = 20
HAND_HOLDS_BONUS = 10
EXTRA_PREP_BONUS = 10


class WeightLiftingManeuverTable(AthleticBrawnManeuverTable):
    """
    Weight Lifting static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.flat_surface = IntVar()
        self.uneven = IntVar()
        self.hand_holds = IntVar()
        self.extra_prep = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_flat_surface_frame():
            """
            Create a frame with a Checkbox indicating whether there is a flat surface
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, FLAT_SURFACE_TEXT, self.flat_surface)
            trace.exit()

        def setup_uneven_frame():
            """
            Create a frame with a Checkbox indicating whether the weight is unevenly distributed
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, UNEVEN_TEXT, self.uneven)
            trace.exit()

        def setup_hand_holds_frame():
            """
            Create a frame with an Checkbox indicating whether there are easy hand-holds
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, HAND_HOLDS_TEXT, self.hand_holds)
            trace.exit()

        def setup_extra_prep_frame():
            """
            Create a frame with an Checkbox indicating whether there has been an extra prep round
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, EXTRA_PREP_TEXT, self.extra_prep)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_flat_surface_frame()
        setup_uneven_frame()
        setup_hand_holds_frame()
        setup_extra_prep_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.flat_surface.get() == 1:
            trace.flow("Flat, level surface")
            bonus += FLAT_SURFACE_BONUS

        if self.uneven.get() == 1:
            trace.flow("Weight unevenly distributed")
            bonus -= UNEVEN_PENALTY

        if self.hand_holds.get() == 1:
            trace.flow("Easy hand-holds")
            bonus += HAND_HOLDS_BONUS

        if self.extra_prep.get() == 1:
            trace.flow("Extra prep round")
            bonus += EXTRA_PREP_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
