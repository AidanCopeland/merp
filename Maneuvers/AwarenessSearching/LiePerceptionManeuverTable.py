# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.AwarenessSearchingManeuverTable import AwarenessSearchingManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

CANNOT_SEE_TEXT = "Cannot see target?"
CANNOT_HEAR_TEXT = "Cannot hear target?"
FAMILIARITY_PROMPT = "Familiarity with target"
UNFAMILIAR_TEXT = "Unfamiliar"
FAMILIAR_TEXT = "Familiar"
KNOWS_WELL_TEXT = "Knows well"
FAMILIARITY_OPTIONS = (UNFAMILIAR_TEXT, FAMILIAR_TEXT, KNOWS_WELL_TEXT)
LANGUAGE_RANKS_TEXT = "Ranks in target's language"

CANNOT_SEE_BONUS = -30
CANNOT_HEAR_BONUS = -50
UNFAMILIAR_BONUS = -25
FAMILIAR_BONUS = 10
KNOWS_WELL_BONUS = 25
NO_LANGUAGE_BONUS = -40
POOR_LANGUAGE_BONUS = -20


class LiePerceptionManeuverTable(AwarenessSearchingManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_cannot_see_frame():
            """
            Create a frame with a Checkbox indicating whether the target cannot be seen.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, CANNOT_SEE_TEXT, self.cannot_see)
            trace.exit()

        def setup_cannot_hear_frame():
            """
            Create a frame with a Checkbox indicating whether the target cannot be heard.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, CANNOT_HEAR_TEXT, self.cannot_hear)
            trace.exit()

        def setup_familiarity_frame():
            """
            Create a frame with an OptionMenu specifying the familiarity with the target
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, FAMILIARITY_PROMPT, UNFAMILIAR_TEXT, self.familiarity_type, *FAMILIARITY_OPTIONS)
            trace.exit()


        def setup_language_ranks_frame():
            """
            Create a frame with an Entry indicating the number of ranks the searcher has in the
            target's language.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, LANGUAGE_RANKS_TEXT, self.language_ranks)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.cannot_see = IntVar()
        self.cannot_hear = IntVar()
        self.familiarity_type = StringVar()
        self.language_ranks = IntVar()
        setup_cannot_see_frame()
        setup_cannot_hear_frame()
        setup_familiarity_frame()
        setup_language_ranks_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.cannot_see.get() == 1:
            trace.flow("Cannot see: -30")
            bonus += CANNOT_SEE_BONUS

        if self.cannot_hear.get() == 1:
            trace.flow("Cannot hear: -50")
            bonus += CANNOT_HEAR_BONUS

        familiarity_type = self.familiarity_type.get()
        if familiarity_type == UNFAMILIAR_TEXT:
            trace.flow("Unfamiliar: -25")
            bonus += UNFAMILIAR_BONUS
        elif familiarity_type == FAMILIAR_TEXT:
            trace.flow("Familiar: +10")
            bonus += FAMILIAR_BONUS
        elif familiarity_type == KNOWS_WELL_TEXT:
            trace.flow("Knows well: +25")
            bonus += KNOWS_WELL_BONUS

        if self.language_ranks.get():
            trace.flow("Set language bonus")
            language_ranks = self.language_ranks.get()

            if language_ranks == 0:
                trace.flow("No ranks: -40")
                bonus -= 40
            elif language_ranks <= 2:
                trace.flow("Low skill: -20")
                bonus -= 20

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
