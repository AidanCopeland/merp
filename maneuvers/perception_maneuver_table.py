# -*- coding: utf-8 -*-
"""
The Perception static maneuver table.

Classes:
    PerceptionManeuverTable
"""
from __future__ import absolute_import
import sys
from tkinter import IntVar, StringVar, Frame

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from maneuvers.subterfuge_stealth.hide_maneuver_table import HideManeuverTable
from maneuvers.subterfuge_stealth.stalk_maneuver_table import StalkManeuverTable
from console.character.secondary_skills import \
    SKILL_PERCEPTION, SKILL_OBSERVATION, SKILL_SITUATIONAL_AWARENESS
from console.character.subterfuge_skills import \
    SKILL_SURVEILLANCE, SKILL_LIE_PERCEPTION, SKILL_POISON_PERCEPTION
from console.character.general_skills import SKILL_TRACK, SKILL_READING_TRACKS

import frame_utils
import trace_log as trace

sys.path.append('../')

SEARCHING_TEXT = "Is character spending time looking for specific information?"

SEARCHING_BONUS = 20

PERCEPTION_TYPE_PROMPT = "Perception for a hiding or stalking opponent?"
PERCEPTION_NONE_TEXT = "No"
PERCEPTION_HIDE_TEXT = "Hiding"
PERCEPTION_STALK_TEXT = "Stalking"
PERCEPTION_DEFAULT = PERCEPTION_NONE_TEXT
PERCEPTION_OPTIONS = (
    PERCEPTION_NONE_TEXT, PERCEPTION_HIDE_TEXT, PERCEPTION_STALK_TEXT
)

OPPONENT_BONUS_TEXT = "Opponent's Stalk/Hide bonus:"


class PerceptionManeuverTable(StaticManeuverTable):
    """
    Perception static maneuver table.

    Methods:
        setup_maneuver_table_frames(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        perception_type_update_callback(self, *_args)
        redraw_maneuver_skill_frames(self, perception_type)
        table_bonus(self)
        skill_type_bonus(self)
    """
    maneuver_result_text = {
        BLUNDER:
            "You not only fail to get any valid information but you pick up invalid information "
            "due to a misconception or improperly sensed details.  "
            "You may never try again on the same topic in the same area.",
        ABSOLUTE_FAILURE:
            "Confusion causes a mental lapse.  "
            "This perception roll and any perception rolls made during the next 10 minutes will "
            "result in failure.",
        FAILURE:
            "You gain no information, but you think that you have learned everything available. "
            "You may not try again on the same topic in the same area for 1 day.",
        PARTIAL_SUCCESS:
            "You gain some of the information on the topic that required the perception roll, but "
            "you are not aware that you missed something.  "
            "You may not try again on the same topic in the same area for 1 hour.",
        NEAR_SUCCESS:
            "You gain some of the information on the topic that required the perception roll, and "
            "you are aware that you missed something. "
            "Think about it for 3 rounds, and you may try again.",
        SUCCESS:
            "You gain all of the information on the topic that required the perception roll.",
        ABSOLUTE_SUCCESS:
            "You are aware of everything in the area that you are examining.  "
            "This includes information on topics other than the one requiring the perception roll."
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.is_searching = IntVar()
        self.skill_frames_parent_frame = Frame()
        self.perception_type = StringVar()
        self.opponent_bonus = IntVar()
        self.opponent_hide_maneuver = HideManeuverTable()
        self.opponent_stalk_maneuver = StalkManeuverTable()

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_searching_frame():
            """
            Create a frame with a Checkbox indicating whether the character is searching for the
            information
            """
            trace.entry()

            frame_utils.setup_checkbox_frame(parent_frame, SEARCHING_TEXT, self.is_searching)

            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_searching_frame()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up frames specific to the skill.
        """
        trace.entry()

        self.skill_frames_parent_frame = parent_frame
        self.perception_type.set(PERCEPTION_NONE_TEXT)
        self.opponent_bonus.set(0)

        self.opponent_hide_maneuver.init_hiding_modifiers()

        self.opponent_stalk_maneuver.init_stalking_modifiers()

        self.redraw_maneuver_skill_frames(self.perception_type.get())
        self.perception_type.trace("w", self.perception_type_update_callback)

        trace.exit()

    def perception_type_update_callback(self, *_args):
        """
        Callback when the type of perception has changed.
        """
        trace.entry()

        self.redraw_maneuver_skill_frames(self.perception_type.get())

        trace.exit()

    def redraw_maneuver_skill_frames(self, perception_type):
        """
        Redraw the frames specific to the skill.
        """
        parent_frame = self.skill_frames_parent_frame
        frame_utils.destroy_frame_objects(parent_frame)

        def setup_perception_type_frame():
            """
            Create a frame with an OptionMenu specifying whether the Perception is
            against an opponent Stalking or Hiding.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(
                parent_frame,
                PERCEPTION_TYPE_PROMPT,
                perception_type,
                self.perception_type,
                *PERCEPTION_OPTIONS)
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

        trace.entry()

        setup_perception_type_frame()
        if self.perception_type.get() == PERCEPTION_HIDE_TEXT:
            trace.flow("Add opponent hiding frames")
            self.opponent_hide_maneuver.redraw_hiding_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()
        elif self.perception_type.get() == PERCEPTION_STALK_TEXT:
            trace.flow("Add opponent stalking frames")
            self.opponent_stalk_maneuver.redraw_stalking_modifier_frames(parent_frame)
            setup_stalk_hide_bonus_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.is_searching.get() == 1:
            trace.flow("Character is searching: +20")
            bonus += SEARCHING_BONUS

        trace.detail("Bonus %d" % bonus)

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

        if self.perception_type.get() == PERCEPTION_HIDE_TEXT:
            trace.flow("Add modifiers for opponent hiding")
            bonus += 50
            bonus -= self.opponent_hide_maneuver.hiding_modifier_bonus()

            trace.detail("Opponent hiding bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        elif self.perception_type.get() == PERCEPTION_STALK_TEXT:
            trace.flow("Add modifiers for opponent stalking")
            bonus += 50
            bonus -= self.opponent_stalk_maneuver.stalking_modifier_bonus()

            trace.detail("Opponent stalking bonus %d" % self.opponent_bonus.get())
            bonus -= self.opponent_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def get_maneuver_preferred_skills(_):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param _: The type of maneuver selected.
        """
        return [
            SKILL_PERCEPTION,
            SKILL_TRACK,
            SKILL_OBSERVATION,
            SKILL_SITUATIONAL_AWARENESS,
            SKILL_SURVEILLANCE,
            SKILL_LIE_PERCEPTION,
            SKILL_POISON_PERCEPTION,
            SKILL_READING_TRACKS
        ]
