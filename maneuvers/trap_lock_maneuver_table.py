# -*- coding: utf-8 -*-
"""
The Pick Locks/Disarm Traps static maneuver table.

Classes:
    TrapLockManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.subterfuge_skills import SKILL_PICK_LOCK, SKILL_DISARM_TRAP
sys.path.append('../')


class TrapLockManeuverTable(StaticManeuverTable):
    """
    Pick Locks/Disarm Traps static maneuver table.
    """
    maneuver_result_text = {
        BLUNDER:
            "If picking a lock, your lockpick is broken and stuck in the lock, rendering it "
            "unopenable until removed (this requires another roll to pick the lock by someone "
            "other than you). "
            "Any traps are set off.",
        ABSOLUTE_FAILURE:
            "You have developed a mental block on this lock/trap and will automatically fail on"
            "any further attempts to pick/disarm it. "
            "There is a 50% chance that any traps will be activated.",
        FAILURE:
            "Currently you have no further ideas on how to pick/disarm this lock/trap. "
            "After 24 hours you may make a Perception roll and if it succeeds you may make another "
            "attempt.",
        PARTIAL_SUCCESS:
            "You have figured out part of the lock/trap and have an intuitive feel for the rest. "
            "Do something else for 10 minutes and then you can try again.",
        NEAR_SUCCESS:
            "You almost had it. If you spend 2 rounds thinking about your attempt (no other "
            "activity), you may try again with an extra +5 bonus.",
        SUCCESS:
            "The lock/trap is picked/disarmed.  +50 on any future attempts to pick/disarm this "
            "lock/trap.",
        ABSOLUTE_SUCCESS:
            "In the future you may automatically pick/disarm (takes one round) this lock/trap or "
            "any identical lock/trap.  +10 to attempts on similar locks/traps in the future."
    }

    @staticmethod
    def get_maneuver_preferred_skills(_):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param _: The type of maneuver selected.
        """
        return [SKILL_PICK_LOCK, SKILL_DISARM_TRAP]
