# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.SelfControlManeuverTable import SelfControlManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

MOON_PHASE_PROMPT = "Phase of moon"
FULL_MOON_TEXT = "Full moon"
HALF_MOON_TEXT = "Half moon"
NEW_MOON_TEXT = "New moon"
FULL_MOON_BONUS = -100
HALF_MOON_BONUS = -50
NEW_MOON_BONUS = 0
MOON_PHASE_OPTIONS = (FULL_MOON_TEXT, HALF_MOON_TEXT, NEW_MOON_TEXT)

DAY_NIGHT_PROMPT = "State of day"
NIGHT_TEXT = "Night"
DAYBREAK_TEXT = "Daybreak"
DAYLIGHT_OUTDOORS_TEXT = "Daylight outdoors"
DAYLIGHT_UNDERGROUND_TEXT = "Daylight indoors or underground"
NIGHT_BONUS = 0
DAYBREAK_BONUS = 100
DAYLIGHT_OUTDOORS_BONUS = 50
DAYLIGHT_UNDERGROUND_BONUS = 10
DAY_NIGHT_OPTIONS = (
    NIGHT_TEXT, DAYBREAK_TEXT, DAYLIGHT_OUTDOORS_TEXT, DAYLIGHT_UNDERGROUND_TEXT)

CHANGE_TYPE_PROMPT = "Start or stop change?"
START_TEXT = "Start change"
STOP_TEXT = "Stop change"
START_BONUS = 0
STOP_BONUS = -25
CHANGE_OPTIONS = (START_TEXT, STOP_TEXT)

DAMAGE_TEXT = "Has taken hits?"
DAMAGE_BONUS = -25

CRITICAL_TEXT = "Has taken a critical in the current combat?"
CRITICAL_BONUS = -50

FRIEND_WOUNDED_PROMPT = "Has seen a friend wounded or killed in the current combat?"
FRIEND_FINE_TEXT = "No"
FRIEND_WOUNDED_TEXT = "Wounded"
FRIEND_KILLED_TEXT = "Killed"
FRIEND_WOUNDED_BONUS = -25
FRIEND_KILLED_BONUS = -50
FRIEND_WOUNDED_OPTIONS = (FRIEND_FINE_TEXT, FRIEND_WOUNDED_TEXT, FRIEND_KILLED_TEXT)


def determine_moon_bonus(moon_phase):
    """
    Determine the bonus to the maneuver based on the phase of the moon.
    :param moon_phase: The phase of the moon.
    :return: The bonus to the maneuver.
    """
    if moon_phase == FULL_MOON_TEXT:
        trace.flow("Full moon: -100")
        return FULL_MOON_BONUS
    elif moon_phase == HALF_MOON_TEXT:
        trace.flow("Half moon: -50")
        return HALF_MOON_BONUS
    else:
        trace.flow("New moon: +0")
        return NEW_MOON_BONUS


def determine_day_night_bonus(time):
    """
    Determine the bonus to the maneuver based on the time of day.
    :param time: The time of day.
    :return: The bonus to the maneuver.
    """
    if time == NIGHT_TEXT:
        trace.flow("Night: +0")
        return NIGHT_BONUS
    elif time == DAYBREAK_TEXT:
        trace.flow("Daybreak: +100")
        return DAYBREAK_BONUS
    elif time == DAYLIGHT_OUTDOORS_TEXT:
        trace.flow("Daylight outdoors: +50")
        return DAYLIGHT_OUTDOORS_BONUS
    else:
        trace.flow("Daylight indoors or underground: +10")
        return DAYLIGHT_UNDERGROUND_BONUS


def determine_start_stop_bonus(start_stop):
    """
    Determine the bonus to the maneuver based on whether the character is starting
    or stopping the change.
    :param start_stop: Whether the character is starting or stopping the change.
    :return: The bonus to the maneuver.
    """
    if start_stop == START_TEXT:
        trace.flow("Start change: +0")
        return START_BONUS
    else:
        trace.flow("Stop change: -25")
        return STOP_BONUS


def determine_taken_damage_bonus(taken_hits, taken_critical):
    """
    Determine the bonus to the maneuver based on whether the character has taken hits
    and/or a critical.
    :param taken_hits: Whether the character has taken hits.
    :param taken_critical: Whether the character has taken a critical in this
    combat.
    :return: The bonus to the maneuver.
    """
    bonus = 0
    if taken_hits == 1:
        trace.flow("Taken hits: -25")
        bonus += DAMAGE_BONUS

    if taken_critical == 1:
        trace.flow("Taken critical: -50")
        bonus += CRITICAL_BONUS

    return bonus


def determine_friend_damage_bonus(friend_damage):
    """
    Determine the bonus to the maneuver based on whether the character has seen a
    friend wounded in this combat.
    :param friend_damage: Injury that the character has seen a friend take.
    :return: The bonus to the maneuver.
    """
    if friend_damage == FRIEND_KILLED_TEXT:
        trace.flow("Friend killed: -50")
        return FRIEND_KILLED_BONUS
    elif friend_damage == FRIEND_WOUNDED_TEXT:
        trace.flow("Friend wounded: -25")
        return FRIEND_WOUNDED_BONUS
    else:
        trace.flow("No injuries to friends")
        return 0


class ControlLycanthrophyManeuverTable(SelfControlManeuverTable):

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_moon_phase_frame():
            """
            Create a frame with an OptionMenu specifying the phase of the moon.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, MOON_PHASE_PROMPT, HALF_MOON_TEXT, self.moon_phase, *MOON_PHASE_OPTIONS)
            trace.exit()

        def setup_day_night_frame():
            """
            Create a frame with an OptionMenu specifying the time of day.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, DAY_NIGHT_PROMPT, DAYLIGHT_OUTDOORS_TEXT, self.day_night, *DAY_NIGHT_OPTIONS)
            trace.exit()

        def setup_start_stop_frame():
            """
            Create a frame with an OptionMenu specifying whether to start or stop the change.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, CHANGE_TYPE_PROMPT, START_TEXT, self.start_stop, *CHANGE_OPTIONS)
            trace.exit()

        def setup_taken_hits_frame():
            """
            Create a frame with a Checkbox indicating whether the character has taken hits
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, DAMAGE_TEXT, self.taken_damage)
            trace.exit()

        def setup_taken_critical_frame():
            """
            Create a frame with a Checkbox indicating whether the character has taken a
            critical in this combat
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, CRITICAL_TEXT, self.taken_critical)
            trace.exit()

        def setup_friend_wounded_frame():
            """
            Create a frame with an OptionMenu specifying whether the character has seen a friend
            wounded or killed in this combat.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame,
                FRIEND_WOUNDED_PROMPT,
                FRIEND_FINE_TEXT,
                self.friend_wounded,
                *FRIEND_WOUNDED_OPTIONS)
            trace.exit()


        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.moon_phase = StringVar()
        self.day_night = StringVar()
        self.start_stop = StringVar()
        self.taken_damage = IntVar()
        self.taken_critical = IntVar()
        self.friend_wounded = StringVar()
        setup_moon_phase_frame()
        setup_day_night_frame()
        setup_start_stop_frame()
        setup_taken_hits_frame()
        setup_taken_critical_frame()
        setup_friend_wounded_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += determine_moon_bonus(self.moon_phase.get())
        bonus += determine_day_night_bonus(self.day_night.get())
        bonus += determine_start_stop_bonus(self.start_stop.get())
        bonus += determine_taken_damage_bonus(
            self.taken_damage.get(), self.taken_critical.get())
        bonus += determine_friend_damage_bonus(self.friend_wounded.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
