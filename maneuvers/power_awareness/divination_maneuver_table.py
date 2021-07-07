# -*- coding: utf-8 -*-
"""
The Divination static maneuver table.

Classes:
    DivinationManeuverTable
"""
import sys
from tkinter import LEFT, RIGHT, BOTH, RAISED, IntVar
from tkinter.ttk import Frame, Label, OptionMenu

from maneuvers.power_awareness_maneuver_table import PowerAwarenessManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS

import frame_utils
import trace_log as trace

sys.path.append('../')


class DivinationManeuverTable(PowerAwarenessManeuverTable):
    """
    Divination static maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        difficulty_bonus(self)
        skill_type_bonus(self)
    """
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
        super().__init__(**kwargs)
        self.major_factor = IntVar()
        self.maneuver_difficulty_options = self.get_maneuver_difficulty_options()
        self.maneuver_difficulty_selector = None

        trace.exit()

    @staticmethod
    def get_maneuver_difficulty_options():
        """
        Return the difficulty options for this maneuver.
        """
        return ""

    @staticmethod
    def get_default_time():
        """
        Return the default time into the past or future for this maneuver.
        """
        return ""

    @staticmethod
    def get_time_prompt():
        """
        Return the text prompt used to request the time into the past or future for this
        maneuver.
        """
        return ""

    @staticmethod
    def get_major_factor_text():
        """
        Return the text specifying that this is a major factor on the past or future.
        """
        return ""

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=self.get_time_prompt())
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                self.get_default_time(),
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
            frame_utils.setup_checkbox_frame(
                parent_frame, self.get_major_factor_text(), self.major_factor)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_major_factor_frame()

        trace.exit()

    def difficulty_bonus(self):
        """
        Determine the difficulty to apply to a maneuver based on its difficulty.
        :return: The maneuver difficulty bonus
        """
        trace.entry()

        bonus = self.get_maneuver_difficulty_bonus(self.maneuver_difficulty.get())
        trace.detail("Returning %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def get_maneuver_difficulty_bonus(_):
        """
        Return the bonus to this maneuver based on how far into the past or
        future the divination is looking.
        """
        return 0

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += self.major_factor_bonus(self.major_factor.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def major_factor_bonus(_):
        """
        Return the bonus to this maneuver depending on whether this is a major
        influencing factor on the past or future.
        """
        return 0
