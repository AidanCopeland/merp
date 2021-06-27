# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Maneuvers.StaticManeuverTable import *

import trace_log as trace
from tkinter import IntVar
standard_library.install_aliases()

sys.path.append('../')

TARGET_TEXT = "Set bonus of +10 to +50 if there is a specific target"


class AwarenessPerceptionsManeuverTable(StaticManeuverTable):
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
            "trigger event entirely.  The red herring seems dangerous, and you focus your attention "
            "upon it entirely, giving any actions against you this round a modification of +20.",
        ABSOLUTE_FAILURE:
            "You are distracted by some minor bodily function (a fierce itch, a sneeze, a quest for "
            "nose gold, etc.), and utterly fail to notice the world around you for a few moments.",
        FAILURE:
            "Zzzzzzz.  You notice nothing.",
        PARTIAL_SUCCESS:
            "The back of your neck prickles a bit, but this feeling of ""missing something"" can't "
            "be pinpointed.  It was probably just that bit of melon you had for breakfast.",
        NEAR_SUCCESS:
            "Your hindbrain is apparently smarter than the rest of you.  If appropriate, you pull up "
            "short and try to pinpoint what has caught your attention by making another roll next "
            "round.",
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
        super(StaticManeuverTable, self).__init__(**kwargs)
        self.target_bonus = IntVar()

        trace.exit()

    @staticmethod
    def select_awareness_perceptions_table(maneuver_type):
        """
        Set the current awareness/perceptions maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """

        from Maneuvers.AwarenessPerceptions.SenseAmbushManeuverTable import SenseAmbushManeuverTable
        from Maneuvers.AwarenessPerceptions.AlertnessManeuverTable import AlertnessManeuverTable

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
            FrameUtils.setup_entry_frame(parent_frame, TARGET_TEXT, self.target_bonus)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
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
