# -*- coding: utf-8 -*-
"""
Utility functions for artistic/active static maneuvers.

Functions:
    SingingManeuverTable
"""
import sys

from maneuvers.artistic_active_maneuver_table import PARTNER_PENALTY, LORE_BONUS

import trace_log as trace

sys.path.append('../')


BAD_LANGUAGE_TEXT = "Only one skill rank in language?"

BAD_LANGUAGE_PENALTY = 20
IMPROVISATION_PENALTY = 30


def table_bonus(table):
    """
    Determine any additional bonuses to apply to a maneuver based on factors
    specific to this maneuver type.
    :param: The calling table instance.
    :return: The additional maneuver bonus
    """
    trace.entry()

    bonus = 0
    trace.detail("Practised bonus: %d" % table.practised_bonus.get())
    bonus += table.practised_bonus.get()
    if table.is_improvised.get() == 1:
        trace.flow("Improvised: -30")
        bonus += IMPROVISATION_PENALTY

    if table.with_partner.get() == 1:
        trace.flow("With partner: -10")
        bonus += PARTNER_PENALTY

    if table.lore_skill.get() == 1:
        trace.flow("Lore skill: +10")
        bonus += LORE_BONUS

    trace.detail("Bonus %d" % bonus)

    trace.exit()
    return bonus
