# -*- coding: utf-8 -*-
"""
The base static maneuver table.

Classes:
    StaticManeuverTable
"""
from __future__ import absolute_import
import sys

from tkinter import StringVar
from tkinter.ttk import OptionMenu

from maneuvers.maneuver_utils import setup_maneuver_difficulty_frame, maneuver_difficulty_options, \
    ROUTINE, EASY, LIGHT, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD

import dice
import trace_log as trace
import frame_utils

sys.path.append('../')

MANEUVER_DIFFICULTY_LABEL_TEXT = "Maneuver difficulty: "

DIFFICULTY_DEFAULT = MEDIUM

maneuver_difficulty_bonuses = {
    ROUTINE: 30,
    EASY: 20,
    LIGHT: 10,
    MEDIUM: 0,
    HARD: -10,
    VERY_HARD: -20,
    EXTREMELY_HARD: -30,
    SHEER_FOLLY: -50,
    ABSURD: -70
}

ABSOLUTE_FAILURE_RESULT = -25
FAILURE_RESULT = 5
PARTIAL_SUCCESS_RESULT = 76
NEAR_SUCCESS_RESULT = 91
SUCCESS_RESULT = 111
ABSOLUTE_SUCCESS_RESULT = 176

BLUNDER = "BLUNDER: "
ABSOLUTE_FAILURE = "ABSOLUTE FAILURE: "
FAILURE = "FAILURE: "
PARTIAL_SUCCESS = "PARTIAL SUCCESS: "
NEAR_SUCCESS = "NEAR SUCCESS: "
SUCCESS = "SUCCESS: "
ABSOLUTE_SUCCESS = "ABSOLUTE_SUCCESS: "


