# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Maneuvers.StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')


class AwarenessSearchingManeuverTable(StaticManeuverTable):
    MANEUVER_DETECT_TRAPS = "Detect Traps"
    MANEUVER_LIE_PERCEPTION = "Lie Perception"
    MANEUVER_LOCATE_HIDDEN = "Locate Hidden"
    MANEUVER_OBSERVATION = "Observation"
    MANEUVER_POISON_PERCEPTION = "Poison Perception"
    MANEUVER_READING_TRACKS = "Reading Tracks"
    MANEUVER_SURVEILLANCE = "Surveillance"
    MANEUVER_TRACKING = "Tracking"

    maneuver_type_options = (
        MANEUVER_DETECT_TRAPS, MANEUVER_LIE_PERCEPTION, MANEUVER_LOCATE_HIDDEN,
        MANEUVER_OBSERVATION, MANEUVER_POISON_PERCEPTION, MANEUVER_READING_TRACKS,
        MANEUVER_SURVEILLANCE, MANEUVER_TRACKING
    )

    maneuver_result_text = {
        BLUNDER:
            "You gain enormous amounts of information about your target... all of it wrong.  A "
            "dangerous target will be perceived as safe, and vice versa.  You utterly "
            "misrepresent what you perceive, and you are _sure_ you are correct.",
        ABSOLUTE_FAILURE:
            "There is a great future waiting for you as an art critic.  You fail to notice even "
            "the most obvious information about your target.",
        FAILURE:
            "Attempting to emulate the perceptive abilities of an eggplant, you notice nothing "
            "useful.",
        PARTIAL_SUCCESS:
            "Your interest is piqued, but you can glean minimal information. "
            "You may try again in 6 rounds, if appropriate.",
        NEAR_SUCCESS:
            "Following your instincts, you focus your attention.  You gather some general "
            "information on your target, but not the specifics which you feel lie just beyond "
            "your grasp. "
            "If appropriate, roll again next round with a modification of +10 to pinpoint what "
            "has eluded you.",
        SUCCESS:
            "Extraordinary!.  Your finely-tuned perception has revealed that which you sought.",
        ABSOLUTE_SUCCESS:
            "Elementary, my dear boy!  You identify with casual ease the target and/or "
            "information you seek, along with contextual information not obvious to a lesser eye."
    }

    maneuver_result_stats = {
        BLUNDER: (-25, 1, -30),
        ABSOLUTE_FAILURE: (0, 2, -10),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (20, 1.75, 0),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 1, 30)
    }

    @staticmethod
    def select_awareness_searching_table(maneuver_type):
        """
        Set the current awareness/searching maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """

        from Maneuvers.AwarenessSearching.LiePerceptionManeuverTable import LiePerceptionManeuverTable
        from Maneuvers.AwarenessSearching.LocateHiddenManeuverTable import LocateHiddenManeuverTable
        from Maneuvers.AwarenessSearching.ObservationManeuverTable import ObservationManeuverTable
        from Maneuvers.AwarenessSearching.SurveillanceManeuverTable import SurveillanceManeuverTable

        if maneuver_type == AwarenessSearchingManeuverTable.MANEUVER_LIE_PERCEPTION:
            trace.flow("Lie Perception maneuver")
            trace.exit()
            return LiePerceptionManeuverTable()
        elif maneuver_type == AwarenessSearchingManeuverTable.MANEUVER_LOCATE_HIDDEN:
            trace.flow("Locate Hidden maneuver")
            trace.exit()
            return LocateHiddenManeuverTable()
        elif maneuver_type == AwarenessSearchingManeuverTable.MANEUVER_OBSERVATION:
            trace.flow("Observation maneuver")
            trace.exit()
            return ObservationManeuverTable()
        elif maneuver_type == AwarenessSearchingManeuverTable.MANEUVER_SURVEILLANCE:
            trace.flow("Surveillance maneuver")
            trace.exit()
            return SurveillanceManeuverTable()
        else:
            return AwarenessSearchingManeuverTable()
