# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.SubterfugeStealthManeuverTable import SubterfugeStealthManeuverTable

import FrameUtils
import trace_log as trace

from Tkinter import IntVar, StringVar

HIDING_PLACE_PROMPT = "Quality of hiding place"
BAD_TEXT = "Bad"
MEDIOCRE_TEXT = "Mediocre"
FAIR_TEXT = "Fair"
GOOD_TEXT = "Good"
VERY_GOOD_TEXT = "Very good"
EXCELLENT_TEXT = "Excellent"

BAD_BONUS = -30
MEDIOCRE_BONUS = -10
FAIR_BONUS = 0
GOOD_BONUS = 10
VERY_GOOD_BONUS = 30
EXCELLENT_BONUS = 50

HIDING_PLACE_OPTIONS = (
    BAD_TEXT, MEDIOCRE_TEXT, FAIR_TEXT, GOOD_TEXT,
    VERY_GOOD_TEXT, EXCELLENT_TEXT
)

INVISIBILITY_TEXT = "Bonus due to any invisibility or other sensory suppression (Invisiblity I gives +70, modified by " \
                    "fringe effects) "

PRESENCE_KNOWN_TEXT = "Presence of hider known to searchers?"
PRESENCE_KNOWN_BONUS = -30

CONTESTED_TEXT = "Roll against searcher's Perception bonus?"

SEARCHER_BONUS_TEXT = "Searcher's Perception bonus"

def determine_hiding_place_bonus(quality):
    """
    Determine the bonus to the maneuver based on the quality of the hiding place.
    :param quality: The quality of the hiding place.
    :return: The bonus to the maneuver.
    """
    if quality == BAD_TEXT:
        trace.flow("Bad: -30")
        return BAD_BONUS
    elif quality == MEDIOCRE_TEXT:
        trace.flow("Mediocre: -10")
        return MEDIOCRE_BONUS
    elif quality == FAIR_TEXT:
        trace.flow("Fair: +0")
        return FAIR_BONUS
    elif quality == GOOD_TEXT:
        trace.flow("Good: +10")
        return GOOD_BONUS
    elif quality == VERY_GOOD_TEXT:
        trace.flow("Very good: +30")
        return VERY_GOOD_BONUS
    else:
        trace.flow("Excellent: +50")
        return EXCELLENT_BONUS


def determine_presence_known_bonus(presence_known):
    """
    Determine the bonus to the maneuver based on whether the presence of the hider
    is known to searchers.
    :param presence_known: Whether the presence of the hider is known.
    :return: The bonus to the maneuver.
    """
    if presence_known == 1:
        trace.flow("Presence known: -30")
        return PRESENCE_KNOWN_BONUS
    else:
        trace.flow("Presence not known: +0")
        return 0


class HideManeuverTable(SubterfugeStealthManeuverTable, object):

    def init_hiding_modifiers(self):
        """
        Set up the modifiers related to hiding.
        """
        self.hiding_place = StringVar()
        self.invisibility_bonus = IntVar()
        self.invisibility_bonus.set(0)

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        trace.entry()

        self.skill_frames_parent_frame = parent_frame
        self.init_hiding_modifiers()
        self.presence_known = IntVar()
        self.contested = IntVar()
        self.searcher_bonus = IntVar()
        self.searcher_bonus.set(0)
        self.contested.set(0)
        self.redraw_maneuver_skill_frames()

        trace.exit()

    def redraw_hiding_modifier_frames(self, parent_frame):
        """
        Redraw frames containing modifiers based on the quality of hiding.
        """

        def setup_hiding_place_frame():
            """
            Create a frame with an OptionMenu specifying the quality of the hiding place.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame,
                HIDING_PLACE_PROMPT,
                FAIR_TEXT,
                self.hiding_place,
                *HIDING_PLACE_OPTIONS)
            trace.exit()

        def setup_invisibility_frame():
            """
            Create a frame with an Entry specifying bonus due to invisibility.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(
                parent_frame, INVISIBILITY_TEXT, self.invisibility_bonus
            )
            trace.exit()

        trace.entry()

        setup_hiding_place_frame()
        setup_invisibility_frame()

        trace.exit()

    def redraw_maneuver_skill_frames(self):
        trace.entry()

        parent_frame = self.skill_frames_parent_frame
        FrameUtils.destroy_frame_objects(parent_frame)

        def setup_presence_known_frame():
            """
            Create a frame with a Checkbox indicating whether the presence of the hider
            is known to searchers.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(
                parent_frame, PRESENCE_KNOWN_TEXT, self.presence_known)
            trace.exit()

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

            trace.exit()

        def setup_searcher_bonus_frame():
            """
            Create a frame with an Entry for a searcher's Perception bonus.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(
                parent_frame, SEARCHER_BONUS_TEXT, self.searcher_bonus
            )
            trace.exit()

        self.redraw_hiding_modifier_frames(parent_frame)
        setup_presence_known_frame()
        setup_contested_frame()
        if self.contested.get() == 1:
            trace.flow("Add frame for searcher bonus")
            setup_searcher_bonus_frame()

        trace.exit()

    def skill_frames_update_callback(self, *args):

        trace.entry()

        self.redraw_maneuver_skill_frames()

        trace.exit()

    def hiding_modifier_bonus(self):
        """
        Determine bonuses to apply to a Hiding maneuver based on the quality of
        the hiding place and any invisibility.
        :return: The bonus to apply to the maneuver.
        """
        trace.entry()

        bonus = 0

        bonus += determine_hiding_place_bonus(self.hiding_place.get())
        bonus += self.invisibility_bonus.get()

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

        bonus += determine_hiding_place_bonus(self.hiding_place.get())
        bonus += self.invisibility_bonus.get()
        bonus += determine_presence_known_bonus(self.presence_known.get())

        trace.detail("Contested? %r" % self.contested.get())

        if self.contested.get() == 1:
            trace.flow("Use searcher bonus: %d" % self.searcher_bonus.get())
            bonus += 50
            bonus -= self.searcher_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
