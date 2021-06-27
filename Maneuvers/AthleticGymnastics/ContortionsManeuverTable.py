# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.AthleticGymnasticsManeuverTable import AthleticGymnasticsManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import StringVar
standard_library.install_aliases()

sys.path.append('../')

BONDS_PROMPT = "Type of bonds"
BONDS_NONE_TEXT = "None"
BONDS_ORGANIC_TEXT = "Organic"
BONDS_METAL_TEXT = "Metal"
BONDS_OPTIONS = (BONDS_NONE_TEXT, BONDS_ORGANIC_TEXT, BONDS_METAL_TEXT)

BONDS_ORGANIC_PENALTY = 10
BONDS_METAL_PENALTY = 30


class ContortionsManeuverTable(AthleticGymnasticsManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(AthleticGymnasticsManeuverTable, self).__init__(**kwargs)
        self.bonds = StringVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_bonds_frame():
            """
            Create a frame with an OptionMenu specifying the bonds (if any)
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, BONDS_PROMPT, BONDS_NONE_TEXT, self.bonds, *BONDS_OPTIONS)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_bonds_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        bonds = self.bonds.get()
        if bonds == BONDS_NONE_TEXT:
            trace.flow("No bonds")
        elif bonds == BONDS_ORGANIC_TEXT:
            trace.flow("Organic bonds")
            bonus -= BONDS_ORGANIC_PENALTY
        elif bonds == BONDS_METAL_TEXT:
            trace.flow("Metal bonds")
            bonus -= BONDS_METAL_PENALTY

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
