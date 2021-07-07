# -*- coding: utf-8 -*-
"""
Utility functions for Read Runes and Use Items static maneuvers.

Functions:
    known_realm_bonus(known_realm)
    known_spell_bonus(known_spell)
    different_realm_bonus(different_realm)
    intrinsic_cast_bonus(can_cast)
"""
import sys

import frame_utils
import trace_log as trace

sys.path.append('../')


KNOW_REALM_TEXT = "Character knows the realm of the spell"
KNOW_SPELL_TEXT = "Character know the spell"
DIFFERENT_REALM_TEXT = "Character's realm differs from spell"
DIFFERENT_BASE_TEXT = "Spell from a different base list to caster"
CAN_CAST_TEXT = "Character can cast spell intrinsically"

KNOWN_REALM_BONUS = 10
UNKNOWN_REALM_BONUS = -20

KNOWN_SPELL_BONUS = 20
UNKNOWN_SPELL_BONUS = -10

DIFFERENT_REALM_BONUS = -30
SAME_REALM_DIFFERENT_BASE_BONUS = -30
DIFFERENT_REALM_DIFFERENT_BASE_BONUS = -40
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
    the spell or ability is.
    :param known_spell: Whether the character knows what the spell is.
    :return: The bonus to the maneuver.
    """
    if known_spell:
        trace.flow("Known spell: +20")
        return KNOWN_SPELL_BONUS
    else:
        trace.flow("Unknown spell: -10")
        return UNKNOWN_SPELL_BONUS


def different_realm_bonus(different_realm, different_base):
    """
    Determine the bonus to the maneuver based on whether the caster's realm
    and/or base differs from the spell's.
    :param different_realm: Whether the caster's realm differs from the
    spell's.
    :param different_base: Whether the spell is from a different profession's
    base spell lists to the caster's.
    :return: The bonus to the maneuver.
    """
    if different_realm and different_base:
        trace.flow("Different realm and base: -40")
        return DIFFERENT_REALM_DIFFERENT_BASE_BONUS
    elif different_realm:
        trace.flow("Different realm: -30")
        return DIFFERENT_REALM_BONUS
    elif different_base:
        trace.flow("Different base: -30")
        return SAME_REALM_DIFFERENT_BASE_BONUS
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


def setup_known_realm_frame(table, parent_frame):
    """
    Create a frame with a Checkbox indicating whether the character knows
    the spell realm.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_checkbox_frame(parent_frame, KNOW_REALM_TEXT, table.known_realm)
    trace.exit()


def setup_known_spell_frame(table, parent_frame):
    """
    Create a frame with a Checkbox indicating whether the character knows
    the spell.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_checkbox_frame(parent_frame, KNOW_SPELL_TEXT, table.known_spell)
    trace.exit()


def setup_different_realm_frame(table, parent_frame):
    """
    Create a frame with a Checkbox indicating whether the character's realm
    differs from the spell.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_checkbox_frame(
        parent_frame, DIFFERENT_REALM_TEXT, table.different_realm)
    trace.exit()


def setup_can_cast_frame(table, parent_frame):
    """
    Create a frame with a Checkbox indicating whether the character can cast
    the spell intrinsically.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_checkbox_frame(parent_frame, CAN_CAST_TEXT, table.can_cast)
    trace.exit()
