# -*- coding: utf-8 -*-
"""
The Pick Locks static maneuver table.

Classes:
    PickLocksManeuverTable

Functions:
    determine_information_bonus(information)
    determine_lock_lore_bonus(lock_lore_made)
    determine_failed_attempts_bonus(num_prior_attempts)
"""
import sys
from tkinter import IntVar, StringVar

from maneuvers.subterfuge_mechanics_maneuver_table import SubterfugeMechanicsManeuverTable

import frame_utils
import trace_log as trace

sys.path.append('../')

INFORMATION_PROMPT = "Information or prior experience relevant to lock"
PICKED_BEFORE_TEXT = "Have picked lock before"
PICKED_TYPE_BEFORE_TEXT = "Have picked this type of lock before"
DESCRIPTION_TEXT = "Have description of mechanism"
NONE_TEXT = "No knowledge"

PICKED_BEFORE_BONUS = 50
PICKED_TYPE_BEFORE_BONUS = 25
DESCRIPTION_BONUS = 10
NONE_BONUS = 0
INFORMATION_OPTIONS = (
    PICKED_BEFORE_TEXT, PICKED_TYPE_BEFORE_TEXT, DESCRIPTION_TEXT, NONE_TEXT)

LOCK_LORE_TEXT = "Successful Lock Lore?"
LOCK_LORE_BONUS = 40

FAILED_TEXT = "Number of prior unsuccessful attempts?"
FAILED_BONUS = -30


def determine_information_bonus(information):
    """
    Determine the bonus to the maneuver based on the relevant information and experience.
    :param information: Information or experience relevant to the lock.
    :return: The bonus to the maneuver.
    """
    if information == PICKED_BEFORE_TEXT:
        trace.flow("Picked before: +50")
        return PICKED_BEFORE_BONUS
    elif information == PICKED_TYPE_BEFORE_TEXT:
        trace.flow("Picked type before: +25")
        return PICKED_TYPE_BEFORE_BONUS
    elif information == DESCRIPTION_TEXT:
        trace.flow("Have description: +10")
        return DESCRIPTION_BONUS
    else:
        trace.flow("No information: +0")
        return NONE_BONUS


def determine_lock_lore_bonus(lock_lore_made):
    """
    Determine the bonus to the maneuver based on whether a successful Lock Lore
    maneuver has been made.
    :param lock_lore_made: Whether a successful Lock Lore maneuver has been made.
    :return: The bonus to the maneuver.
    """
    if lock_lore_made == 1:
        trace.flow("Lock lore made: +40")
        return LOCK_LORE_BONUS
    else:
        trace.flow("No Lock Lore: +0")
        return 0


def determine_failed_attempts_bonus(num_prior_attempts):
    """
    Determine the bonus to the maneuver based on whether previous unsuccessful
    attempts have been made.
    :param num_prior_attempts: The number of unsuccessful prior attempts that have
    been made.
    :return: The bonus to the maneuver.
    """
    trace.flow("%d prior attempts: %d bonus" %
               (num_prior_attempts, num_prior_attempts * FAILED_BONUS))
    return num_prior_attempts * FAILED_BONUS


class PickLocksManeuverTable(SubterfugeMechanicsManeuverTable):
    """
    Pick Locks static maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.lock_lore = IntVar()
        self.failed_attempts = IntVar()
        self.information = StringVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_lock_lore_frame():
            """
            Create a frame with a Checkbox indicating whether a successful Lock Lore
            maneuver has been made
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, LOCK_LORE_TEXT, self.lock_lore)
            trace.exit()

        def setup_failed_attempts_frame():
            """
            Create a frame with an Entry indicating the number of unsuccessful attempts
            that have been made.
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, FAILED_TEXT, self.failed_attempts)
            trace.exit()

        def setup_information_frame():
            """
            Create a frame with an OptionMenu specifying the relevant information available.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(
                parent_frame, INFORMATION_PROMPT, NONE_TEXT, self.information, *INFORMATION_OPTIONS)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        setup_lock_lore_frame()
        setup_failed_attempts_frame()
        setup_information_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += determine_lock_lore_bonus(self.lock_lore.get())
        bonus += determine_failed_attempts_bonus(self.failed_attempts.get())
        bonus += determine_information_bonus(self.information.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
