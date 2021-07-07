# -*- coding: utf-8 -*-
"""
The Music static maneuver table.

Classes:
    MusicManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.artistic_passive_maneuver_table import ArtisticPassiveManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')

NUMBER_PEOPLE_TEXT = "Number of people involved?"


class MusicManeuverTable(ArtisticPassiveManeuverTable):
    """
    Music static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
    """

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.number_people = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_number_people_frame():
            """
            Create a frame with an Entry specifying the number of people involved
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, NUMBER_PEOPLE_TEXT, self.number_people)

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.number_people.set(1)
        setup_number_people_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.number_people.get() <= 1:
            bonus = 0
        elif self.number_people.get() <= 4:
            bonus -= 5
        elif self.number_people.get() <= 10:
            bonus -= 10
        elif self.number_people.get() <= 20:
            bonus -= 15
        else:
            bonus -= 20

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
