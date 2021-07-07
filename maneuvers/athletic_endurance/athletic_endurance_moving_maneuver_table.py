# -*- coding: utf-8 -*-
"""
The Athletic/Endurance moving maneuver table.

Classes:
    AthleticEnduranceMovingManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.moving_maneuver_table import MovingManeuverTable
from maneuvers import maneuver_utils

import trace_log as trace

sys.path.append('../')

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


class AthleticEnduranceMovingManeuverTable(MovingManeuverTable):
    """
    Athletic/Endurance moving maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.equipment_bonus = IntVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        maneuver_utils.setup_maneuver_table_frames_for_equipment(self, parent_frame)
