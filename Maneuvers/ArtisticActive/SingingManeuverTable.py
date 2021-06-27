# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable, PARTNER_PENALTY, LORE_BONUS

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


BAD_LANGUAGE_TEXT = "Only one skill rank in language?"

BAD_LANGUAGE_PENALTY = 20
IMPROVISATION_PENALTY = 30


class SingingManeuverTable(ArtisticActiveManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(ArtisticActiveManeuverTable, self).__init__(**kwargs)
        self.bad_language = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_bad_language_frame():
            """
            Create a frame with a Checkbox indicating whether the speaker has only 1 rank in the language
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, BAD_LANGUAGE_TEXT, self.bad_language)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_bad_language_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        trace.detail("Practised bonus: %d" % self.practised_bonus.get())
        bonus += self.practised_bonus.get()
        if self.is_improvised.get() == 1:
            trace.flow("Improvised: -30")
            bonus += IMPROVISATION_PENALTY

        if self.with_partner.get() == 1:
            trace.flow("With partner: -10")
            bonus += PARTNER_PENALTY

        if self.lore_skill.get() == 1:
            trace.flow("Lore skill: +10")
            bonus += LORE_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.bad_language.get() == 1:
            trace.flow("Singer is not proficient in language")
            bonus -= BAD_LANGUAGE_PENALTY

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
