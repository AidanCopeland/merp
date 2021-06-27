# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable, PARTNER_PENALTY, LORE_BONUS

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


ELF_TEXT = "Elf?"
LANGUAGE_TEXT = "Does character have 4+ ranks in the language?"

ELF_BONUS = 10
LANGUAGE_BONUS = 10
IMPROVISATION_PENALTY = 30


class PoeticImprovisationManeuverTable(ArtisticActiveManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(ArtisticActiveManeuverTable, self).__init__(**kwargs)
        self.is_elf = IntVar()
        self.proficient_language = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_elf_frame():
            """
            Create a frame with a Checkbox indicating whether the character is an elf
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, ELF_TEXT, self.is_elf)
            trace.exit()

        def setup_proficient_language_frame():
            """
            Create a frame with a Checkbox indicating whether the character is proficient in the language
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, LANGUAGE_TEXT, self.proficient_language)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_elf_frame()
        setup_proficient_language_frame()

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
            bonus -= IMPROVISATION_PENALTY

        if self.with_partner.get() == 1:
            trace.flow("With partner: -10")
            bonus -= PARTNER_PENALTY

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
        if self.is_elf.get() == 1:
            trace.flow("Character is elf: +10")
            bonus += ELF_BONUS

        if self.proficient_language.get() == 1:
            trace.flow("Character is proficient in the language: +10")
            bonus += LANGUAGE_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
