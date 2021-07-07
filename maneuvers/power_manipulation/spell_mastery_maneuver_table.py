# -*- coding: utf-8 -*-
"""
The Spell Mastery static maneuver table.

Classes:
    SpellMasteryManeuverTable
"""
import sys
from tkinter import IntVar, StringVar

from maneuvers.power_manipulation_maneuver_table import PowerManipulationManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')


CASTER_TO_TARGET_TEXT = "Range increase: caster/self to target/touch"
CASTER_TO_TARGET_BONUS = -30

TOUCH_TO_TEN_FT_TEXT = "Range increase: touch to 10'"
TOUCH_TO_TEN_FT_BONUS = -30

RANGE_MULTIPLIER_TEXT = "Range multiplier:"
RANGE_MULTIPLIER_BONUS = -10

ADDITIONAL_TARGET_TEXT = "Additional targets:"
ADDITIONAL_TARGET_BONUS = -30

TARGET_TO_TEN_FT_RADIUS_TEXT = "Area of Effect increase: target to 10'R"
TARGET_TO_TEN_FT_RADIUS_BONUS = -50

AREA_OF_EFFECT_MULTIPLIER_TEXT = "Area of Effect multiplier:"
AREA_OF_EFFECT_MULTIPLIER_BONUS = -10

NO_DURATION_TO_1_RND_TEXT = "Duration increase: no duration to 1 round"
NO_DURATION_TO_1_RND_BONUS = -50

CONCENTRATION_TO_RND_PER_LVL_TEXT = "Duration increase: concentration to 1 rnd/lvl (c)"
CONCENTRATION_TO_RND_PER_LVL_BONUS = -20

CONCENTRATION_TO_MIN_PER_LVL_TEXT = "Duration increase: concentration to 1 min/lvl (c)"
CONCENTRATION_TO_MIN_PER_LVL_BONUS = -50

DURATION_MULTIPLIER_TEXT = "Duration multiplier:"
DURATION_MULTIPLIER_BONUS = -10

INCREASED_POWER_PROMPT = "Increased spell power: penalty to target's RR"
INCREASED_POWER_0 = "0"
INCREASED_POWER_NEG_10 = "-10"
INCREASED_POWER_NEG_20 = "-20"
INCREASED_POWER_NEG_30 = "-30"
INCREASED_POWER_NEG_40 = "-40"
INCREASED_POWER_OPTIONS = (
    INCREASED_POWER_NEG_10, INCREASED_POWER_NEG_20, INCREASED_POWER_NEG_30,
    INCREASED_POWER_NEG_40
)


