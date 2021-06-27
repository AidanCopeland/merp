# -*- coding: utf-8 -*-
from future import standard_library
import sys
from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


COMPLEX_CONCEPTS_TEXT = "Complex concepts?"
WITH_PROPS_TEXT = "With props?"

COMPLEX_CONCEPTS_PENALTY = 15
WITH_PROPS_BONUS = 10


class MimeryManeuverTable(ArtisticActiveManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(ArtisticActiveManeuverTable, self).__init__(**kwargs)
        self.complex_concepts = IntVar()
        self.with_props = IntVar()
        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_complex_concepts_frame():
            """
            Create a frame with a Checkbox indicating whether the mime involves complex concepts
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, COMPLEX_CONCEPTS_TEXT, self.complex_concepts)
            trace.exit()

        def setup_with_props_frame():
            """
            Create a frame with a Checkbox indicating whether the mime uses props
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, WITH_PROPS_TEXT, self.with_props)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_complex_concepts_frame()
        setup_with_props_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.complex_concepts.get() == 1:
            trace.flow("Complex concepts")
            bonus -= COMPLEX_CONCEPTS_PENALTY

        if self.with_props.get() == 1:
            trace.flow("Using props")
            bonus += WITH_PROPS_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
