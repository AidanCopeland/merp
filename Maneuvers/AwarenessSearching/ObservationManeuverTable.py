# -*- coding: utf-8 -*-
import sys

from Maneuvers.AwarenessPerceptionsManeuverTable import AwarenessPerceptionsManeuverTable
from Maneuvers.SubterfugeStealth.HideManeuverTable import HideManeuverTable
from Maneuvers.SubterfugeStealth.StalkManeuverTable import StalkManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import StringVar, IntVar

sys.path.append('../')

OBSERVATION_TYPE_PROMPT = "Observation for a hiding or stalking opponent?"
OBSERVATION_NONE_TEXT = "No"
OBSERVATION_HIDE_TEXT = "Hiding"
OBSERVATION_STALK_TEXT = "Stalking"

OBSERVATION_DEFAULT = OBSERVATION_NONE_TEXT
OBSERVATION_OPTIONS = (
    OBSERVATION_NONE_TEXT, OBSERVATION_HIDE_TEXT, OBSERVATION_STALK_TEXT
)

OPPONENT_BONUS_TEXT = "Opponent's Stalk/Hide bonus:"


class ObservationManeuverTable(AwarenessPerceptionsManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        trace.entry()

        self.skill_frames_parent_frame = parent_frame
        self.observation_type = StringVar()
        self.observation_type.set(OBSERVATION_NONE_TEXT)
        self.opponent_bonus = IntVar()
        self.opponent_bonus.set(0)

        self.opponent_hide_maneuver = HideManeuverTable()
        self.opponent_hide_maneuver.init_hiding_modifiers()

        self.opponent_stalk_maneuver = StalkManeuverTable()
        self.opponent_stalk_maneuver.init_stalking_modifiers()

        self.redraw_maneuver_skill_frames(self.observation_type.get())
        self.observation_type.trace("w", self.observation_type_update_callback)

        trace.exit()

    def observation_type_update_callback(self, *args):
        """
        Callback when the type of observation has changed.
        """
        trace.entry()

        self.redraw_maneuver_skill_frames(self.observation_type.get())

        trace.exit()

    def redraw_maneuver_skill_frames(self, observation_type):
        """
        Redraw the frames specific to the skill.
        """
        parent_frame = self.skill_frames_parent_frame
        FrameUtils.destroy_frame_objects(parent_frame)

        def setup_observation_type_frame():
            """
            Create a frame with an OptionMenu specifying whether the Observation is
            against an opponent Stalking or Hiding.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame,
                OBSERVATION_TYPE_PROMPT,
                observation_type,
                self.observation_type,
                *OBSERVATION_OPTIONS)
            trace.exit()

        def setup_stalk_hide_bonus_frame():
            """
            Create a frame with an Entry containing the Stalk/Hide bonus of the
            opponent.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(
                parent_frame,
                OPPONENT_BONUS_TEXT,
                self.opponent_bonus
            )

        trace.entry()

        setup_observation_type_frame()
        trace.detail("Observation type %s" % self.observation_type.get())
        if self.observation_type.get() == OBSERVATION_HIDE_TEXT:
            trace.flow("Add opponent hiding frames")
            self.opponent_hide_maneuver.redraw_hiding_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()
        elif self.observation_type.get() == OBSERVATION_STALK_TEXT:
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
        
        if self.observation_type.get() == OBSERVATION_HIDE_TEXT:
            trace.flow("Add modifiers for opponent hiding")
            bonus += 50
            bonus -= self.opponent_hide_maneuver.hiding_modifier_bonus()

            trace.detail("Opponent hiding bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        elif self.observation_type.get() == OBSERVATION_STALK_TEXT:
            trace.flow("Add modifiers for opponent stalking")
            bonus += 50
            bonus -= self.opponent_stalk_maneuver.stalking_modifier_bonus()

            trace.detail("Opponent stalking bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
