# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

UNFAMILIAR_TEXT = "Is character unfamiliar with the nature of the subject?"
LANGUAGE_TEXT = "Does character have 4+ ranks in the language?"

UNFAMILIAR_PENALTY = 30
LANGUAGE_BONUS = 10


class ActingManeuverTable(ArtisticActiveManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_unfamiliar_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the character is unfamiliar with the subject
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, UNFAMILIAR_TEXT, self.unfamiliar)
            trace.exit()

        def setup_proficient_language_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the character is proficient in the language
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, LANGUAGE_TEXT, self.proficient_language)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.unfamiliar = IntVar()
        self.proficient_language = IntVar()
        setup_unfamiliar_frame(parent_frame)
        setup_proficient_language_frame(parent_frame)

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

        if self.proficient_language.get() == 1:
            trace.flow("Proficient in language")
            bonus += LANGUAGE_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
