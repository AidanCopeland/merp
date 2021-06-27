# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.ArtisticPassiveManeuverTable import ArtisticPassiveManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


PERSONAL_TEXT = "Is this about a personal experience?"
UNFAMILIAR_TEXT = "Is this about an unfamiliar topic?"
LANGUAGE_TEXT = "4+ ranks in language?"

PERSONAL_BONUS = 10
UNFAMILIAR_PENALTY = 30
LANGUAGE_BONUS = 15


class PoetryManeuverTable(ArtisticPassiveManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(ArtisticPassiveManeuverTable, self).__init__(**kwargs)
        self.unfamiliar = IntVar()
        self.personal = IntVar()
        self.language_proficient = IntVar()

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

        def setup_personal_frame():
            """
            Create a frame with a Checkbox indicating whether this is about a personal experience
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, PERSONAL_TEXT, self.personal)
            trace.exit()

        def setup_language_frame():
            """
            Create a frame with a Checkbox indicating whether the character is proficient in the language
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, LANGUAGE_TEXT, self.language_proficient)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_unfamiliar_frame()
        setup_personal_frame()
        setup_language_frame()

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

        if self.personal.get() == 1:
            trace.flow("Personal experience")
            bonus += PERSONAL_BONUS

        if self.language_proficient.get() == 1:
            trace.flow("Proficient in language")
            bonus += LANGUAGE_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
