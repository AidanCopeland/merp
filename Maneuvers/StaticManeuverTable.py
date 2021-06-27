# -*- coding: utf-8 -*-
from __future__ import absolute_import
from future import standard_library
from builtins import object
import sys

from tkinter import LEFT, RIGHT, BOTH, RAISED, StringVar
from tkinter.ttk import Frame, Label, OptionMenu

import dice
import trace_log as trace
import FrameUtils
standard_library.install_aliases()

sys.path.append('../')

MANEUVER_DIFFICULTY_LABEL_TEXT = "Maneuver difficulty: "

ROUTINE = "Routine"
EASY = "Easy"
LIGHT = "Light"
MEDIUM = "Medium"
HARD = "Hard"
VERY_HARD = "Very Hard"
EXTREMELY_HARD = "Extremely Hard"
SHEER_FOLLY = "Sheer Folly"
ABSURD = "Absurd"

DIFFICULTY_DEFAULT = MEDIUM

maneuver_difficulty_options = (
    ROUTINE, EASY, LIGHT, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD)

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


class StaticManeuverTable(object):
    maneuver_result_text = {
        BLUNDER: "You fail spectacularly.  If possible, your action has the opposite effect from what you intended.",
        ABSOLUTE_FAILURE: "Utter incompetence causes a mental lapse.  "
                          "Any static actions attempted during the next 10 min (60 rounds) will result in Failure.",
        FAILURE: "You have failed.  You may not try again the same action in the same place for 1 day.",
        PARTIAL_SUCCESS: "If partial success is possible, you accomplish 20% of your action.  "
                         "You may not try the same action in the same place for 1 hour.",
        NEAR_SUCCESS: "If partial success is possible, you accomplish half of your action."
                      "You may try again after 3 rounds of contemplation.",
        SUCCESS: "Your action is successful.",
        ABSOLUTE_SUCCESS: "Your action is successful.  "
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
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=MANEUVER_DIFFICULTY_LABEL_TEXT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = maneuver_difficulty_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                MEDIUM,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        parent_frame.pack()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the chosen skill.
        """
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
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
        trace.entry()

        trace.exit()
        return 0

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
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
        from .ManeuverTable import ManeuverResult

        if roll >= ABSOLUTE_SUCCESS_RESULT:
            trace.flow("Absolute success")
            maneuver_result_text = self.result_text(ABSOLUTE_SUCCESS)
            maneuver_result_stats = self.result_stats(ABSOLUTE_SUCCESS)
            return ManeuverResult(ABSOLUTE_SUCCESS +
                                  maneuver_result_text,
                                  maneuver_result_stats[0],
                                  maneuver_result_stats[1],
                                  maneuver_result_stats[2],
                                  False)
        elif roll >= SUCCESS_RESULT:
            trace.flow("Success")
            maneuver_result_text = self.result_text(SUCCESS)
            maneuver_result_stats = self.result_stats(SUCCESS)
            return ManeuverResult(SUCCESS +
                                  maneuver_result_text,
                                  maneuver_result_stats[0],
                                  maneuver_result_stats[1],
                                  maneuver_result_stats[2],
                                  False)
        elif roll >= NEAR_SUCCESS_RESULT:
            trace.flow("Near success")
            maneuver_result_text = self.result_text(NEAR_SUCCESS)
            maneuver_result_stats = self.result_stats(NEAR_SUCCESS)
            return ManeuverResult(NEAR_SUCCESS +
                                  maneuver_result_text,
                                  maneuver_result_stats[0],
                                  maneuver_result_stats[1],
                                  maneuver_result_stats[2],
                                  False)
        elif roll >= PARTIAL_SUCCESS_RESULT:
            trace.flow("Partial success")
            maneuver_result_text = self.result_text(PARTIAL_SUCCESS)
            maneuver_result_stats = self.result_stats(PARTIAL_SUCCESS)
            return ManeuverResult(PARTIAL_SUCCESS +
                                  maneuver_result_text,
                                  maneuver_result_stats[0],
                                  maneuver_result_stats[1],
                                  maneuver_result_stats[2],
                                  False)
        elif roll >= FAILURE_RESULT:
            trace.flow("Failure")
            maneuver_result_text = self.result_text(FAILURE)
            maneuver_result_stats = self.result_stats(FAILURE)
            return ManeuverResult(FAILURE +
                                  maneuver_result_text,
                                  maneuver_result_stats[0],
                                  maneuver_result_stats[1],
                                  maneuver_result_stats[2],
                                  False)
        elif roll >= ABSOLUTE_FAILURE_RESULT:
            trace.flow("Absolute Failure")
            maneuver_result_text = self.result_text(ABSOLUTE_FAILURE)
            maneuver_result_stats = self.result_stats(ABSOLUTE_FAILURE)
            return ManeuverResult(ABSOLUTE_FAILURE +
                                  maneuver_result_text,
                                  maneuver_result_stats[0],
                                  maneuver_result_stats[1],
                                  maneuver_result_stats[2],
                                  False)
        else:
            trace.flow("Blunder")
            maneuver_result_text = self.result_text(BLUNDER)
            maneuver_result_stats = self.result_stats(BLUNDER)
            return ManeuverResult(BLUNDER +
                                  maneuver_result_text,
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
