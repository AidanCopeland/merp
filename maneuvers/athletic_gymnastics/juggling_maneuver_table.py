# -*- coding: utf-8 -*-
"""
The Juggling static maneuver table.

Classes:
    JugglingManeuverTable
"""
import sys
from tkinter import IntVar

from maneuvers.athletic_gymnastic_maneuver_table import AthleticGymnasticsManeuverTable
from maneuvers.static_maneuver_table import \
    maneuver_difficulty_bonuses, ROUTINE, EASY, LIGHT, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD,\
    SHEER_FOLLY, ABSURD

import frame_utils
from verify_utils import verify_int_value
import trace_log as trace

sys.path.append('../')

NUM_OBJECTS_PROMPT = "Number of objects juggled"
IRREGULAR_PROMPT = "Irregularly shaped objects?"
SHARP_PROMPT = "Sharp objects?"
DIFFERENT_PROMPT = "Different objects?"
WEIGHT_PROMPT = "Individual objects' weight (lb)?"

IRREGULAR_PENALTY = 10
SHARP_PENALTY = 20
DIFFERENT_PENALTY = 30
WEIGHT_PENALTY = 5


class JugglingManeuverTable(AthleticGymnasticsManeuverTable):
    """
    Juggling static maneuver table.

    Methods:
        setup_difficulty_frame(parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.num_objects = IntVar()
        self.is_irregular = IntVar()
        self.is_sharp = IntVar()
        self.is_different = IntVar()
        self.weight = IntVar()

        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_num_objects_frame():
            """
            Create a frame with an Entry specifying the number of objects
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, NUM_OBJECTS_PROMPT, self.num_objects)
            trace.exit()

        def setup_irregular_frame():
            """
            Create a frame with a Checkbox indicating whether the objects are irregular
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, IRREGULAR_PROMPT, self.is_irregular)
            trace.exit()

        def setup_sharp_frame():
            """
            Create a frame with a Checkbox indicating whether the objects are sharp
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, SHARP_PROMPT, self.is_sharp)
            trace.exit()

        def setup_different_frame():
            """
            Create a frame with a Checkbox indicating whether the objects are different
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, DIFFERENT_PROMPT, self.is_different)
            trace.exit()

        def setup_weight_frame():
            """
            Create a frame with an Entry specifying the weight of the objects
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, WEIGHT_PROMPT, self.weight)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.num_objects.set(2)
        setup_num_objects_frame()
        setup_irregular_frame()
        setup_sharp_frame()
        setup_different_frame()
        setup_weight_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        verify_int_value(self.num_objects, 2, minimum=1)

        bonus = 0

        def num_objects_bonus():
            """
            Determine the bonus to apply based on the number of objects.
            :return: The bonus to apply.
            """
            # pylint: disable=too-many-return-statements
            trace.entry()
            num_objects = self.num_objects.get()
            if num_objects <= 2:
                return maneuver_difficulty_bonuses[ROUTINE]
            elif num_objects == 3:
                return maneuver_difficulty_bonuses[EASY]
            elif num_objects == 4:
                return maneuver_difficulty_bonuses[LIGHT]
            elif num_objects == 5:
                return maneuver_difficulty_bonuses[MEDIUM]
            elif num_objects == 6:
                return maneuver_difficulty_bonuses[HARD]
            elif num_objects == 7:
                return maneuver_difficulty_bonuses[VERY_HARD]
            elif num_objects == 8:
                return maneuver_difficulty_bonuses[EXTREMELY_HARD]
            elif num_objects == 9:
                return maneuver_difficulty_bonuses[SHEER_FOLLY]
            else:
                return maneuver_difficulty_bonuses[ABSURD]

        bonus += num_objects_bonus()
        if self.is_irregular.get() == 1:
            trace.flow("Irregular objects")
            bonus -= IRREGULAR_PENALTY

        if self.is_sharp.get() == 1:
            trace.flow("Sharp objects")
            bonus -= SHARP_PENALTY

        if self.is_different.get() == 1:
            trace.flow("Different objects")
            bonus -= DIFFERENT_PENALTY

        weight = self.weight.get()
        trace.detail("Weight %d" % weight)
        bonus -= (weight - 1) * WEIGHT_PENALTY

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
