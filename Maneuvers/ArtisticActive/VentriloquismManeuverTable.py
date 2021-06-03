# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

WITH_PROPS_TEXT = "With props?"
VOICE_DISTANCE_TEXT = "Distance voice thrown (in feet)?"

WITH_PROPS_BONUS = 15
VOICE_DISTANCE_PENALTY = 5


class VentriloquismManeuverTable(ArtisticActiveManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_with_props_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the mime uses props
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, WITH_PROPS_TEXT, self.with_props)
            trace.exit()

        def setup_voice_distance_frame(parent_frame):
            """
            Create a frame with an Entry specifying the distance the voice is "thrown"
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, VOICE_DISTANCE_TEXT, self.voice_distance)

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.with_props = IntVar()
        self.voice_distance = IntVar()
        self.voice_distance.set(0)
        setup_with_props_frame(parent_frame)

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.with_props.get() == 1:
            trace.flow("Using props")
            bonus += WITH_PROPS_BONUS

        voice_distance_penalty = self.voice_distance.get() * VOICE_DISTANCE_PENALTY
        trace.detail("Voice distance penalty %d" % voice_distance_penalty)

        bonus -= voice_distance_penalty

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
