# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from Maneuvers.PowerAwarenessManeuverTable import \
    PowerAwarenessManeuverTable, BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from ttk import Frame, Label, OptionMenu

import FrameUtils
import trace_log as trace

from Tkinter import LEFT, RIGHT, BOTH, RAISED, IntVar

TIME_PROMPT = "Distance into past (no more than): "

TWELVE_HOURS = "12 hours"
ONE_DAY = "1 day"
ONE_WEEK = "1 week"
TWO_WEEKS = "2 weeks"
ONE_MONTH = "1 month"
THREE_MONTHS = "3 months"
SIX_MONTHS = "6 months"
ONE_YEAR = "1 year"
UNLIMITED = "Unlimited"

TIME_DEFAULT = TWO_WEEKS

time_options = (
    TWELVE_HOURS, ONE_DAY, ONE_WEEK, TWO_WEEKS, ONE_MONTH, THREE_MONTHS,
    SIX_MONTHS, ONE_YEAR, UNLIMITED
)

maneuver_difficulty_bonuses = {
    TWELVE_HOURS: 30,
    ONE_DAY: 20,
    ONE_WEEK: 10,
    TWO_WEEKS: 0,
    ONE_MONTH: -10,
    THREE_MONTHS: -20,
    SIX_MONTHS: -30,
    ONE_YEAR: -50,
    UNLIMITED: -70
}

MAJOR_FACTOR_TEXT = "Major influencing factor on the past"

MAJOR_FACTOR_BONUS = 10
MINOR_FACTOR_BONUS = -10

def major_factor_bonus(major_factor):
    """
    Determine the bonus to the maneuver based on whether this is a major
    influencing factor on the past.
    :param major_factor: Whether this is a major influencing factor.
    :return: The bonus to the maneuver.
    """
    if major_factor:
        trace.flow("Major factor: +10")
        return MAJOR_FACTOR_BONUS
    else:
        trace.flow("Minor factor: -10")
        return MINOR_FACTOR_BONUS


class DivinationPastManeuverTable(PowerAwarenessManeuverTable):

    maneuver_result_text = {
        BLUNDER:
            "Disaster strikes.  In your attempt at divination, you damage your apparatus "
            "through carelessness (e.g., tear a card, drop the crystal, lose a die, etc.) "
            "and the reading is ruined.  All future attempts at Divination will suffer a "
            "special modification of -50 until the apparatus is repaired or replaced.",
        ABSOLUTE_FAILURE:
            "You work the apparatus and produce a reading which you are certain is "
            "absolutely correct.  Your confidence is misplaced as the reading is "
            "completely wrong or utterly random (GM discretion).  Knowing the "
            "techniques is not enough….",
        FAILURE:
            "You work the apparatus and produce a reading.  You know the reading is a "
            "random result devoid of any meaning.  Perhaps the querent will be "
            "satisfied with a trusty rendition of ""You will meet a dark handsome "
            "stranger?""",
        PARTIAL_SUCCESS:
            "You have some flair with divination and your reading is quite perceptive. "
            "It is only 50% accurate (the other 50% of the reading comprises incorrect "
            "or random elements at GM discretion) and you don’t know which half is "
            "correct.",
        NEAR_SUCCESS:
            "With time, you might become an accomplished diviner.  Your reading is 75% "
            "accurate (the other 25% of the reading comprises incorrect or random "
            "elements at GM discretion) and you don’t know which portions are correct.",
        SUCCESS:
            "You have almost mastered the technique.  Your reading is 90% accurate (the "
            "remaining 10% of the reading comprises incorrect or random elements at GM "
            "discretion) and you don’t know which portions are incorrect.",
        ABSOLUTE_SUCCESS:
            "Your reading is 100% accurate. All you have to do is interpret it "
            "correctly.  Hopefully the querent is paying you well. "
            "Now how about those Lottery numbers, Nostradamus?"
    }

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=TIME_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = time_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                TWO_WEEKS,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_major_factor_frame():
            """
            Create a frame with a Checkbox indicating whether this is a major
            influencing factor on the past.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(
                parent_frame, MAJOR_FACTOR_TEXT, self.major_factor)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.major_factor = IntVar()
        setup_major_factor_frame()

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

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += major_factor_bonus(self.major_factor.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
