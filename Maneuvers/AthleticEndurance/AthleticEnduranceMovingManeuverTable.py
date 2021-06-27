# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.MovingManeuverTable import MovingManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class AthleticEnduranceMovingManeuverTable(MovingManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(MovingManeuverTable, self).__init__(**kwargs)
        self.equipment_bonus = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_equipment_frame():
            """
            Create a frame with an Entry indicating whether proper equipment is missing.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, EQUIPMENT_TEXT, self.equipment_bonus)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.equipment_bonus.set(0)
        setup_equipment_frame()

        trace.exit()
