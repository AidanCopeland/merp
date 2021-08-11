# -*- coding: utf-8 -*-
"""
The Awareness/Searching static maneuver table.

Classes:
    AwarenessSearchingManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.general_skills import SKILL_READING_TRACKS, SKILL_TRACK
from console.character.subterfuge_skills import \
    SKILL_LIE_PERCEPTION, SKILL_POISON_PERCEPTION, SKILL_SURVEILLANCE, SKILL_INTERROGATION, \
    SKILL_POISON_LORE
from console.character.secondary_skills import \
    SKILL_DETECT_TRAPS, SKILL_LOCATE_HIDDEN, SKILL_OBSERVATION, SKILL_PERCEPTION, \
    SKILL_DISCERN_WOUNDS, SKILL_FIRST_AID
import trace_log as trace

sys.path.append('../')


class AwarenessSearchingManeuverTable(StaticManeuverTable):
    """
    Awareness/Searching static maneuver table.

    Methods:
        select_awareness_searching_table(maneuver_type)
    """
    MANEUVER_DETECT_TRAPS = "Detect Traps"
    MANEUVER_DISCERN_WOUNDS = "Discern Wounds"
    MANEUVER_LIE_PERCEPTION = "Lie Perception"
    MANEUVER_LOCATE_HIDDEN = "Locate Hidden"
    MANEUVER_OBSERVATION = "Observation"
    MANEUVER_POISON_PERCEPTION = "Poison Perception"
    MANEUVER_READING_TRACKS = "Reading Tracks"
    MANEUVER_SURVEILLANCE = "Surveillance"
    MANEUVER_TRACKING = "Tracking"

    maneuver_type_options = (
        MANEUVER_DETECT_TRAPS, MANEUVER_DISCERN_WOUNDS, MANEUVER_LIE_PERCEPTION,
        MANEUVER_LOCATE_HIDDEN, MANEUVER_OBSERVATION, MANEUVER_POISON_PERCEPTION,
        MANEUVER_READING_TRACKS, MANEUVER_SURVEILLANCE, MANEUVER_TRACKING
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
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.awareness_searching.lie_perception_maneuver_table import \
            LiePerceptionManeuverTable
        from maneuvers.awareness_searching.locate_hidden_maneuver_table import \
            LocateHiddenManeuverTable
        from maneuvers.awareness_searching.observation_surveillance_maneuver_table import \
            ObservationSurveillanceManeuverTable

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
            return ObservationSurveillanceManeuverTable()
        elif maneuver_type == AwarenessSearchingManeuverTable.MANEUVER_SURVEILLANCE:
            trace.flow("Surveillance maneuver")
            trace.exit()
            return ObservationSurveillanceManeuverTable()
        else:
            return AwarenessSearchingManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            AwarenessSearchingManeuverTable.MANEUVER_LIE_PERCEPTION:
                [SKILL_LIE_PERCEPTION, SKILL_INTERROGATION],
            AwarenessSearchingManeuverTable.MANEUVER_LOCATE_HIDDEN:
                [SKILL_LOCATE_HIDDEN, SKILL_PERCEPTION],
            AwarenessSearchingManeuverTable.MANEUVER_OBSERVATION:
                [SKILL_OBSERVATION, SKILL_PERCEPTION],
            AwarenessSearchingManeuverTable.MANEUVER_SURVEILLANCE:
                [SKILL_SURVEILLANCE, SKILL_PERCEPTION],
            AwarenessSearchingManeuverTable.MANEUVER_DETECT_TRAPS:
                [SKILL_DETECT_TRAPS, SKILL_PERCEPTION],
            AwarenessSearchingManeuverTable.MANEUVER_POISON_PERCEPTION:
                [SKILL_POISON_PERCEPTION, SKILL_PERCEPTION, SKILL_POISON_LORE],
            AwarenessSearchingManeuverTable.MANEUVER_READING_TRACKS:
                [SKILL_READING_TRACKS, SKILL_TRACK],
            AwarenessSearchingManeuverTable.MANEUVER_DISCERN_WOUNDS:
                [SKILL_DISCERN_WOUNDS, SKILL_FIRST_AID],
            AwarenessSearchingManeuverTable.MANEUVER_TRACKING:
                [SKILL_TRACK, SKILL_READING_TRACKS]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
