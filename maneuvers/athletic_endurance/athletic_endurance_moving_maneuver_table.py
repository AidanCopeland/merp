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
from maneuvers.athletic_endurance_maneuver_table import AthleticEnduranceManeuverTable
from console.character.secondary_skills import SKILL_DISTANCE_RUNNING, SKILL_SPRINTING
from console.character.general_skills import SKILL_ROWING, SKILL_SCALING, SKILL_CLIMB, SKILL_SWIM

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

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            AthleticEnduranceManeuverTable.MANEUVER_DISTANCE_RUNNING: [SKILL_DISTANCE_RUNNING, ],
            AthleticEnduranceManeuverTable.MANEUVER_ROWING: [SKILL_ROWING, ],
            AthleticEnduranceManeuverTable.MANEUVER_SCALING:
                [SKILL_SCALING, SKILL_CLIMB],
            AthleticEnduranceManeuverTable.MANEUVER_SPRINTING: [SKILL_SPRINTING, ],
            AthleticEnduranceManeuverTable.MANEUVER_SWIMMING: [SKILL_SWIM, ]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
