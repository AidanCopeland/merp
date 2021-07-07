# -*- coding: utf-8 -*-
"""
The Awareness/Senses static maneuver table.

Classes:
    AwarenessSensesManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
import trace_log as trace

sys.path.append('../')


class AwarenessSensesManeuverTable(StaticManeuverTable):
    """
    Awareness/Senses static maneuver table.

    Methods:
        select_awareness_senses_table(maneuver_type)
    """
    MANEUVER_DIRECTION_SENSE = "Direction Sense"
    MANEUVER_SENSE_AWARENESS = "Sense Awareness"
    MANEUVER_SITUATIONAL_AWARENESS = "Situational Awareness"
    MANEUVER_SLA = "Spatial Location Awareness"
    MANEUVER_TIME_SENSE = "Time Sense"

    maneuver_type_options = (
        MANEUVER_DIRECTION_SENSE, MANEUVER_SENSE_AWARENESS, MANEUVER_SITUATIONAL_AWARENESS,
        MANEUVER_SLA, MANEUVER_TIME_SENSE
    )

    maneuver_result_text = {
        BLUNDER:
            "Sensory overload renders you partially insensible with hallucinations and shock "
            "trauma; you are stunned for 1-10 rounds.  You will operate at a -20 modification "
            "(non-cumulative) to this skill until you receive a result of Absolute Success.",
        ABSOLUTE_FAILURE:
            "Your senses refuse to operate correctly.  Your disorientation renders you "
            "stunned for two rounds.",
        FAILURE:
            "You learn nothing of import.  Perhaps there _is_ nothing of import to learn... "
            "perhaps not.",
        PARTIAL_SUCCESS:
            "You are wary.  If another skill would be appropriate to the situation, you are "
            "aware of this and may utilize it.",
        NEAR_SUCCESS:
            "You have a vague grasp of the information you seek.  Time to pay attention.  If "
            "appropriate, you may roll again next round with a modification of +10.",
        SUCCESS:
            "Your senses never lie.  You pick up all pertinent information on your target or "
            "situation.",
        ABSOLUTE_SUCCESS:
            "The hairs on the back of your neck spring upright!  With preternatural intuition, "
            "you may react immediately (with no penalty) to any information you receive on your "
            "target or situation.  In addition, you receive unusual or extraneous information, "
            "and you may make a secondary static maneuver at no penalty to utilize this "
            "information (e.g., a Tactics roll, an attempt at identification, etc.)."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -20),
        ABSOLUTE_FAILURE: (-20, 1.5, -10),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (20, 1, 5),
        NEAR_SUCCESS: (80, 1.2, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.75, 30)
    }

    @staticmethod
    def select_awareness_senses_table(maneuver_type):
        """
        Set the current awareness/senses maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.awareness_senses.direction_sense_maneuver_table import \
            DirectionSenseManeuverTable
        from maneuvers.awareness_senses.sla_maneuver_table import SLAManeuverTable
        from maneuvers.awareness_senses.time_sense_maneuver_table import TimeSenseManeuverTable

        if maneuver_type == AwarenessSensesManeuverTable.MANEUVER_DIRECTION_SENSE:
            trace.flow("Direction Sense maneuver")
            trace.exit()
            return DirectionSenseManeuverTable()
        elif maneuver_type == AwarenessSensesManeuverTable.MANEUVER_SLA:
            trace.flow("Spatial Location Awareness maneuver")
            trace.exit()
            return SLAManeuverTable()
        elif maneuver_type == AwarenessSensesManeuverTable.MANEUVER_TIME_SENSE:
            trace.flow("Time Sense maneuver")
            trace.exit()
            return TimeSenseManeuverTable()
        else:
            return AwarenessSensesManeuverTable()
