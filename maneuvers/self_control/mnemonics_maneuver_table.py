# -*- coding: utf-8 -*-
"""
The Mnemonics static maneuver table.

Classes:
    MnemonicsManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.self_control_maneuver_table import SelfControlManeuverTable

import frame_utils
import trace_log as trace


sys.path.append('../')


WEEKS_PAST_TEXT = "Number of weeks in past when information was learned"
WEEKS_PAST_BONUS = 5

CAREFULLY_LEARNED_TEXT = "Carefully committed to memory?"
CAREFULLY_LEARNED_BONUS = 30

PC_IMPACT_TEXT = "Bonus for impact to PC (-10 to +30)"


class MnemonicsManeuverTable(SelfControlManeuverTable):
    """
    Mnemonics static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.weeks_past = IntVar()
        self.carefully_learned = IntVar()
        self.pc_impact = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_weeks_past_frame():
            """
            Create a frame with an Entry indicating the time since the information
            was learned.
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, WEEKS_PAST_TEXT, self.weeks_past)
            trace.exit()

        def setup_carefully_learned_frame():
            """
            Create a frame with a Checkbox indicating whether the information was
            carefully learned.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(
                parent_frame, CAREFULLY_LEARNED_TEXT, self.carefully_learned)
            trace.exit()

        def setup_pc_impact_frame():
            """
            Create a frame with an Entry indicating the impact of the information on
            the PC.
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, PC_IMPACT_TEXT, self.pc_impact)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        setup_carefully_learned_frame()
        setup_weeks_past_frame()
        setup_pc_impact_frame()
        self.weeks_past.set(0)
        self.pc_impact.set(0)

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        weeks_past = self.weeks_past.get()
        trace.detail("%d weeks in past, %d bonus" %
                     (weeks_past, weeks_past * WEEKS_PAST_BONUS))
        bonus += weeks_past * WEEKS_PAST_BONUS

        if self.carefully_learned.get() == 1:
            trace.flow("Carefully learned: +30")
            bonus += CAREFULLY_LEARNED_BONUS

        trace.detail("Impact on PC: %d" % self.pc_impact.get())
        bonus += self.pc_impact.get()
