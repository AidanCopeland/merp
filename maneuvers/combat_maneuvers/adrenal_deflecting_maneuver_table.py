# -*- coding: utf-8 -*-
"""
The Adrenal Deflecting moving maneuver table.

Classes:
    AdrenalDeflectingManeuverTable
"""
import sys
from tkinter import StringVar

from maneuvers.moving_maneuver_table import EXTREMELY_HARD, SHEER_FOLLY
from maneuvers.combat_maneuvers.adrenal_deflection_evasion_maneuver_table import \
    AdrenalDeflectionEvasionManeuverTable
from console.character.weapon_skills import SKILL_ADRENAL_DEFLECTING

import trace_log as trace

sys.path.append('../')

THROWN_WEAPON_TEXT = "Thrown"
MISSILE_WEAPON_TEXT = "Missile"

weapon_options = (
    THROWN_WEAPON_TEXT,
    MISSILE_WEAPON_TEXT)

weapon_difficulties = {
    THROWN_WEAPON_TEXT: EXTREMELY_HARD,
    MISSILE_WEAPON_TEXT: SHEER_FOLLY
}


class AdrenalDeflectingManeuverTable(AdrenalDeflectionEvasionManeuverTable):
    """
    Adrenal Deflecting moving maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        difficulty_table_column(self)
        maneuver_resolution(self, roll)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.weapon_type = StringVar()
        trace.exit()

    @staticmethod
    def get_weapon_options():
        """
        Returns the list of weapons being deflected or evaded.
        """
        return weapon_options

    def get_weapon_difficulty(self):
        """
        Returns the difficulty of the maneuver based on the weapon type.
        """
        return weapon_difficulties[self.weapon_type.get()]

    @staticmethod
    def get_maneuver_preferred_skills(_):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param _: The type of maneuver selected.
        """
        return [SKILL_ADRENAL_DEFLECTING, ]
