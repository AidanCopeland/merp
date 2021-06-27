# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.SelfControlManeuverTable import SelfControlManeuverTable
from tkinter.ttk import Frame, Label, OptionMenu

import FrameUtils
import trace_log as trace

from tkinter import LEFT, RIGHT, BOTH, RAISED, IntVar
standard_library.install_aliases()

sys.path.append('../')


TIME_PROMPT = "Difficulty of meditation: "

ROUTINE = "Calm and sedate settings, etc. (routine)"
EASY = "Easy"
LIGHT = "Light"
MEDIUM = "Medium"
HARD = "Hard"
VERY_HARD = "Very Hard"
EXTREMELY_HARD = "Extremely Hard"
SHEER_FOLLY = "Sheer Folly"
ABSURD = "Ongoing battle and melee combat, etc. (absurd)"

DIFFICULTY_DEFAULT = MEDIUM

maneuver_difficulty_options = (
    ROUTINE, EASY, LIGHT, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD)

maneuver_difficulty_bonuses = {
    ROUTINE: 30,
    EASY: 20,
    LIGHT: 10,
    MEDIUM: 0,
    HARD: -10,
    VERY_HARD: -20,
    EXTREMELY_HARD: -30,
    SHEER_FOLLY: -50,
    ABSURD: -70
}

ELF_TEXT = "Is character an elf?"
ELF_BONUS = 25


class MeditationManeuverTable(SelfControlManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(SelfControlManeuverTable, self).__init__(**kwargs)
        self.maneuver_difficulty_options = None
        self.maneuver_difficulty_selector = None
        self.is_elf = IntVar()

        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=TIME_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = maneuver_difficulty_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                MEDIUM,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_is_elf_frame():
            """
            Create a frame with a Checkbox indicating whether the character is an elf.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, ELF_TEXT, self.is_elf)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        setup_is_elf_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        if self.is_elf.get() == 1:
            trace.flow("Elf: +25")
            return ELF_BONUS
        else:
            return 0
