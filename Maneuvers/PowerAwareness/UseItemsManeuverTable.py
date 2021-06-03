# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.PowerAwarenessManeuverTable import PowerAwarenessManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

KNOW_REALM_TEXT = "Character knows the realm of the spell"
KNOW_SPELL_TEXT = "Character knows the spell"
DIFFERENT_REALM_TEXT = "Character's realm differs from spell"
CAN_CAST_TEXT = "Character can cast spell intrinsically"

KNOWN_REALM_BONUS = 10
UNKNOWN_REALM_BONUS = -20

KNOWN_SPELL_BONUS = 20
UNKNOWN_SPELL_BONUS = -10

DIFFERENT_REALM_BONUS = -30
CAN_CAST_BONUS = 30

def known_realm_bonus(known_realm):
    """
    Determine the bonus to the maneuver based on whether the character knows the
    spell realm.
    :param known_realm: Whether the character knows the realm of the spell.
    :return: The bonus depending on whether the character knows the spell realm.
    """
    if known_realm:
        trace.flow("Known realm: +10")
        return KNOWN_REALM_BONUS
    else:
        trace.flow("Unknown realm: -20")
        return UNKNOWN_REALM_BONUS

def known_spell_bonus(known_spell):
    """
    Determine the bonus to the maneuver based on whether the character knows what
    the spell is.
    :param known_spell: Whether the character knows what the spell is.
    :return: The bonus to the maneuver.
    """
    if known_spell:
        trace.flow("Known spell: +20")
        return KNOWN_SPELL_BONUS
    else:
        trace.flow("Unknown spell: -10")
        return UNKNOWN_SPELL_BONUS

def different_realm_bonus(different_realm):
    """
    Determine the bonus to the maneuver based on whether the caster's realm
    differs from the spell's.
    :param different_realm: Whether the caster's realm differs from the
    spell's.
    :return: The bonus to the maneuver.
    """
    if different_realm:
        trace.flow("Different realm: -30")
        return DIFFERENT_REALM_BONUS
    else:
        return 0

def intrinsic_cast_bonus(can_cast):
    """
    Determine the bonus to the maneuver based on whether the caster can cast
    the spell intrinsically.
    :param can_cast: Whether the caster can cast the spell intrinsically.
    :return: The bonus to the maneuver.
    """
    if can_cast:
        trace.flow("Can cast intrinsically: +30")
        return CAN_CAST_BONUS
    else:
        return 0

class UseItemsManeuverTable(PowerAwarenessManeuverTable):

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_known_realm_frame():
            """
            Create a frame with a Checkbox indicating whether the character knows
            the spell realm.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, KNOW_REALM_TEXT, self.known_realm)
            trace.exit()

        def setup_known_spell_frame():
            """
            Create a frame with a Checkbox indicating whether the character knows
            the spell.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, KNOW_SPELL_TEXT, self.known_spell)
            trace.exit()

        def setup_different_realm_frame():
            """
            Create a frame with a Checkbox indicating whether the character's realm
            differs from the spell.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(
                parent_frame, DIFFERENT_REALM_TEXT, self.different_realm)
            trace.exit()

        def setup_can_cast_frame():
            """
            Create a frame with a Checkbox indicating whether the character can cast
            the spell intrinsically.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, CAN_CAST_TEXT, self.can_cast)
            trace.exit()
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.known_realm = IntVar()
        self.known_spell = IntVar()
        self.different_realm = IntVar()
        self.can_cast = IntVar()
        setup_known_realm_frame()
        setup_known_spell_frame()
        setup_different_realm_frame()
        setup_can_cast_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += known_realm_bonus(self.known_realm.get())
        bonus += known_spell_bonus(self.known_spell.get())
        bonus += different_realm_bonus(self.different_realm.get())
        bonus += intrinsic_cast_bonus(self.can_cast.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
