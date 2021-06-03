# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from StaticManeuverTable import *

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

IS_LOYAL_TEXT = "Is audience personally loyal or devoted to the character?"
IS_HIRED_TEXT = "Is audience under hire to the character?"

IS_LOYAL_BONUS = 50
IS_HIRED_BONUS = 20


class InteractionManeuverTable(StaticManeuverTable):
    maneuver_result_text = {
        BLUNDER: "Your blatant attempt at coercion alienates your audience.  "
                 "They are influenced to do the opposite of what you were attempting to get them to do.  "
                 "Until a change in circumstances occurs, any influence attempts by you will fail.",
        ABSOLUTE_FAILURE: "Your audience rejects you, causing you to lose confidence and your air of authority. "
                          "Any influence attempts during the next hour will result in failure.",
        FAILURE: "You have failed.  "
                 "Your audience will not be receptive to any of your attempts at influence for at least 1 day.",
        PARTIAL_SUCCESS: "Your audience is still listening.  You can continue to try to influence them.",
        NEAR_SUCCESS: "Keep talking, your audience is becoming more friendly. "
                      "Modify your next roll by +20.",
        SUCCESS: "You have influenced your audience.",
        ABSOLUTE_SUCCESS: "Not only did you influence your audience, but you receive a +50 bonus on influencing"
                          " them until you do something to cause them to lose confidence in you."
    }

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        def setup_loyal_audience_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the audience is loyal to the character
            """
            trace.entry()

            FrameUtils.setup_checkbox_frame(parent_frame, IS_LOYAL_TEXT, self.is_loyal)

            trace.exit()

        def setup_hired_audience_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the audience is hired to the character
            """
            trace.entry()

            FrameUtils.setup_checkbox_frame(parent_frame, IS_HIRED_TEXT, self.is_hired)

            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.is_loyal = IntVar()
        self.is_hired = IntVar()
        setup_loyal_audience_frame(parent_frame)
        setup_hired_audience_frame(parent_frame)

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.is_loyal.get() == 1:
            trace.flow("Audience is loyal: +50")
            bonus += IS_LOYAL_BONUS

        if self.is_hired.get() == 1:
            trace.flow("Audience is hired: +20")
            bonus += IS_HIRED_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
