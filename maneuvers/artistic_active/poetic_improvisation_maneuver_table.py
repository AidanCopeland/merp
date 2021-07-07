# -*- coding: utf-8 -*-
"""
The Poetic Improvisation static maneuver table.

Classes:
    PoeticImprovisationManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.artistic_active_maneuver_table import ArtisticActiveManeuverTable
from maneuvers.artistic_active import artistic_active_utils

import frame_utils
import trace_log as trace

sys.path.append('../')


ELF_TEXT = "Elf?"
LANGUAGE_TEXT = "Does character have 4+ ranks in the language?"

ELF_BONUS = 10
LANGUAGE_BONUS = 10
IMPROVISATION_PENALTY = 30


class PoeticImprovisationManeuverTable(ArtisticActiveManeuverTable):
    """
    Poetic Improvisation static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        table_bonus(self)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
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
            frame_utils.setup_checkbox_frame(parent_frame, ELF_TEXT, self.is_elf)
            trace.exit()

        def setup_proficient_language_frame():
            """
            Create a frame with a Checkbox indicating whether the character is proficient in the
            language.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, LANGUAGE_TEXT, self.proficient_language)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_elf_frame()
        setup_proficient_language_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        return artistic_active_utils.table_bonus(self)

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