class StaticManeuverTable:
    """
    The base static maneuver table.  Overridden by per-skill static maneuver tables.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        setup_maneuver_table_frames(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        setup_maneuver_fumble_frame(parent_frame)
        difficulty_bonus(self)
        table_bonus(self)
        skill_type_bonus(self)
        maneuver_resolution(self, roll)
        result_text(self, result)
        result_stats(self, result)
        resolve_fumble()
    """
    maneuver_result_text = {
        BLUNDER:
            "You fail spectacularly.  If possible, your action has the opposite effect from what "
            "you intended.",
        ABSOLUTE_FAILURE:
            "Utter incompetence causes a mental lapse.  "
            "Any static actions attempted during the next 10 min (60 rounds) will result in "
            "Failure.",
        FAILURE:
            "You have failed.  You may not try again the same action in the same place for 1 day.",
        PARTIAL_SUCCESS:
            "If partial success is possible, you accomplish 20% of your action.  "
            "You may not try the same action in the same place for 1 hour.",
        NEAR_SUCCESS:
            "If partial success is possible, you accomplish half of your action.  "
            "You may try again after 3 rounds of contemplation.",
        SUCCESS:
            "Your action is successful.",
        ABSOLUTE_SUCCESS:
            "Your action is successful.  "
            "You get a +20 bonus to further static actions for the next 10 minutes (60 rounds)."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 5, -30),
        ABSOLUTE_FAILURE: (-20, 3, -10),
        FAILURE: (0, 2, 0),
        PARTIAL_SUCCESS: (20, 1.5, 5),
        NEAR_SUCCESS: (80, 1.25, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.75, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        dice.randomize()
        self.maneuver_difficulty = StringVar()
        self.maneuver_difficulty_options = maneuver_difficulty_options
        self.maneuver_difficulty_selector = \
            OptionMenu(
                None,
                self.maneuver_difficulty,
                MEDIUM,
                *self.maneuver_difficulty_options)
        self.maneuver_type = kwargs.get('maneuver_type', None)
        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        """
        Creates a frame to allow selection of the maneuver difficulty using an OptionMenu widget.
        """
        setup_maneuver_difficulty_frame(self, parent_frame)

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        # pylint: disable=no-self-use
        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        parent_frame.pack()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the chosen skill.
        """
        # pylint: disable=no-self-use
        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        parent_frame.pack()

        trace.exit()

    @staticmethod
    def setup_maneuver_fumble_frame(parent_frame):
        """
        Set up the frame to handle maneuver fumble.
        This is not required for a Static Maneuver, so the method is empty.
        """

    def difficulty_bonus(self):
        """
        Determine the difficulty to apply to a maneuver based on its difficulty.
        :return: The maneuver difficulty bonus
        """
        trace.entry()

        bonus = maneuver_difficulty_bonuses[self.maneuver_difficulty.get()]
        trace.detail("Returning %d" % bonus)

        trace.exit()
        return bonus

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        # pylint: disable=no-self-use
        trace.entry()

        trace.exit()
        return 0

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        # pylint: disable=no-self-use
        trace.entry()

        trace.exit()
        return 0

    def maneuver_resolution(self, roll):
        """
        Resolve the maneuver based on the modified roll.
        This method may carry out side-effects based on the resolution of the maneuver.
        :param roll: The modified roll.
        :return: A ManeuverResult containing the text output of the resolution and
        statistics about the effectiveness of the maneuver.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from .maneuver_table import ManeuverResult

        if roll >= ABSOLUTE_SUCCESS_RESULT:
            trace.flow("Absolute success")
            maneuver_result_text = ABSOLUTE_SUCCESS + self.result_text(ABSOLUTE_SUCCESS)
            maneuver_result_stats = self.result_stats(ABSOLUTE_SUCCESS)

        elif roll >= SUCCESS_RESULT:
            trace.flow("Success")
            maneuver_result_text = SUCCESS + self.result_text(SUCCESS)
            maneuver_result_stats = self.result_stats(SUCCESS)

        elif roll >= NEAR_SUCCESS_RESULT:
            trace.flow("Near success")
            maneuver_result_text = NEAR_SUCCESS + self.result_text(NEAR_SUCCESS)
            maneuver_result_stats = self.result_stats(NEAR_SUCCESS)

        elif roll >= PARTIAL_SUCCESS_RESULT:
            trace.flow("Partial success")
            maneuver_result_text = PARTIAL_SUCCESS + self.result_text(PARTIAL_SUCCESS)
            maneuver_result_stats = self.result_stats(PARTIAL_SUCCESS)

        elif roll >= FAILURE_RESULT:
            trace.flow("Failure")
            maneuver_result_text = FAILURE + self.result_text(FAILURE)
            maneuver_result_stats = self.result_stats(FAILURE)

        elif roll >= ABSOLUTE_FAILURE_RESULT:
            trace.flow("Absolute Failure")
            maneuver_result_text = ABSOLUTE_FAILURE + self.result_text(ABSOLUTE_FAILURE)
            maneuver_result_stats = self.result_stats(ABSOLUTE_FAILURE)

        else:
            trace.flow("Blunder")
            maneuver_result_text = BLUNDER + self.result_text(BLUNDER)
            maneuver_result_stats = self.result_stats(BLUNDER)

        return ManeuverResult(maneuver_result_text,
                              maneuver_result_stats[0],
                              maneuver_result_stats[1],
                              maneuver_result_stats[2],
                              False)

    def result_text(self, result):
        """
        Return the text to report for the maneuver result.
        :param result: The type of result achieved.
        """
        trace.detail("Result is %r" % result)
        return self.maneuver_result_text[result]

    def result_stats(self, result):
        """
        Return statistics about the effectiveness of the maneuver.
        :param result: The type of result achieved.
        """
        return self.maneuver_result_stats[result]

    @staticmethod
    def resolve_fumble():
        """
        Resolve a fumble roll.  This is never made for a static maneuver, so
        asserts.
        """
        assert False

    @staticmethod
    def get_maneuver_preferred_skills(_):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param _: The type of maneuver selected.
        """
        return []
