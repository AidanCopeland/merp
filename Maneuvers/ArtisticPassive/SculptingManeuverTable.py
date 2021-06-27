# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.ArtisticPassiveManeuverTable import ArtisticPassiveManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


UNFAMILIAR_TEXT = "Is this an unfamiliar medium?"
POSED_TEXT = "Is this from a posed image or person?"
MEMORY_TEXT = "Is this from memory?"
IG_BONUS_TEXT = "If from memory, enter IG stat bonus"

UNFAMILIAR_PENALTY = 30
POSED_BONUS = 10
MEMORY_BASE_PENALTY = 30


class SculptingManeuverTable(ArtisticPassiveManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(ArtisticPassiveManeuverTable, self).__init__(**kwargs)
        self.unfamiliar = IntVar()
        self.posed = IntVar()
        self.from_memory = IntVar()
        self.ig_bonus = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_unfamiliar_frame():
            """
            Create a frame with a Checkbox indicating whether the character is unfamiliar with the medium
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, UNFAMILIAR_TEXT, self.unfamiliar)
            trace.exit()

        def setup_posed_frame():
            """
            Create a frame with a Checkbox indicating whether sculpture is from a posed image or person
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, POSED_TEXT, self.posed)
            trace.exit()

        def setup_memory_frame():
            """
            Create a frame with an Checkbox indicating whether this is from memory
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, MEMORY_TEXT, self.from_memory)
            trace.exit()

        def setup_ig_bonus_frame():
            """
            Create a frame with an Entry specifying the IG stat
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, MEMORY_TEXT, self.ig_bonus)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.ig_bonus.set(0)
        setup_unfamiliar_frame()
        setup_posed_frame()
        setup_memory_frame()
        setup_ig_bonus_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.unfamiliar.get() == 1:
            trace.flow("Unfamiliar with nature of subject")
            bonus -= UNFAMILIAR_PENALTY

        if self.posed.get() == 1:
            trace.flow("Posed subject")
            bonus += POSED_BONUS

        if self.from_memory.get() == 1:
            trace.flow("From memory")
            bonus -= (MEMORY_BASE_PENALTY - self.ig_bonus.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
