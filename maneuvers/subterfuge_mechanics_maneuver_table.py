# -*- coding: utf-8 -*-
"""
The Subterfuge/Mechanics static maneuver table.

Classes:
    SelfControlManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
import trace_log as trace

sys.path.append('../')


class SubterfugeMechanicsManeuverTable(StaticManeuverTable):
    """
    Subterfuge/Mechanics static maneuver table.

    Methods:
        select_subterfuge_mechanics_table(maneuver_type)
    """
    MANEUVER_CAMOUFLAGE = "Camouflage"
    MANEUVER_DISARM_TRAPS = "Disarm Traps"
    MANEUVER_DISGUISE = "Disguise"
    MANEUVER_COUNTERFEITING = "Counterfeiting"
    MANEUVER_FORGERY = "Forgery"
    MANEUVER_HIDING_ITEMS = "Hiding Items"
    MANEUVER_PICK_LOCKS = "Pick Locks"
    MANEUVER_SET_TRAPS = "Set Traps"
    MANEUVER_TRAP_BUILDING = "Trap Building"
    MANEUVER_USE_REMOVE_POISON = "Use/Remove Poison"

    maneuver_type_options = (
        MANEUVER_CAMOUFLAGE, MANEUVER_DISARM_TRAPS, MANEUVER_DISGUISE,
        MANEUVER_COUNTERFEITING, MANEUVER_FORGERY, MANEUVER_HIDING_ITEMS,
        MANEUVER_PICK_LOCKS, MANEUVER_SET_TRAPS, MANEUVER_TRAP_BUILDING,
        MANEUVER_USE_REMOVE_POISON
    )

    maneuver_result_text = {
        BLUNDER:
            "You are convinced that you must be simply a character in some macabre "
            "game.  The worst possible result occurs (a trap goes off on you, your "
            "lockpick breaks off within the mechanism, you poison yourself, you break "
            "or lose the item you are trying to hide, etc.).  You may not try again.  "
            "This only happens in stories, doesn't it?  Perhaps you should get a day "
            "job.",
        ABSOLUTE_FAILURE:
            "Your subterfuge SEEMS to work, but in fact it will come apart during its "
            "first authentic use.  There is a 50% chance that it will activate, "
            "affecting you.  Hopefully you are careful enough to avoid having it "
            "traced back to you.  Regardless, you may not try again.",
        FAILURE:
            "Your attempt fails utterly.  You are crushed.  There is a 20% chance "
            "that the mechanism will, in fact, activate, affecting you.  You may not "
            "try again for at least 24 hours.",
        PARTIAL_SUCCESS:
            "Your attempt is marginal.  You can't seem to do any better, but anyone "
            "attempting to circumvent your subterfuge will receive a modification of "
            "+20.  You sigh in exasperation.",
        NEAR_SUCCESS:
            "You believe you have finished, and sign off on your work as complete, but "
            "d5 rounds later, you realise that you have forgotten one key element.  "
            "If it is possible to return to your work with your tools, you may make the "
            "necessary adjustment for normal operation with a roll modified by +10. "
            "If not, your attempt will fail.  At least you know what went wrong.",
        SUCCESS:
            "With a sly smile, you place the polishing touch on your subterfuge.  "
            "Success!  A masterpiece, certainly, but is it art?",
        ABSOLUTE_SUCCESS:
            "Incredible!  Your skills have soared!  Your subterfuge is so perfect that "
            "any attempt to pierce it receives a modification of -20 in addition to "
            "any other modifiers."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -20),
        ABSOLUTE_FAILURE: (-25, 1, 0),
        FAILURE: (0, 1.5, 0),
        PARTIAL_SUCCESS: (20, 2, 5),
        NEAR_SUCCESS: (90, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_subterfuge_mechanics_table(maneuver_type):
        """
        Set the current SubterfugeMechanics maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.subterfuge_mechanics.pick_locks_maneuver_table import PickLocksManeuverTable

        if maneuver_type == SubterfugeMechanicsManeuverTable.MANEUVER_PICK_LOCKS:
            trace.flow("Pick Locks")
            return PickLocksManeuverTable()
        else:
            trace.flow("Subterfuge/Mechanics")
            return SubterfugeMechanicsManeuverTable()
