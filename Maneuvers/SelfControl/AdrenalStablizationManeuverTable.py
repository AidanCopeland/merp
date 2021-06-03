# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.SelfControlManeuverTable import SelfControlManeuverTable
from ttk import Frame, Label, OptionMenu

import FrameUtils
import trace_log as trace

from Tkinter import LEFT, RIGHT, BOTH, RAISED

INJURY_PROMPT = "Severity of injuries: "

PRACTISING = "Just practising"
ONE_HPR = "Bleeding 1 hit/rnd"
TWO_HPR = "Bleeding 2 hits/rnd"
THREE_HPR = "Bleeding 3 hits/rnd"
FOUR_HPR = "Bleeding 4 hits/rnd"
FIVE_HPR = "Bleeding 5 hits/rnd"
SIX_PLUS_HPR = "Bleeding 6 hits/rnd or more"
ONE_LIMB_OFF = "One limb amputated"
TWO_LIMBS_OFF = "Two limbs amputated"

INJURY_DEFAULT = PRACTISING

injury_options = (
    PRACTISING, ONE_HPR, TWO_HPR, THREE_HPR, FOUR_HPR, FIVE_HPR,
    SIX_PLUS_HPR, ONE_LIMB_OFF, TWO_LIMBS_OFF
)

maneuver_difficulty_bonuses = {
    PRACTISING: 30,
    ONE_HPR: 20,
    TWO_HPR: 10,
    THREE_HPR: 0,
    FOUR_HPR: -10,
    FIVE_HPR: -20,
    SIX_PLUS_HPR: -30,
    ONE_LIMB_OFF: -50,
    TWO_LIMBS_OFF: -70
}


class AdrenalStablizationManueverTable(SelfControlManeuverTable):

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=INJURY_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = injury_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                INJURY_DEFAULT,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def difficulty_bonus(self):
        """
        Determine the difficulty to apply to a maneuver based on its difficulty.
        :return: The maneuver difficulty bonus
        """
        trace.entry()

        bonus = maneuver_difficulty_bonuses[self.maneuver_difficulty.get()]
        trace.detail("Returning %d" % bonus)

        trace.exit()
        return bonus
