# -*- coding: utf-8 -*-
"""
The Divination (past) static maneuver table.

Classes:
    DivinationPastManeuverTable
"""
import sys
from tkinter import LEFT, RIGHT, BOTH, RAISED, IntVar
from tkinter.ttk import Frame, Label, OptionMenu

from maneuvers.power_awareness.divination_maneuver_table import DivinationManeuverTable
import frame_utils
import trace_log as trace

sys.path.append('../')

PAST_TIME_PROMPT = "Distance into past (no more than): "

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


class DivinationPastManeuverTable(DivinationManeuverTable):
    """
    Divination (past) static maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        difficulty_bonus(self)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.major_factor = IntVar()
        self.maneuver_difficulty_options = None
        self.maneuver_difficulty_selector = None

        trace.exit()

    @staticmethod
    def get_maneuver_difficulty_options():
        """
        Return the difficulty options for this maneuver.
        """
        return time_options

    @staticmethod
    def get_default_time():
        """
        Return the default time into the past for this maneuver.
        """
        return TWO_WEEKS

    @staticmethod
    def get_time_prompt():
        """
        Return the text prompt used to request the time into the past for this
        maneuver.
        """
        return PAST_TIME_PROMPT

    @staticmethod
    def get_major_factor_text():
        """
        Return the text specifying that this is a major factor on the past.
        """
        return MAJOR_FACTOR_TEXT

    @staticmethod
    def get_maneuver_difficulty_bonus(maneuver_difficulty):
        """
        Return the bonus to this maneuver based on how far into the
        past the divination is looking.
        """
        return maneuver_difficulty_bonuses[maneuver_difficulty]

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=PAST_TIME_PROMPT)
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
            frame_utils.setup_checkbox_frame(
                parent_frame, MAJOR_FACTOR_TEXT, self.major_factor)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
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

    @staticmethod
    def major_factor_bonus(major_factor):
        """
        Determine the bonus to the maneuver based on whether this is a major
        influencing factor on the future.
        :param major_factor: Whether this is a major influencing factor.
        :return: The bonus to the maneuver.
        """
        if major_factor == 1:
            trace.flow("Major factor: +10")
            return MAJOR_FACTOR_BONUS
        else:
            trace.flow("Minor factor: -10")
            return MINOR_FACTOR_BONUS
