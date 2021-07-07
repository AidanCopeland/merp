# -*- coding: utf-8 -*-
"""
The Stalking static maneuver table.

Classes:
    StalkManeuverTable

Functions:
    determine_pace_bonus(pace)
"""
import sys
from tkinter import StringVar, IntVar

from maneuvers.subterfuge_stealth_maneuver_table import SubterfugeStealthManeuverTable
from maneuvers.subterfuge_stealth import stalk_hide_utils

import frame_utils
import trace_log as trace

sys.path.append('../')

PACE_PROMPT = "Stalking pace"
CRAWL_TEXT = "Crawl (0.25x base)"
CREEP_TEXT = "Creep (0.5x base)"
WALK_TEXT = "Walk"
JOG_TEXT = "Jog (1.5x base)"
RUN_TEXT = "Run (2x base)"
SPRINT_TEXT = "Sprint, Fast Sprint, Dash (3+ x base)"

CRAWL_BONUS = 10
CREEP_BONUS = 0
WALK_BONUS = -10
JOG_BONUS = -25
RUN_BONUS = -50
SPRINT_BONUS = -75

PACE_OPTIONS = (
    CRAWL_TEXT, CREEP_TEXT, WALK_TEXT,
    JOG_TEXT, RUN_TEXT, SPRINT_TEXT
)
INVISIBILITY_TEXT = "Bonus due to any invisibility or other sensory suppression " \
                    "(Invisiblity I gives +70, modified by fringe effects)"


def determine_pace_bonus(pace):
    """
    Determine the bonus to the maneuver based on the stalking pace.
    :param pace: The stalking pace.
    :return: The bonus to the maneuver.
    """
    if pace == CRAWL_TEXT:
        trace.flow("Crawl: +10")
        return CRAWL_BONUS
    elif pace == CREEP_TEXT:
        trace.flow("Creep: +0")
        return CREEP_BONUS
    elif pace == WALK_TEXT:
        trace.flow("Walk: -10")
        return WALK_BONUS
    elif pace == JOG_TEXT:
        trace.flow("Jog: -25")
        return JOG_BONUS
    elif pace == RUN_TEXT:
        trace.flow("Run: -50")
        return RUN_BONUS
    else:
        trace.flow("Sprint: -75")
        return SPRINT_BONUS


class StalkManeuverTable(SubterfugeStealthManeuverTable):
    """
    Stalking static maneuver table.

    Methods:
        init_stalking_modifiers(self)
        setup_maneuver_skill_frames(self, parent_frame)
        redraw_stalking_modifier_frames(self, parent_frame)
        redraw_maneuver_skill_frames(self)
        skill_frames_update_callback(self, *_args)
        stalking_modifier_bonus(self)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.pace = StringVar()
        self.invisibility_bonus = IntVar()
        self.skill_frames_parent_frame = None
        self.contested = IntVar()
        self.searcher_bonus = IntVar()

        trace.exit()

    def init_stalking_modifiers(self):
        """
        Set up the modifiers related to stalking.
        """
        self.invisibility_bonus.set(0)

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        self.skill_frames_parent_frame = parent_frame

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

        self.init_stalking_modifiers()
        self.searcher_bonus.set(0)
        self.contested.set(0)
        self.redraw_maneuver_skill_frames()

        trace.exit()

    def redraw_stalking_modifier_frames(self, parent_frame):
        """
        Redraw frames containing modifiers based on the quality of stalking.
        """

        def setup_pace_frame():
            """
            Create a frame with an OptionMenu specifying the pace of stalking.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(
                parent_frame,
                PACE_PROMPT,
                CREEP_TEXT,
                self.pace,
                *PACE_OPTIONS)
            trace.exit()

        def setup_invisibility_frame():
            """
            Create a frame with an Entry specifying bonus due to invisibility.
            """
            trace.entry()
            frame_utils.setup_entry_frame(
                parent_frame, INVISIBILITY_TEXT, self.invisibility_bonus
            )
            trace.exit()

        trace.entry()

        setup_pace_frame()
        setup_invisibility_frame()

        trace.exit()

    def redraw_maneuver_skill_frames(self):
        """
        Redraw the frames containing skill-specific modifiers.
        """
        trace.entry()

        parent_frame = self.skill_frames_parent_frame
        frame_utils.destroy_frame_objects(parent_frame)

        self.redraw_stalking_modifier_frames(parent_frame)

        stalk_hide_utils.setup_contested_frame(self, parent_frame)
        if self.contested.get() == 1:
            trace.flow("Add frame for searcher bonus")
            stalk_hide_utils.setup_searcher_bonus_frame(self, parent_frame)

        trace.exit()

    def skill_frames_update_callback(self, *_args):
        """
        Callback made when it is necessary to redraw the frames containing Stalk-specific
        modifiers.
        """
        trace.entry()

        self.redraw_maneuver_skill_frames()

        trace.exit()

    def stalking_modifier_bonus(self):
        """
        Determine bonuses to apply to a Stalking maneuver based on the pace of stalking
        and any invisibility.
        :return: The bonus to apply to the maneuver.
        """
        trace.entry()

        bonus = 0

        bonus += determine_pace_bonus(self.pace.get())
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

        bonus += self.stalking_modifier_bonus()

        trace.detail("Contested? %r" % self.contested.get())

        if self.contested.get() == 1:
            trace.flow("Use searcher bonus: %d" % self.searcher_bonus.get())
            bonus += 50
            bonus -= self.searcher_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
