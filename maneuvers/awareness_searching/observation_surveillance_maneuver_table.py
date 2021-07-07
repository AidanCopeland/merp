# -*- coding: utf-8 -*-
"""
The Observation/Surveillance static maneuver table.

Classes:
    ObservationSurveillanceManeuverTable
"""
import sys
from tkinter import StringVar, IntVar

from maneuvers.awareness_perceptions_maneuver_table import AwarenessPerceptionsManeuverTable
from maneuvers.subterfuge_stealth.hide_maneuver_table import HideManeuverTable
from maneuvers.subterfuge_stealth.stalk_maneuver_table import StalkManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')

OBSERVATION_SURVEILLANCE_TYPE_PROMPT = \
    "Observation/surveillance for a hiding or stalking opponent?"
OBSERVATION_SURVEILLANCE_NONE_TEXT = "No"
OBSERVATION_SURVEILLANCE_HIDE_TEXT = "Hiding"
OBSERVATION_SURVEILLANCE_STALK_TEXT = "Stalking"

OBSERVATION_SURVEILLANCE_DEFAULT = OBSERVATION_SURVEILLANCE_NONE_TEXT
OBSERVATION_SURVEILLANCE_OPTIONS = (
    OBSERVATION_SURVEILLANCE_NONE_TEXT, OBSERVATION_SURVEILLANCE_HIDE_TEXT,
    OBSERVATION_SURVEILLANCE_STALK_TEXT
)

OPPONENT_BONUS_TEXT = "Opponent's Stalk/Hide bonus:"


class ObservationSurveillanceManeuverTable(AwarenessPerceptionsManeuverTable):
    """
    Observation/Surveillance static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        observation_surveillance_type_update_callback(self, *_args)
        redraw_maneuver_skill_frames(self, surveillance_type)
        skill_type_bonus(self)
    """

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.skill_frames_parent_frame = None
        self.observation_surveillance_type = StringVar()
        self.observation_surveillance_type.set(OBSERVATION_SURVEILLANCE_NONE_TEXT)
        self.current_observation_surveillance_type = OBSERVATION_SURVEILLANCE_NONE_TEXT
        self.opponent_bonus = IntVar()
        self.opponent_hide_maneuver = HideManeuverTable()
        self.opponent_stalk_maneuver = StalkManeuverTable()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        trace.entry()

        self.skill_frames_parent_frame = parent_frame
        self.opponent_bonus.set(0)

        self.opponent_hide_maneuver.init_hiding_modifiers()

        self.opponent_stalk_maneuver.init_stalking_modifiers()

        self.redraw_maneuver_skill_frames(self.observation_surveillance_type.get())
        self.observation_surveillance_type.trace(
            "w", self.observation_surveillance_type_update_callback)

        trace.exit()

    def observation_surveillance_type_update_callback(self, *_args):
        """
        Callback when the type of observation or surveillance has changed.
        """
        trace.entry()

        self.setup_maneuver_skill_frames(self.skill_frames_parent_frame)

        trace.exit()

    def redraw_maneuver_skill_frames(self, surveillance_type):
        """
        Redraw the frames specific to the skill.
        """
        trace.entry()

        parent_frame = self.skill_frames_parent_frame
        frame_utils.destroy_frame_objects(parent_frame)

        def setup_observation_surveillance_type_frame():
            """
            Create a frame with an OptionMenu specifying whether the Observation or Surveillance
            is against an opponent Stalking or Hiding.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(
                parent_frame,
                OBSERVATION_SURVEILLANCE_TYPE_PROMPT,
                surveillance_type,
                self.observation_surveillance_type,
                *OBSERVATION_SURVEILLANCE_OPTIONS)
            trace.exit()

        def setup_stalk_hide_bonus_frame():
            """
            Create a frame with an Entry containing the Stalk/Hide bonus of the
            opponent.
            """
            trace.entry()
            frame_utils.setup_entry_frame(
                parent_frame,
                OPPONENT_BONUS_TEXT,
                self.opponent_bonus
            )
            trace.exit()

        setup_observation_surveillance_type_frame()
        trace.detail("Observation/Surveillance type %s" % surveillance_type)
        if surveillance_type == OBSERVATION_SURVEILLANCE_HIDE_TEXT:
            trace.flow("Add opponent hiding frames")
            self.opponent_hide_maneuver.redraw_hiding_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()
        elif surveillance_type == OBSERVATION_SURVEILLANCE_STALK_TEXT:
            trace.flow("Add opponent stalking frames")
            self.opponent_stalk_maneuver.redraw_stalking_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        trace.flow("Add active surveillance bonus")
        bonus += 20

        if self.observation_surveillance_type.get() == OBSERVATION_SURVEILLANCE_HIDE_TEXT:
            trace.flow("Add modifiers for opponent hiding")
            bonus += 50
            bonus -= self.opponent_hide_maneuver.hiding_modifier_bonus()

            trace.detail("Opponent hiding bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        elif self.observation_surveillance_type.get() == OBSERVATION_SURVEILLANCE_STALK_TEXT:
            trace.flow("Add modifiers for opponent stalking")
            bonus += 50
            bonus -= self.opponent_stalk_maneuver.stalking_modifier_bonus()

            trace.detail("Opponent stalking bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
