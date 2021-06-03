# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.AwarenessSensesManeuverTable import AwarenessSensesManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

NO_REFERENTS_TEXT = "Are there no external referents?"
SLEEP_TEXT = "Right after sleep/unconsciousness?"

NO_REFERENTS_BONUS = -40
SLEEP_BONUS = -20


class TimeSenseManeuverTable(AwarenessSensesManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_no_referents_frame():
            """
            Create a frame with a Checkbox indicating whether there are no external
            referents.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, NO_REFERENTS_TEXT, self.no_referents)
            trace.exit()

        def setup_sleep_frame():
            """
            Create a frame with a Checkbox indicating whether this is just after sleep or
            unconsciousness.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, SLEEP_TEXT, self.sleep)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.no_referents = IntVar()
        self.sleep = IntVar()
        setup_no_referents_frame()
        setup_sleep_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.no_referents.get() == 1:
            trace.flow("No external referents: -40")
            bonus += NO_REFERENTS_BONUS

        if self.sleep.get() == 1:
            trace.flow("After sleep/unconsciousness: -20")
            bonus += SLEEP_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
