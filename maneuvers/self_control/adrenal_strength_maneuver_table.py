# -*- coding: utf-8 -*-
"""
The Adrenal Strength static maneuver table.

Classes:
    AdrenalStrengthManeuverTable
"""
from __future__ import division
from builtins import str
import sys
from tkinter import IntVar
from past.utils import old_div

from maneuvers.self_control_maneuver_table import SelfControlManeuverTable
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS


import frame_utils
import trace_log as trace

sys.path.append('../')


DESIRED_BONUS_TEXT = "Desired bonus to OB (minimum 10)"


class AdrenalStrengthManeuverTable(SelfControlManeuverTable):
    """
    Adrenal Strength static maneuver table.

    Methods:
        setup_difficulty_frame(self, parent_frame)
        setup_maneuver_skill_frames(self, parent_frame)
        difficulty_bonus(self)
        result_text(self, result)
        attack_bonus_text(result, desired_bonus)
        previous_penalty_text(desired_bonus)
        fumble_text(desired_bonus)
        cooldown_text(desired_bonus)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.desired_bonus = IntVar()

        trace.exit()

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        frame_utils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_desired_bonus_frame():
            """
            Create a frame with an Entry indicating the desired bonus above +10.
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, DESIRED_BONUS_TEXT, self.desired_bonus)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.desired_bonus.set(10)
        setup_desired_bonus_frame()

        trace.exit()

    def difficulty_bonus(self):
        """
        Determine the difficulty to apply to a maneuver based on its difficulty.
        :return: The maneuver difficulty bonus
        """
        trace.entry()

        desired_bonus = max(self.desired_bonus.get(), 10)

        bonus = -desired_bonus

        trace.detail("Returning %d" % bonus)

        trace.exit()
        return bonus

    def result_text(self, result):
        """
        Return additional text to report for the maneuver result.
        :param result: The type of result achieved.
        """
        trace.detail("Result is %s" % result)

        desired_bonus = max(self.desired_bonus.get(), 10)

        result_text = self.maneuver_result_text[result]
        attack_bonus_text = self.attack_bonus_text(result, desired_bonus)
        previous_penalty_text = self.previous_penalty_text(desired_bonus)
        fumble_text = self.fumble_text(desired_bonus)
        cooldown_text = self.cooldown_text(desired_bonus)

        return result_text + '\n' + \
               attack_bonus_text + fumble_text + previous_penalty_text + cooldown_text

    @staticmethod
    def attack_bonus_text(result, desired_bonus):
        """
        Return additional text to report the bonus achieved for the attack.
        :param result: The type of result achieved.
        :param desired_bonus: The desired bonus for the attack.
        """
        desired_hits_multiplier = 1 + (old_div(desired_bonus, 10))

        if result == PARTIAL_SUCCESS:
            trace.flow("Partial success")
            actual_bonus = desired_bonus * 0.3
            return str("\nYou attack with a bonus of %d.\n" % actual_bonus)
        elif result == NEAR_SUCCESS:
            trace.flow("Near success")
            actual_bonus = desired_bonus * 0.8
            return str("\nYou attack with a bonus of %d.\n" % actual_bonus)
        elif result == SUCCESS:
            trace.flow("SUCCESS")
            return \
                str("\nYou attack with a bonus of %d.  Concussion hits are multiplied by %d.\n" %
                    (desired_bonus, desired_hits_multiplier))
        elif result == ABSOLUTE_SUCCESS:
            trace.flow("ABSOLUTE_SUCCESS")
            actual_bonus = desired_bonus * 1.2
            return \
                str("\nYou attack with a bonus of %d.  Concussion hits are multiplied by %d.\n" %
                    (actual_bonus, desired_hits_multiplier))
        else:
            return "\n"

    @staticmethod
    def previous_penalty_text(desired_bonus):
        """
        Return additional text to report the penalty to activity required on the previous round.
        :param desired_bonus: The desired bonus for the attack.
        """
        previous_penalty = desired_bonus + 10

        return \
            str("This requires a penalty of %d to activity the previous round.\n" %
                previous_penalty)

    @staticmethod
    def fumble_text(desired_bonus):
        """
        Return additional text to report the additional fumble range applied to the weapon.
        :param desired_bonus: The desired bonus for the attack.
        """
        fumble_increase = old_div(desired_bonus, 10)

        return str("Fumble range is increased by %d.\n" % fumble_increase)

    @staticmethod
    def cooldown_text(desired_bonus):
        """
        Return additional text to report any additional cooldown required after the attack.
        :param desired_bonus: The desired bonus for the attack.
        """
        cooldown_period = old_div((desired_bonus - 1), 10)
        if cooldown_period != 0:
            return str("This requires an additional %d rounds cooldown before the maneuver can be "
                       "attempted again" % cooldown_period)
        else:
            return ""
