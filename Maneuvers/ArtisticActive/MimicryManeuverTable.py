# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

SOUNDS_PROMPT = "Type of sounds being imitated:"
SOUNDS_SIMPLE_TEXT = "Simple (one note/tone)"
SOUNDS_COMPLEX_TEXT = "Multitone (birds trilling, etc.)"
SOUNDS_VERY_COMPLEX_TEXT = "Very complex (comprehensive words)"
SOUNDS_OPTIONS = (SOUNDS_SIMPLE_TEXT, SOUNDS_COMPLEX_TEXT, SOUNDS_VERY_COMPLEX_TEXT)
IMITATE_VOCAL_TEXT = "Imitating another's vocal sounds?"
MULTI_SIDED_TEXT = "Multi-sided conversations?"
NON_ANIMATE_PROMPT = "Non-animate sounds being imitated"
NON_ANIMATE_NONE_TEXT = "None"
NON_ANIMATE_SIMPLE_TEXT = "Simple"
NON_ANIMATE_COMPLEX_TEXT = "Complex - consider up to extra 40 penalty"
NON_ANIMATE_OPTIONS = (NON_ANIMATE_NONE_TEXT, NON_ANIMATE_SIMPLE_TEXT, NON_ANIMATE_COMPLEX_TEXT)

SOUNDS_SIMPLE_BONUS = 20
SOUNDS_COMPLEX_PENALTY = 10
SOUNDS_VERY_COMPLEX_PENALTY = 20
IMITATE_VOCAL_PENALTY = 20
MULTI_SIDED_PENALTY = 30
NON_ANIMATE_SIMPLE_PENALTY = 25
NON_ANIMATE_COMPLEX_PENALTY = 35


class MimicryManeuverTable(ArtisticActiveManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_sounds_type_frame():
            """
            Create a frame with an OptionMenu specifying the type of sounds being imitated
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, SOUNDS_PROMPT, SOUNDS_SIMPLE_TEXT, self.sounds_type, *SOUNDS_OPTIONS)
            trace.exit()

        def setup_imitate_vocal_frame():
            """
            Create a frame with a Checkbox indicating whether another's vocal patterns are imitated.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, IMITATE_VOCAL_TEXT, self.imitate_vocal_patterns)
            trace.exit()

        def setup_multi_sided_frame():
            """
            Create a frame with a Checkbox indicating whether multi-sided conversations are imitated.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, MULTI_SIDED_TEXT, self.multi_sided)
            trace.exit()

        def setup_non_animate_frame():
            """
            Create a frame with an OptionMenu specifying the type of non-animate sounds being imitated
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, NON_ANIMATE_PROMPT, NON_ANIMATE_NONE_TEXT, self.non_animate, *NON_ANIMATE_OPTIONS)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.sounds_type = StringVar()
        self.imitate_vocal_patterns = IntVar()
        self.multi_sided = IntVar()
        self.non_animate = StringVar()
        setup_sounds_type_frame()
        setup_imitate_vocal_frame()
        setup_multi_sided_frame()
        setup_non_animate_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        sounds_type = self.sounds_type.get()
        if sounds_type == SOUNDS_SIMPLE_TEXT:
            trace.flow("Simple sounds: +20")
            bonus += SOUNDS_SIMPLE_BONUS
        elif sounds_type == SOUNDS_COMPLEX_TEXT:
            trace.flow("Complex sounds: -10")
            bonus -= SOUNDS_COMPLEX_PENALTY
        elif sounds_type == SOUNDS_VERY_COMPLEX_TEXT:
            trace.flow("Very complex sounds: -20")
            bonus -= SOUNDS_VERY_COMPLEX_PENALTY

        if self.imitate_vocal_patterns.get() == 1:
            trace.flow("Imitate vocal patters")
            bonus -= IMITATE_VOCAL_PENALTY

        if self.multi_sided.get() == 1:
            trace.flow("Multi-sided conversations")
            bonus -= MULTI_SIDED_PENALTY

        non_animate_sounds = self.non_animate.get()
        if non_animate_sounds == NON_ANIMATE_SIMPLE_TEXT:
            trace.flow("Simple non-animate sounds: -25")
            bonus -= NON_ANIMATE_SIMPLE_PENALTY
        elif non_animate_sounds == NON_ANIMATE_COMPLEX_TEXT:
            trace.flow("Complex non-animate sounds: -35")
            bonus -= NON_ANIMATE_COMPLEX_PENALTY

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
