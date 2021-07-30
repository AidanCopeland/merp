# -*- coding: utf-8 -*-
"""
The Adrenal Evasion moving maneuver table.

Classes:
    AdrenalEvasionManeuverTable
"""
import sys
from tkinter import StringVar

from maneuvers.moving_maneuver_table import HARD, EXTREMELY_HARD
from maneuvers.combat_maneuvers.adrenal_deflection_evasion_maneuver_table import \
    AdrenalDeflectionEvasionManeuverTable

import trace_log as trace

sys.path.append('../')

MELEE_THROWN_WEAPON_TEXT = "Melee/Thrown"
MISSILE_WEAPON_TEXT = "Missile"

weapon_options = (
    MELEE_THROWN_WEAPON_TEXT,
    MISSILE_WEAPON_TEXT)

weapon_difficulties = {
    MELEE_THROWN_WEAPON_TEXT: HARD,
    MISSILE_WEAPON_TEXT: EXTREMELY_HARD
}


class AdrenalEvasionManeuverTable(AdrenalDeflectionEvasionManeuverTable):
    """
    Adrenal Evasion moving maneuver table.

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
