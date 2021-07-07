# -*- coding: utf-8 -*-
"""
The Riding moving maneuver table.

Classes:
    RidingManeuverTable
"""
import sys
from tkinter import StringVar

from maneuvers.moving_maneuver_table import MovingManeuverTable
from maneuvers.outdoor_animal_maneuver_table import \
    intelligence_bonus, creature_type_bonus, domestication_bonus
from maneuvers.outdoor_animal_maneuver_table import \
    INTELLIGENCE_OPTIONS, DOMESTICATION_OPTIONS, CREATURE_TYPE_OPTIONS
from maneuvers.outdoor_animal_maneuver_table import \
    ANIMAL_INTELLIGENCE_TEXT, TAME_TEXT, EQUINE_TEXT

import frame_utils
import trace_log as trace


sys.path.append('../')

ACTIVITY_PROMPT = "Activity used for riding"
INTELLIGENCE_PROMPT = "Creature's intelligence level"
DOMESTICATION_PROMPT = "Creature's level of domestication"
CREATURE_TYPE_PROMPT = "Type of creature"

FIVE_PERCENT_TEXT = "5%"
TEN_PERCENT_TEXT = "10%"
TWENTY_PERCENT_TEXT = "20%"
THIRTY_PERCENT_TEXT = "30%"
FORTY_PERCENT_TEXT = "40%"
FIFTY_PERCENT_TEXT = "50%"
SIXTY_PERCENT_TEXT = "60% (normal, no penalty/bonus)"
SEVENTY_PERCENT_TEXT = "70%"
EIGHTY_PERCENT_TEXT = "80%"
NINETY_PERCENT_TEXT = "90%"
HUNDRED_PERCENT_TEXT = "100%"
ACTIVITY_OPTIONS = (
    FIVE_PERCENT_TEXT, TEN_PERCENT_TEXT, TWENTY_PERCENT_TEXT, THIRTY_PERCENT_TEXT,
    FORTY_PERCENT_TEXT, FIFTY_PERCENT_TEXT, SIXTY_PERCENT_TEXT, SEVENTY_PERCENT_TEXT,
    EIGHTY_PERCENT_TEXT, NINETY_PERCENT_TEXT, HUNDRED_PERCENT_TEXT
)

FIVE_PERCENT_BONUS = -30
TEN_PERCENT_BONUS = -25
TWENTY_PERCENT_BONUS = -20
THIRTY_PERCENT_BONUS = -15
FORTY_PERCENT_BONUS = -10
FIFTY_PERCENT_BONUS = -5
SIXTY_PERCENT_BONUS = 0
SEVENTY_PERCENT_BONUS = 10
EIGHTY_PERCENT_BONUS = 20
NINETY_PERCENT_BONUS = 35
HUNDRED_PERCENT_BONUS = 50


class RidingManeuverTable(MovingManeuverTable):
    """
    Riding moving maneuver table.

    Methods:
        setup_maneuver_skill_frames(self, parent_frame)
        skill_type_bonus(self)
    """
    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.activity_amount = StringVar()
        self.intelligence = StringVar()
        self.domestication = StringVar()
        self.creature_type = StringVar()

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_activity_frame():
            """
            Create a frame with an OptionMenu specifying the amount of activity used for riding.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               ACTIVITY_PROMPT,
                                               SIXTY_PERCENT_TEXT,
                                               self.activity_amount,
                                               *ACTIVITY_OPTIONS)
            trace.exit()

        def setup_intelligence_frame():
            """
            Create a frame with an OptionMenu specifying the level of the creature's intelligence.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               INTELLIGENCE_PROMPT,
                                               ANIMAL_INTELLIGENCE_TEXT,
                                               self.intelligence,
                                               *INTELLIGENCE_OPTIONS)
            trace.exit()

        def setup_domestication_frame():
            """
            Create a frame with an OptionMenu specifying the level of domestication of the creature.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               DOMESTICATION_PROMPT,
                                               TAME_TEXT,
                                               self.domestication,
                                               *DOMESTICATION_OPTIONS)
            trace.exit()

        def setup_creature_type_frame():
            """
            Create a frame with an OptionMenu specifying the type of the creature.
            """
            trace.entry()
            frame_utils.setup_optionmenu_frame(parent_frame,
                                               CREATURE_TYPE_PROMPT,
                                               EQUINE_TEXT,
                                               self.creature_type,
                                               *CREATURE_TYPE_OPTIONS)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        setup_activity_frame()
        setup_intelligence_frame()
        setup_domestication_frame()
        setup_creature_type_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        activity_amount = self.activity_amount.get()
        if activity_amount == FIVE_PERCENT_TEXT:
            trace.flow("5% activity: -30")
            bonus += FIVE_PERCENT_BONUS
        elif activity_amount == TEN_PERCENT_TEXT:
            trace.flow("10% activity: -25")
            bonus += TEN_PERCENT_BONUS
        elif activity_amount == TWENTY_PERCENT_TEXT:
            trace.flow("20% activity: -20")
            bonus += TWENTY_PERCENT_BONUS
        elif activity_amount == THIRTY_PERCENT_TEXT:
            trace.flow("30% activity: -15")
            bonus += THIRTY_PERCENT_BONUS
        elif activity_amount == FORTY_PERCENT_TEXT:
            trace.flow("40% activity: -10")
            bonus += FORTY_PERCENT_BONUS
        elif activity_amount == FIFTY_PERCENT_TEXT:
            trace.flow("50% activity: -5")
            bonus += FIFTY_PERCENT_BONUS
        elif activity_amount == SIXTY_PERCENT_TEXT:
            trace.flow("60% activity: +0")
            bonus += SIXTY_PERCENT_BONUS
        elif activity_amount == SEVENTY_PERCENT_TEXT:
            trace.flow("70% activity: +10")
            bonus += SEVENTY_PERCENT_BONUS
        elif activity_amount == EIGHTY_PERCENT_TEXT:
            trace.flow("80% activity: +20")
            bonus += EIGHTY_PERCENT_BONUS
        elif activity_amount == NINETY_PERCENT_BONUS:
            trace.flow("90% activity: +35")
            bonus += NINETY_PERCENT_BONUS
        elif activity_amount == HUNDRED_PERCENT_TEXT:
            trace.flow("100% activity: +50")
            bonus += HUNDRED_PERCENT_BONUS

        bonus += intelligence_bonus(self.intelligence.get())

        bonus += domestication_bonus(self.domestication.get())

        bonus += creature_type_bonus(self.creature_type.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
