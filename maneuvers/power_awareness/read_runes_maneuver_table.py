# -*- coding: utf-8 -*-
"""
The Read Runes static maneuver table.

Classes:
    ReadRunesManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.power_awareness_maneuver_table import PowerAwarenessManeuverTable
import maneuvers.power_awareness.read_runes_use_items_utils as read_runes_utils

import frame_utils
import trace_log as trace

sys.path.append('../')


KNOW_REALM_TEXT = "Character knows the realm of the spell"
KNOW_SPELL_TEXT = "Character know the spell"
DIFFERENT_REALM_TEXT = "Character's realm differs from spell"
DIFFERENT_BASE_TEXT = "Spell from a different base list to caster"
CAN_CAST_TEXT = "Character can cast spell intrinsically"


class ReadRunesManeuverTable(PowerAwarenessManeuverTable):
    """
    Read Runes static maneuver table.

    Methods:
        setup_difficulty_frame(parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.known_realm = IntVar()
        self.known_spell = IntVar()
        self.different_realm = IntVar()
        self.different_base = IntVar()
        self.can_cast = IntVar()

        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """
        def setup_different_base_frame():
            """
            Create a frame with a Checkbox indicating whether the spell is from a
            different base to the character.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(
                parent_frame, DIFFERENT_BASE_TEXT, self.different_base)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        read_runes_utils.setup_known_realm_frame(self, parent_frame)
        read_runes_utils.setup_known_spell_frame(self, parent_frame)
        read_runes_utils.setup_different_realm_frame(self, parent_frame)
        setup_different_base_frame()
        read_runes_utils.setup_can_cast_frame(self, parent_frame)

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += read_runes_utils.known_realm_bonus(self.known_realm.get())
        bonus += read_runes_utils.known_spell_bonus(self.known_spell.get())
        bonus += read_runes_utils.different_realm_bonus(
            self.different_realm.get(), self.different_base.get())
        bonus += read_runes_utils.intrinsic_cast_bonus(self.can_cast.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
