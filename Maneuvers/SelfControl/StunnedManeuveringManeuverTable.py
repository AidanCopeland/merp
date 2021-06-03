# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.SelfControlManeuverTable import \
    SelfControlManeuverTable, BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from ttk import Frame, Label, OptionMenu
from Tkinter import IntVar

import FrameUtils
import trace_log as trace

from Tkinter import LEFT, RIGHT, BOTH, RAISED

TIME_PROMPT = "Number of rounds stunned: "

ONE_TO_THREE = "1 - 3"
FOUR_TO_FIVE = "4 - 5"
SIX_TO_EIGHT = "6 - 8"
NINE_TO_ELEVEN = "9 - 11"
TWELVE_TO_FIFTEEN = "12 - 15"
SIXTEEN_PLUS = "16+"

DEFAULT_STUN = ONE_TO_THREE

stun_options = (
    ONE_TO_THREE, FOUR_TO_FIVE, SIX_TO_EIGHT,
    NINE_TO_ELEVEN, TWELVE_TO_FIFTEEN, SIXTEEN_PLUS
)

maneuver_difficulty_bonuses = {
    ONE_TO_THREE: 0,
    FOUR_TO_FIVE: -10,
    SIX_TO_EIGHT: -20,
    NINE_TO_ELEVEN: -30,
    TWELVE_TO_FIFTEEN: -50,
    SIXTEEN_PLUS: -70
}

FIGHT_THROUGH_TEXT = "Fight through stun, instead of relieving accumulated stun?"


class StunnedManeuveringManeuverTable(SelfControlManeuverTable):

    maneuver_result_stats = {
        BLUNDER: (0, 1, -20),
        ABSOLUTE_FAILURE: (0, 1, -25),
        FAILURE: (0, 1, -5),
        PARTIAL_SUCCESS: (100, 1, 0),
        NEAR_SUCCESS: (100, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (100, 1, 30)
    }

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=TIME_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = stun_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                ONE_TO_THREE,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

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

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_fight_through_frame():
            """
            Create a frame with a Checkbox indicating whether immediate action is required.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, FIGHT_THROUGH_TEXT, self.fight_through)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.fight_through = IntVar()
        self.fight_through.set(0)
        setup_fight_through_frame()

        trace.exit()

    def result_text(self, result):
        """
        Return additional text to report for the maneuver result.
        :param result: The type of result achieved.
        """
        rounds_stun_relieved = self.rounds_stun_relieved[result]

        if rounds_stun_relieved < 0:
            trace.flow("Additional stun")
            return str("In your attempt to relieve your condition, you have merely worsened it.  Stun increases by %d "
                       "rounds." % -rounds_stun_relieved)
        elif rounds_stun_relieved == 0:
            trace.flow("No effect")
            return str("Your efforts have no effect, and your amount of accumulated stun is unchanged.")
        else:
            trace.flow("Stun relieved")
            if self.fight_through.get() == 0:
                trace.flow("Relieve accumulated stun")
                return str("Your accumulated stun is reduced by %d rounds." % rounds_stun_relieved)
            else:
                trace.flow("Act immediately")
                act_rounds = (rounds_stun_relieved + 1) / 2
                return str("You may act for %d rounds, during which time your accumulated stun will reduce normally." % act_rounds)

    rounds_stun_relieved = {
        BLUNDER: -3,
        ABSOLUTE_FAILURE: -2,
        FAILURE: -1,
        PARTIAL_SUCCESS: 0,
        NEAR_SUCCESS: 1,
        SUCCESS: 2,
        ABSOLUTE_SUCCESS: 3
    }
