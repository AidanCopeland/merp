# -*- coding: utf-8 -*-
import sys

from StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')


class PowerAwarenessManeuverTable(StaticManeuverTable):
    MANEUVER_ATTUNEMENT = "Attunement"
    MANEUVER_USE_ITEMS = "Use Items"
    MANEUVER_DIVINATION_PAST = "Divination (past)"
    MANEUVER_DIVINATION_FUTURE = "Divination (future)"
    MANEUVER_POWER_PERCEPTION = "Power Perception"
    MANEUVER_READ_RUNES = "Read Runes"

    maneuver_type_options = (
        MANEUVER_ATTUNEMENT, MANEUVER_USE_ITEMS, MANEUVER_DIVINATION_PAST,
        MANEUVER_DIVINATION_FUTURE, MANEUVER_POWER_PERCEPTION, MANEUVER_READ_RUNES
    )

    maneuver_result_text = {
        BLUNDER:
            "Your carelessness earns misfortune.  You stare into the source of magic, "
            "and it blinds you as a gaze into the sun.  Your inner eye (and thus all "
            "skills in this category) is at a -30 modifications for the next month.  "
            "You probably don't look both ways when crossing the street, do you?  "
            "The spell, if any, goes off.",
        ABSOLUTE_FAILURE:
            "Great Jumpin' Lizards!  Your attempt to tune your senses to mystical forces "
            "yields a power backlash!  Roll on the Non-Attack / Other Spell category of "
            "the Spell Failure Table.  The spell, if any, goes off.",
        FAILURE:
            "The forces you seek elude you.  Perhaps a period of meditation would clear "
            "your mind for another attempt.  Then again, you may be beyond hope.",
        PARTIAL_SUCCESS:
            "You see what you are after, but it is meaningless to you.  Your frame of "
            "reference is inappropriate to this venue.  You may try again only after "
            "resting for 1 hour.  The realm of the spell (if any) is known.",
        NEAR_SUCCESS:
            "Despite your best efforts, things remain just out of focus.  Another "
            "attempt, if appropriate, may be made at +10 to clarify matters.  The spell "
            "(if any) is known.",
        SUCCESS:
            "Your mystical senses are at your beck.  Your maneuver succeeds normally.  "
            "The spell, if any, is known and usable.",
        ABSOLUTE_SUCCESS:
            "You slip into the realm of the magical with effortless grace, discerning "
            "all you seek and more.  You stare beyond the superficial into the workings "
            "of the forces you examine.  Of course, this may be more than you wanted to "
            "know... be careful what you ask for, as you may get it!  "
            "The spell if any, is known and usable."
    }

    maneuver_result_stats = {
        BLUNDER: (-100, 2, -30),
        ABSOLUTE_FAILURE: (-20, 1.5, -10),
        FAILURE: (0, 1.25, -5),
        PARTIAL_SUCCESS: (20, 1.25, 0),
        NEAR_SUCCESS: (80, 1.25, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.75, 30)
    }

    @staticmethod
    def select_power_awareness_table(maneuver_type):
        """
        Set the current PowerAwareness maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """

        from Maneuvers.PowerAwareness.UseItemsManeuverTable import UseItemsManeuverTable
        from Maneuvers.PowerAwareness.DivinationPastManeuverTable import DivinationPastManeuverTable
        from Maneuvers.PowerAwareness.DivinationFutureManeuverTable import DivinationFutureManeuverTable
        from Maneuvers.PowerAwareness.ReadRunesManeuverTable import ReadRunesManeuverTable

        if maneuver_type == PowerAwarenessManeuverTable.MANEUVER_USE_ITEMS:
            trace.flow("Use items maneuver")
            trace.exit()
            return UseItemsManeuverTable()
        elif maneuver_type == PowerAwarenessManeuverTable.MANEUVER_DIVINATION_PAST:
            trace.flow("Divination (past) maneuver")
            trace.exit()
            return DivinationPastManeuverTable()
        elif maneuver_type == PowerAwarenessManeuverTable.MANEUVER_DIVINATION_FUTURE:
            trace.flow("Divination (future) maneuver")
            trace.exit()
            return DivinationFutureManeuverTable()
        elif maneuver_type == PowerAwarenessManeuverTable.MANEUVER_READ_RUNES:
            trace.flow("Read Runes maneuver")
            trace.exit()
            return ReadRunesManeuverTable()
        else:
            return PowerAwarenessManeuverTable()


