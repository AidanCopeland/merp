# -*- coding: utf-8 -*-
"""
The Awareness/Perceptions static maneuver table.

Classes:
    AwarenessPerceptionsManeuverTable
"""
from __future__ import absolute_import
import sys
from tkinter import IntVar

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.weapon_skills import SKILL_COMBAT_AWARENESS
from console.character.secondary_skills import SKILL_PERCEPTION, SKILL_SENSE_AMBUSH, SKILL_ALERTNESS
import frame_utils
import trace_log as trace

sys.path.append('../')

TARGET_TEXT = "Set bonus of +10 to +50 if there is a specific target"


class AwarenessPerceptionsManeuverTable(StaticManeuverTable):
    """
    Awareness/Perceptions static maneuver table.

    Methods:
        select_awareness_perceptions_table(maneuver_type)
        setup_maneuver_table_frames(self, parent_frame)
        table_bonus(self)
    """
    MANEUVER_ALERTNESS = "Alertness"
    MANEUVER_COMBAT_AWARENESS = "Combat Awareness"
    MANEUVER_SENSE_AMBUSH = "Sense Ambush"

    maneuver_type_options = (
        MANEUVER_ALERTNESS, MANEUVER_COMBAT_AWARENESS, MANEUVER_SENSE_AMBUSH
    )

    # noinspection SpellCheckingInspection
    maneuver_result_text = {
        BLUNDER:
            "What was that?!  You are distracted by a figment of your own perception, and miss the "
            "trigger event entirely.  The red herring seems dangerous, and you focus your "
            "attention upon it entirely, giving any actions against you this round a modification "
            "of +20.",
        ABSOLUTE_FAILURE:
            "You are distracted by some minor bodily function (a fierce itch, a sneeze, a quest "
            "for nose gold, etc.), and utterly fail to notice the world around you for a few "
            "moments.",
        FAILURE:
            "Zzzzzzz.  You notice nothing.",
        PARTIAL_SUCCESS:
            "The back of your neck prickles a bit, but this feeling of ""missing something"" can't "
            "be pinpointed.  It was probably just that bit of melon you had for breakfast.",
        NEAR_SUCCESS:
            "Your hindbrain is apparently smarter than the rest of you.  If appropriate, you pull "
            "up short and try to pinpoint what has caught your attention by making another roll "
            "next round.",
        SUCCESS:
            "The angel hovering over your shoulder has something to tell you.  You notice the "
            "trigger for this maneuver, and may direct conscious activity to its observation.",
        ABSOLUTE_SUCCESS:
            "Almost before you can focus your attention on what your subconscious is telling you, "
            "you begin to react.  You gain one round's worth of direct observation through your "
            "overactive awareness of your environment.  This information is free of activity "
            "penalties, requiring no time to acquire."
    }

    maneuver_result_stats = {
        BLUNDER: (-20, 1, -20),
        ABSOLUTE_FAILURE: (-10, 1, -10),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (20, 1, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 1, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.target_bonus = IntVar()

        trace.exit()

    @staticmethod
    def select_awareness_perceptions_table(maneuver_type):
        """
        Set the current awareness/perceptions maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.awareness_perceptions.sense_ambush_maneuver_table import \
            SenseAmbushManeuverTable
        from maneuvers.awareness_perceptions.alertness_maneuver_table import AlertnessManeuverTable

        if maneuver_type == AwarenessPerceptionsManeuverTable.MANEUVER_SENSE_AMBUSH:
            trace.flow("Sense Ambush maneuver")
            trace.exit()
            return SenseAmbushManeuverTable()
        else:
            trace.flow("Alertness maneuver")
            trace.exit()
            return AlertnessManeuverTable()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_specific_target_frame():
            """
            Create a frame with an Entry indicating whether there is a specific target.
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, TARGET_TEXT, self.target_bonus)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.target_bonus.set(0)
        setup_specific_target_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        trace.detail("Specific target bonus: %d" % self.target_bonus.get())
        bonus += self.target_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            AwarenessPerceptionsManeuverTable.MANEUVER_SENSE_AMBUSH:
                [SKILL_SENSE_AMBUSH, SKILL_PERCEPTION],
            AwarenessPerceptionsManeuverTable.MANEUVER_COMBAT_AWARENESS:
                [SKILL_COMBAT_AWARENESS, SKILL_PERCEPTION],
            AwarenessPerceptionsManeuverTable.MANEUVER_ALERTNESS:
                [SKILL_ALERTNESS, SKILL_PERCEPTION]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
