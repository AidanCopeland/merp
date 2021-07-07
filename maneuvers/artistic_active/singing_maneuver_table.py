# -*- coding: utf-8 -*-
"""
The Singing static maneuver table.

Classes:
    SingingManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.artistic_active_maneuver_table import ArtisticActiveManeuverTable
from maneuvers.artistic_active import artistic_active_utils

import frame_utils
import trace_log as trace

sys.path.append('../')


BAD_LANGUAGE_TEXT = "Only one skill rank in language?"

BAD_LANGUAGE_PENALTY = 20
IMPROVISATION_PENALTY = 30


class SingingManeuverTable(ArtisticActiveManeuverTable):
    """
    Singing static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        table_bonus(self)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.bad_language = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_bad_language_frame():
            """
            Create a frame with a Checkbox indicating whether the speaker has only 1 rank in the
            language
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, BAD_LANGUAGE_TEXT, self.bad_language)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_bad_language_frame()

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
        if self.bad_language.get() == 1:
            trace.flow("Singer is not proficient in language")
            bonus -= BAD_LANGUAGE_PENALTY

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
