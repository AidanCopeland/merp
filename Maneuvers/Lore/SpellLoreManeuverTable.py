# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.LoreManeuverTable import LoreManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')


INSTANT_SPELL_TEXT = "Instant spell cast?"
INSTANT_SPELL_BONUS = -30


class SpellLoreManeuverTable(LoreManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(LoreManeuverTable, self).__init__(**kwargs)
        self.instant_spell = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_instant_spell_frame():
            """
            Create a frame with a Checkbox indicating whether the spell was an Instant spell.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, INSTANT_SPELL_TEXT, self.instant_spell)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_instant_spell_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        if self.instant_spell.get() == 1:
            trace.flow("Instant spell: -30")
            bonus += INSTANT_SPELL_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
