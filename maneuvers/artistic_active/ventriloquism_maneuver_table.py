# -*- coding: utf-8 -*-
"""
The Ventriloquism static maneuver table.

Classes:
    VentriloquismManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.artistic_active_maneuver_table import ArtisticActiveManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


WITH_PROPS_TEXT = "With props?"
VOICE_DISTANCE_TEXT = "Distance voice thrown (in feet)?"

WITH_PROPS_BONUS = 15
VOICE_DISTANCE_PENALTY = 5


class VentriloquismManeuverTable(ArtisticActiveManeuverTable):
    """
    Ventriloquism static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.with_props = IntVar()
        self.voice_distance = IntVar()
        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_with_props_frame():
            """
            Create a frame with a Checkbox indicating whether the mime uses props
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, WITH_PROPS_TEXT, self.with_props)
            trace.exit()

        def setup_voice_distance_frame():
            """
            Create a frame with an Entry specifying the distance the voice is "thrown"
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, VOICE_DISTANCE_TEXT, self.voice_distance)

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.voice_distance.set(0)
        setup_with_props_frame()
        setup_voice_distance_frame()

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
