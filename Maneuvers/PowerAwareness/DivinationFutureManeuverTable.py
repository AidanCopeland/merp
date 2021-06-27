# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.PowerAwarenessManeuverTable import PowerAwarenessManeuverTable
from Maneuvers.StaticManeuverTable import BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from tkinter.ttk import Frame, Label, OptionMenu

import FrameUtils
import trace_log as trace

from tkinter import LEFT, RIGHT, BOTH, RAISED, IntVar
standard_library.install_aliases()

sys.path.append('../')


TIME_PROMPT = "Distance into future (no more than): "

TEN_MINUTES = "10 minutes"
THIRTY_MINUTES = "30 minutes"
ONE_HOUR = "1 hour"
SIX_HOURS = "6 hours"
TWELVE_HOURS = "12 hours"
ONE_DAY = "1 day"
ONE_WEEK = "1 week"
ONE_MONTH = "1 month"
SIX_MONTHS = "6 months"

TIME_DEFAULT = SIX_HOURS

time_options = (
    TEN_MINUTES, THIRTY_MINUTES, ONE_HOUR, SIX_HOURS, TWELVE_HOURS, ONE_DAY,
    ONE_WEEK, ONE_MONTH, SIX_MONTHS
)

maneuver_difficulty_bonuses = {
    TEN_MINUTES: 30,
    THIRTY_MINUTES: 20,
    ONE_HOUR: 10,
    SIX_HOURS: 0,
    TWELVE_HOURS: -10,
    ONE_DAY: -20,
    ONE_WEEK: -30,
    ONE_MONTH: -50,
    SIX_MONTHS: -70
}

MAJOR_FACTOR_TEXT = "Major influencing factor on the future"

MAJOR_FACTOR_BONUS = -30
MINOR_FACTOR_BONUS = -70


def major_factor_bonus(major_factor):
    """
    Determine the bonus to the maneuver based on whether this is a major
    influencing factor on the future.
    :param major_factor: Whether this is a major influencing factor.
    :return: The bonus to the maneuver.
    """
    if major_factor == 1:
        trace.flow("Major factor: -30")
        return MAJOR_FACTOR_BONUS
    else:
        trace.flow("Minor factor: -70")
        return MINOR_FACTOR_BONUS


class DivinationFutureManeuverTable(PowerAwarenessManeuverTable):
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

    def __init__(self, **kwargs):
        trace.entry()
        super(PowerAwarenessManeuverTable, self).__init__(**kwargs)
        self.major_factor = IntVar()
        self.maneuver_difficulty_options = None
        self.maneuver_difficulty_selector = None

        trace.exit()

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
                SIX_HOURS,
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
            influencing factor on the future.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(
                parent_frame, MAJOR_FACTOR_TEXT, self.major_factor)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
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
