# -*- coding: utf-8 -*-
from future import standard_library
import sys

from Maneuvers.MovingManeuverTable import MovingManeuverTable
from Maneuvers.OutdoorAnimalManeuverTable import intelligence_bonus, creature_type_bonus, domestication_bonus

import FrameUtils
import trace_log as trace

from tkinter import StringVar
standard_library.install_aliases()

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

NON_INTELLIGENT_TEXT = "Non-intelligent"
LOW_INTELLIGENCE_TEXT = "Low-intelligence"
ANIMAL_INTELLIGENCE_TEXT = "Animal intelligence"
INTELLIGENCE_OPTIONS = (
    NON_INTELLIGENT_TEXT, LOW_INTELLIGENCE_TEXT, ANIMAL_INTELLIGENCE_TEXT)

NON_INTELLIGENT_BONUS = -50
LOW_INTELLIGENCE_BONUS = -10
ANIMAL_INTELLIGENCE_BONUS = 0

UNTAMED_TEXT = "Wild/untamed"
TAME_TEXT = "Domesticated"
BEFRIENDED_TEXT = "Befriended/raised from birth"
DOMESTICATION_OPTIONS = (
    UNTAMED_TEXT, TAME_TEXT, BEFRIENDED_TEXT
)

UNTAMED_BONUS = -20
TAME_BONUS = 0
BEFRIENDED_BONUS = 30

AMPHIBIAN_TEXT = "Amphibian"
ARTHROPOD_TEXT = "Arthropods (insects)"
AVIAN_TEXT = "Avian (birds)"
BOVINE_TEXT = "Bovine (cattle, buffalo, deer, etc.)"
CANINE_TEXT = "Canine (dogs, wolves, foxes, etc.)"
CETACEAN_TEXT = "Cetacean (all sea mammals)"
COELENTERATE_TEXT = "Coelenterate (jellyfish, etc.)"
EQUINE_TEXT = "Equine (all horse types)"
FELINE_TEXT = "Feline (all cats)"
FISH_TEXT = "Fish (all fish with bones, scales, fins)"
MOLLUSC_TEXT = "Mollusca (snails, clams, squids, etc.)"
PACHYDERM_TEXT = "Pachyderms (elephants, rhinoceros, etc.)"
RODENT_TEXT = "Rodents (rats, beavers, rabbits, etc.)"
SAURIAN_TEXT = "Saurians (dry-land, legged reptiles)"
SERPENTINE_TEXT = "Serpentine (all snakes and serpents)"
SIMIAN_TEXT = "Simians (apes, monkeys and gorillas)"
SWINE_TEXT = "Swine (pigs, boars, etc.)"
URSINE_TEXT = "Ursine (bears, wolverines, pandas, etc.)"
CREATURE_TYPE_OPTIONS = (
    AMPHIBIAN_TEXT, ARTHROPOD_TEXT, AVIAN_TEXT, BOVINE_TEXT, CANINE_TEXT,
    CETACEAN_TEXT, COELENTERATE_TEXT, EQUINE_TEXT, FELINE_TEXT, FISH_TEXT,
    MOLLUSC_TEXT, PACHYDERM_TEXT, RODENT_TEXT, SAURIAN_TEXT, SERPENTINE_TEXT,
    SIMIAN_TEXT, SWINE_TEXT, URSINE_TEXT
)

AMPHIBIAN_BONUS = -10
ARTHROPOD_BONUS = -50
AVIAN_BONUS = -20
BOVINE_BONUS = 0
CANINE_BONUS = 10
CETACEAN_BONUS = -20
COELENTERATE_BONUS = -10
EQUINE_BONUS = 0
FELINE_BONUS = -10
FISH_BONUS = -30
MOLLUSC_BONUS = -40
PACHYDERM_BONUS = 0
RODENT_BONUS = 0
SAURIAN_BONUS = -10
SERPENTINE_BONUS = -10
SIMIAN_BONUS = 50
SWINE_BONUS = 0
URSINE_BONUS = 0


class RidingManeuverTable(MovingManeuverTable):
    def __init__(self, **kwargs):
        trace.entry()
        super(MovingManeuverTable, self).__init__(**kwargs)
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
            FrameUtils.setup_optionmenu_frame(
                parent_frame, ACTIVITY_PROMPT, SIXTY_PERCENT_TEXT, self.activity_amount, *ACTIVITY_OPTIONS)
            trace.exit()

        def setup_intelligence_frame():
            """
            Create a frame with an OptionMenu specifying the level of the creature's intelligence.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, INTELLIGENCE_PROMPT, ANIMAL_INTELLIGENCE_TEXT, self.intelligence, *INTELLIGENCE_OPTIONS)
            trace.exit()

        def setup_domestication_frame():
            """
            Create a frame with an OptionMenu specifying the level of domestication of the creature.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, DOMESTICATION_PROMPT, TAME_TEXT, self.domestication, *DOMESTICATION_OPTIONS)
            trace.exit()

        def setup_creature_type_frame():
            """
            Create a frame with an OptionMenu specifying the type of the creature.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, CREATURE_TYPE_PROMPT, EQUINE_TEXT, self.creature_type, *CREATURE_TYPE_OPTIONS)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
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
