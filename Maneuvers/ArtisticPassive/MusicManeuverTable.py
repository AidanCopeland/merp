# -*- coding: utf-8 -*-
import sys

from Maneuvers.ArtisticPassiveManeuverTable import ArtisticPassiveManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

sys.path.append('../')

NUMBER_PEOPLE_TEXT = "Number of people involved?"


class MusicManeuverTable(ArtisticPassiveManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_number_people_frame(parent_frame):
            """
            Create a frame with an Entry specifying the number of people involved
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, NUMBER_PEOPLE_TEXT, self.number_people)

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.number_people = IntVar()
        self.number_people.set(1)
        setup_number_people_frame(parent_frame)

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
