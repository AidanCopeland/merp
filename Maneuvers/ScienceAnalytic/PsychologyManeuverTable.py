# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.ScienceAnalyticManeuverTable import ScienceAnalyticManeuverTable

import FrameUtils
import trace_log as trace

from tkinter import IntVar, StringVar
standard_library.install_aliases()

sys.path.append('../')


ILLNESS_LEVEL_PROMPT = "Severity of mental illness"
ILLNESS_SLIGHT_TEXT = "Slight"
ILLNESS_MODERATE_TEXT = "Moderate"
ILLNESS_SEVERE_TEXT = "Severe"
ILLNESS_OPTIONS = (
    ILLNESS_SLIGHT_TEXT, ILLNESS_MODERATE_TEXT, ILLNESS_SEVERE_TEXT
)

ILLNESS_SLIGHT_BONUS = 5
ILLNESS_MODERATE_BONUS = -5
ILLNESS_SEVERE_BONUS = -20

YEARS_TEXT = "Number of years affected"
YEARS_BONUS = -10

SEVERITY_TEXT = "Bonus caused by severity of event which caused illness (+30 to -70)"

LEVEL_TEXT = "Level of PC/NPC which caused illness"


def illness_level_bonus(illness_level):
    """
    Determine the bonus to the maneuver based on the severity of the illness.
    :param illness_level: The severity of the illness.
    :return: The bonus to the maneuver.
    """
    if illness_level == ILLNESS_SLIGHT_TEXT:
        trace.flow("Slight illness: +5")
        return ILLNESS_SLIGHT_BONUS
    elif illness_level == ILLNESS_MODERATE_TEXT:
        trace.flow("Moderate illness: -5")
        return ILLNESS_MODERATE_BONUS
    else:
        trace.flow("Severe illness: -20")
        return ILLNESS_SEVERE_BONUS


def years_affected_bonus(years_affected):
    """
    Determine the bonus to the maneuver based on the number of years affected.
    :param years_affected: The number of years affected.
    :return: The bonus to the maneuver.
    """
    trace.flow("%d years affected, bonus %d" %
               (years_affected, years_affected * YEARS_BONUS))
    return years_affected * YEARS_BONUS


class PsychologyManeuverTable(ScienceAnalyticManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(ScienceAnalyticManeuverTable, self).__init__(**kwargs)
        self.illness_level = StringVar()
        self.years_affected = IntVar()
        self.event_severity = IntVar()
        self.npc_level = IntVar()

        trace.exit()

    @staticmethod
    def setup_difficulty_frame(parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_illness_level_frame():
            """
            Create a frame with an OptionMenu specifying the severity of the illness.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, ILLNESS_LEVEL_PROMPT, ILLNESS_SLIGHT_TEXT, self.illness_level, *ILLNESS_OPTIONS)
            trace.exit()

        def setup_years_affected_frame():
            """
            Create a frame with an Entry indicating number of years affected.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, YEARS_TEXT, self.years_affected)
            trace.exit()

        def setup_event_severity_frame():
            """
            Create a frame with an Entry indicating severity of the event which caused
            the illness.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, SEVERITY_TEXT, self.event_severity)
            trace.exit()

        def setup_npc_level_frame():
            """
            Create a frame with an Entry indicating the level of the character which
            caused the illness
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, LEVEL_TEXT, self.npc_level)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        setup_illness_level_frame()
        setup_years_affected_frame()
        setup_event_severity_frame()
        setup_npc_level_frame()
        self.years_affected.set(0)
        self.event_severity.set(0)
        self.npc_level.set(0)

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += illness_level_bonus(self.illness_level.get())
        bonus += years_affected_bonus(self.years_affected.get())

        bonus += self.event_severity.get()
        trace.flow("Event severity bonus: %d" % self.event_severity.get())

        bonus -= self.npc_level.get()
        trace.flow("NPC level penalty: %d" % self.npc_level.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
