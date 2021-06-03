# -*- coding: utf-8 -*-
import sys

from Maneuvers.AwarenessPerceptionsManeuverTable import AwarenessPerceptionsManeuverTable
from Maneuvers.SubterfugeStealth.HideManeuverTable import HideManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

sys.path.append('../')

AMBUSH_TEXT = "Bonus/penalty based on efficacy of ambush: +30 to -70"
CONTESTED_TEXT = "Roll against opponent's Hiding bonus?"
OPPONENT_BONUS_TEXT = "Opponent's Stalk/Hide bonus:"

class SenseAmbushManeuverTable(AwarenessPerceptionsManeuverTable):

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        trace.entry()

        self.skill_frames_parent_frame = parent_frame
        self.efficacy_bonus = IntVar()
        self.contested = IntVar()
        self.contested.set(0)
        self.opponent_bonus = IntVar()
        self.opponent_bonus.set(0)

        self.opponent_hide_maneuver = HideManeuverTable()
        self.opponent_hide_maneuver.init_hiding_modifiers()

        self.redraw_maneuver_skill_frames()

        trace.exit()

    def redraw_maneuver_skill_frames(self):
        """
        Redraw the frames specific to the skill.
        """
        def setup_ambush_efficacy_frame():
            """
            Create a frame with an Entry specifying the efficacy of the ambush
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, AMBUSH_TEXT, self.efficacy_bonus)
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

        def setup_contested_frame():
            """
            Create a frame with a Checkbox indicating whether the searcher's Perception
            bonus should be used against the Hide skill.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(
                parent_frame, CONTESTED_TEXT, self.contested
            )
            self.contested.trace("w",self.skill_frames_update_callback)

        trace.entry()
        parent_frame = self.skill_frames_parent_frame
        FrameUtils.destroy_frame_objects(parent_frame)

        setup_ambush_efficacy_frame()
        setup_contested_frame()

        if self.contested.get() == 1:
            trace.flow("Add frames for opponent bonuses")
            self.opponent_hide_maneuver.redraw_hiding_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()

        trace.exit()

    def skill_frames_update_callback(self, *args):

        trace.entry()

        self.redraw_maneuver_skill_frames()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.efficacy_bonus.get():
            trace.flow("Set efficacy bonus")
            bonus += self.efficacy_bonus.get()

        if self.contested.get() == 1:
            trace.flow("Add modifiers for opponent hiding")
            bonus += 50
            bonus -= self.opponent_hide_maneuver.hiding_modifier_bonus()

            trace.detail("Opponent hiding bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
