# -*- coding: utf-8 -*-
"""
The Tale Telling static maneuver table.

Classes:
    TaleTellingManeuverTable
"""
import sys
from tkinter import IntVar, StringVar

from maneuvers.artistic_active_maneuver_table import ArtisticActiveManeuverTable
from maneuvers.artistic_active import artistic_active_utils

import frame_utils
import trace_log as trace

sys.path.append('../')

LANGUAGE_TEXT = "Does character have 4+ ranks in the language?"
RACE_TEXT = "Character's race:"
RACE_ELF = "Elf"
RACE_HOBBIT = "Hobbit"
RACE_OTHER = "Other"

RACE_OPTIONS = (RACE_ELF, RACE_HOBBIT, RACE_OTHER)

ELF_BONUS = 10
HOBBIT_BONUS = 15
LANGUAGE_BONUS = 10
IMPROVISATION_PENALTY = 30


class TaleTellingManeuverTable(ArtisticActiveManeuverTable):
    """
    Tale Telling static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        table_bonus(self)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.proficient_language = IntVar()
        self.race = StringVar()
        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_proficient_language_frame():
            """
            Create a frame with a Checkbox indicating whether the character is proficient in the
            language
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, LANGUAGE_TEXT, self.proficient_language)
            trace.exit()

        def setup_race_frame():
            """
            Create a frame with an OptionMenu specifying the character's race
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               RACE_TEXT,
                                               RACE_OTHER,
                                               self.race,
                                               *RACE_OPTIONS)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_proficient_language_frame()
        setup_race_frame()

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
        if self.proficient_language.get() == 1:
            trace.flow("Character is proficient in the language")
            bonus += LANGUAGE_BONUS

        if self.race.get() == RACE_ELF:
            trace.flow("Elf: +10 bonus")
            bonus += ELF_BONUS
        elif self.race.get() == RACE_HOBBIT:
            trace.flow("Hobbit: +15 bonus")
            bonus += HOBBIT_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
