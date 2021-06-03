# -*- coding: utf-8 -*-
import sys

from Maneuvers.AwarenessPerceptionsManeuverTable import AwarenessPerceptionsManeuverTable
from Maneuvers.SubterfugeStealth.HideManeuverTable import HideManeuverTable
from Maneuvers.SubterfugeStealth.StalkManeuverTable import StalkManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import StringVar, IntVar

sys.path.append('../')

SURVEILLANCE_TYPE_PROMPT = "Surveillance for a hiding or stalking opponent?"
SURVEILLANCE_NONE_TEXT = "No"
SURVEILLANCE_HIDE_TEXT = "Hiding"
SURVEILLANCE_STALK_TEXT = "Stalking"

SURVEILLANCE_DEFAULT = SURVEILLANCE_NONE_TEXT
SURVEILLANCE_OPTIONS = (
    SURVEILLANCE_NONE_TEXT, SURVEILLANCE_HIDE_TEXT, SURVEILLANCE_STALK_TEXT
)

OPPONENT_BONUS_TEXT = "Opponent's Stalk/Hide bonus:"


class SurveillanceManeuverTable(AwarenessPerceptionsManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        trace.entry()

        self.skill_frames_parent_frame = parent_frame
        self.surveillance_type = StringVar()
        self.surveillance_type.set(SURVEILLANCE_NONE_TEXT)
        self.opponent_bonus = IntVar()
        self.opponent_bonus.set(0)

        self.opponent_hide_maneuver = HideManeuverTable()
        self.opponent_hide_maneuver.init_hiding_modifiers()

        self.opponent_stalk_maneuver = StalkManeuverTable()
        self.opponent_stalk_maneuver.init_stalking_modifiers()

        self.redraw_maneuver_skill_frames(self.surveillance_type.get())
        self.surveillance_type.trace("w", self.surveillance_type_update_callback)

        trace.exit()

    def surveillance_type_update_callback(self, *args):
        """
        Callback when the type of surveillance has changed.
        """
        trace.entry()

        self.redraw_maneuver_skill_frames(self.surveillance_type.get())

        trace.exit()

    def redraw_maneuver_skill_frames(self, surveillance_type):
        """
        Redraw the frames specific to the skill.
        """
        parent_frame = self.skill_frames_parent_frame
        FrameUtils.destroy_frame_objects(parent_frame)

        def setup_surveillance_type_frame():
            """
            Create a frame with an OptionMenu specifying whether the Surveillance is
            against an opponent Stalking or Hiding.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame,
                SURVEILLANCE_TYPE_PROMPT,
                surveillance_type,
                self.surveillance_type,
                *SURVEILLANCE_OPTIONS)
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

        setup_surveillance_type_frame()
        trace.detail("Surveillance type %s" % self.surveillance_type.get())
        if self.surveillance_type.get() == SURVEILLANCE_HIDE_TEXT:
            trace.flow("Add opponent hiding frames")
            self.opponent_hide_maneuver.redraw_hiding_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()
        elif self.surveillance_type.get() == SURVEILLANCE_STALK_TEXT:
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

        if self.surveillance_type.get() == SURVEILLANCE_HIDE_TEXT:
            trace.flow("Add modifiers for opponent hiding")
            bonus += 50
            bonus -= self.opponent_hide_maneuver.hiding_modifier_bonus()

            trace.detail("Opponent hiding bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        elif self.surveillance_type.get() == SURVEILLANCE_STALK_TEXT:
            trace.flow("Add modifiers for opponent stalking")
            bonus += 50
            bonus -= self.opponent_stalk_maneuver.stalking_modifier_bonus()

            trace.detail("Opponent stalking bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
