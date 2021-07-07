# -*- coding: utf-8 -*-
"""
The Divination (future) static maneuver table.

Classes:
    DivinationFutureManeuverTable
"""
import sys

from maneuvers.power_awareness.divination_maneuver_table import DivinationManeuverTable

import trace_log as trace

sys.path.append('../')


FUTURE_TIME_PROMPT = "Distance into future (no more than): "

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


class DivinationFutureManeuverTable(DivinationManeuverTable):
    """
    Divination (future) static maneuver table.

    Methods:
        get_maneuver_difficulty_options()
        get_default_time()
        get_time_prompt()
        get_major_factor_text()
        get_maneuver_difficulty_bonus(maneuver_difficulty)
    """

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)

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
        Return the default time into the future for this maneuver.
        """
        return SIX_HOURS

    @staticmethod
    def get_time_prompt():
        """
        Return the text prompt used to request the time into the future for this
        maneuver.
        """
        return FUTURE_TIME_PROMPT

    @staticmethod
    def get_major_factor_text():
        """
        Return the text specifying that this is a major factor on the future.
        """
        return MAJOR_FACTOR_TEXT

    @staticmethod
    def get_maneuver_difficulty_bonus(maneuver_difficulty):
        """
        Return the bonus to this maneuver based on how far into the
        future the divination is looking.
        """
        return maneuver_difficulty_bonuses[maneuver_difficulty]

    @staticmethod
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