class SpellMasteryManeuverTable(PowerManipulationManeuverTable):
    """
    Spell Mastery static maneuver table.

    Methods:
        setup_difficulty_frame(parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
        range_bonus(self)
        area_of_effect_bonus(self)
        duration_bonus(self)
        increased_power_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.caster_to_target = IntVar()
        self.touch_to_10_foot = IntVar()
        self.range_multiplier = IntVar()
        self.additional_targets = IntVar()
        self.target_to_10_foot = IntVar()
        self.area_of_effect_multiplier = IntVar()
        self.no_duration_to_1_rnd = IntVar()
        self.concentration_to_rnd_per_lvl = IntVar()
        self.concentration_to_min_per_lvl = IntVar()
        self.duration_multiplier = IntVar()
        self.increased_power = StringVar()

        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        self.__setup_caster_touch_frame(parent_frame)
        self.__setup_touch_10_foot_frame(parent_frame)
        self.__setup_range_multiplier_frame(parent_frame)
        self.range_multiplier.set(1)

        self.__setup_additional_target_frame(parent_frame)
        self.__setup_target_10_foot_frame(parent_frame)
        self.__setup_aoe_multiplier_frame(parent_frame)
        self.additional_targets.set(0)
        self.area_of_effect_multiplier.set(1)

        self.__setup_no_duration_to_1_rnd_frame(parent_frame)
        self.__setup_concentration_to_rnd_per_level_frame(parent_frame)
        self.__setup_concentration_to_min_per_level_frame(parent_frame)
        self.__setup_duration_multiplier_frame(parent_frame)
        self.duration_multiplier.set(1)
        self.__setup_increased_power_frame(parent_frame)

        trace.exit()

    def __setup_caster_touch_frame(self, parent_frame):
        """
        Create a frame with a Checkbox indicating whether the range is increased
        from caster to touch.
        """
        trace.entry()
        frame_utils.setup_checkbox_frame(parent_frame,
                                         CASTER_TO_TARGET_TEXT,
                                         self.caster_to_target)
        trace.exit()

    def __setup_touch_10_foot_frame(self, parent_frame):
        """
        Create a frame with a Checkbox indicating whether the range is increased
        from touch to 10'.
        """
        trace.entry()
        frame_utils.setup_checkbox_frame(parent_frame,
                                         TOUCH_TO_TEN_FT_TEXT,
                                         self.touch_to_10_foot)
        trace.exit()

    def __setup_range_multiplier_frame(self, parent_frame):
        """
        Create a frame with an Entry indicating the range multiplier.
        """
        trace.entry()
        frame_utils.setup_entry_frame(parent_frame, RANGE_MULTIPLIER_TEXT, self.range_multiplier)
        trace.exit()

    def __setup_additional_target_frame(self, parent_frame):
        """
        Create a frame with an Entry indicating the number of additional targets.
        """
        trace.entry()
        frame_utils.setup_entry_frame(parent_frame,
                                      ADDITIONAL_TARGET_TEXT,
                                      self.additional_targets)
        trace.exit()

    def __setup_target_10_foot_frame(self, parent_frame):
        """
        Create a frame with a Checkbox indicating whether the area of effect is increased
        from a single target to 10'R.
        """
        trace.entry()
        frame_utils.setup_checkbox_frame(parent_frame,
                                         TARGET_TO_TEN_FT_RADIUS_TEXT,
                                         self.target_to_10_foot)
        trace.exit()

    def __setup_aoe_multiplier_frame(self, parent_frame):
        """
        Create a frame with an Entry indicating the area of effect multiplier.
        """
        trace.entry()
        frame_utils.setup_entry_frame(parent_frame,
                                      AREA_OF_EFFECT_MULTIPLIER_TEXT,
                                      self.area_of_effect_multiplier)
        trace.exit()

    def __setup_no_duration_to_1_rnd_frame(self, parent_frame):
        """
        Create a frame with a Checkbox indicating whether the duration is increased
        from no duration to 1 round.
        """
        trace.entry()
        frame_utils.setup_checkbox_frame(parent_frame,
                                         NO_DURATION_TO_1_RND_TEXT,
                                         self.no_duration_to_1_rnd)
        trace.exit()

    def __setup_concentration_to_rnd_per_level_frame(self, parent_frame):
        """
        Create a frame with a Checkbox indicating whether the duration is increased
        from concentration to 1 round per level.
        """
        trace.entry()
        frame_utils.setup_checkbox_frame(parent_frame,
                                         CONCENTRATION_TO_RND_PER_LVL_TEXT,
                                         self.concentration_to_rnd_per_lvl)
        trace.exit()

    def __setup_concentration_to_min_per_level_frame(self, parent_frame):
        """
        Create a frame with a Checkbox indicating whether the duration is increased
        from concentration to 1 minute per level.
        """
        trace.entry()
        frame_utils.setup_checkbox_frame(parent_frame,
                                         CONCENTRATION_TO_MIN_PER_LVL_TEXT,
                                         self.concentration_to_min_per_lvl)
        trace.exit()

    def __setup_duration_multiplier_frame(self, parent_frame):
        """
        Create a frame with an Entry indicating the duration multiplier.
        """
        trace.entry()
        frame_utils.setup_entry_frame(parent_frame,
                                      DURATION_MULTIPLIER_TEXT,
                                      self.duration_multiplier)
        trace.exit()

    def __setup_increased_power_frame(self, parent_frame):
        """
        Create a frame with an OptionMenu indicating any additional RR penalty
        to apply to the target(s).
        """
        trace.entry()
        frame_utils.setup_optionmenu_frame(
            parent_frame,
            INCREASED_POWER_PROMPT,
            INCREASED_POWER_0,
            self.increased_power,
            *INCREASED_POWER_OPTIONS)

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += self.range_bonus()
        bonus += self.area_of_effect_bonus()
        bonus += self.duration_bonus()
        bonus += self.increased_power_bonus()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    def range_bonus(self):
        """
        Determine any additional bonuses to apply to this maneuver based on the range
        modifiers applied.
        :return: The additional maneuver bonus.
        """
        trace.entry()

        bonus = 0

        if self.caster_to_target.get() == 1:
            trace.flow("Caster/self to target/touch increase: -30")
            bonus += CASTER_TO_TARGET_BONUS

        if self.touch_to_10_foot.get() == 1:
            trace.flow("Touch to 10 foot increase: -30")
            bonus += TOUCH_TO_TEN_FT_BONUS

        if self.range_multiplier.get() > 1:
            range_bonus = RANGE_MULTIPLIER_BONUS * self.range_multiplier.get()
            trace.flow(
                "Range multiplier: %u" % range_bonus)
            bonus += (RANGE_MULTIPLIER_BONUS * self.range_multiplier.get())

        trace.exit()
        return bonus

    def area_of_effect_bonus(self):
        """
        Determine any additional bonuses to apply to this maneuver based on the area
        of effect modifiers applied.
        :return: The additional maneuver bonus.
        """
        trace.entry()

        bonus = 0

        if self.additional_targets.get() > 0:
            target_bonus = ADDITIONAL_TARGET_BONUS * self.additional_targets.get()
            trace.flow("Additional targets: %u" % target_bonus)
            return target_bonus

        if self.target_to_10_foot.get() == 1:
            trace.flow("Target to 10'R: -50")
            bonus += TARGET_TO_TEN_FT_RADIUS_BONUS

        if self.area_of_effect_multiplier.get() > 1:
            aoe_bonus = AREA_OF_EFFECT_MULTIPLIER_BONUS * self.area_of_effect_multiplier.get()
            trace.flow(
                "Area of effect multiplier: %u" % aoe_bonus)
            bonus += aoe_bonus

        trace.exit()
        return bonus

    def duration_bonus(self):
        """
        Determine any additional bonuses to apply to this maneuver based on the
        duration modifiers applied.
        :return: The additional maneuver bonus.
        """
        trace.entry()

        bonus = 0

        if self.no_duration_to_1_rnd.get() == 1:
            trace.flow("No duration to 1 round: -50, value is %r" % self.no_duration_to_1_rnd.get())
            bonus += NO_DURATION_TO_1_RND_BONUS
        elif self.concentration_to_min_per_lvl.get() == 1:
            trace.flow("Concentration to 1 min/lvl: -50")
            bonus += CONCENTRATION_TO_MIN_PER_LVL_BONUS
        elif self.concentration_to_rnd_per_lvl.get() == 1:
            trace.flow("Concentration to 1 rnd/lvl: -20")
            bonus += CONCENTRATION_TO_RND_PER_LVL_BONUS

        if self.duration_multiplier.get() > 1:
            duration_bonus = DURATION_MULTIPLIER_BONUS * self.duration_multiplier.get()
            trace.flow(
                "Duration multiplier: %u" % duration_bonus)
            bonus += duration_bonus

        trace.exit()
        return bonus

    def increased_power_bonus(self):
        """
        Determine any additional bonuses to apply to this maneuver based on
        increased power applied.
        :return: The additional maneuver bonus.
        """
        trace.entry()

        bonus = 0

        increased_power = int(self.increased_power.get())
        if increased_power != 0:
            trace.flow("RR penalty: %d" % increased_power)
            bonus = increased_power - 10

        trace.detail("Bonus %d" % bonus)

        trace.exit()

        return bonus
