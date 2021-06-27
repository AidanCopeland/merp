# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Maneuvers.StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')

INTELLIGENCE_PROMPT = "Creature's intelligence level"
DOMESTICATION_PROMPT = "Creature's level of domestication"
CREATURE_TYPE_PROMPT = "Type of creature"

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


def intelligence_bonus(intelligence):
    if intelligence == ANIMAL_INTELLIGENCE_TEXT:
        trace.flow("Animal intelligence: 0")
        return ANIMAL_INTELLIGENCE_BONUS
    elif intelligence == LOW_INTELLIGENCE_TEXT:
        trace.flow("Low intelligence: -10")
        return LOW_INTELLIGENCE_BONUS
    else:
        trace.flow("Non-intelligent: -50")
        return NON_INTELLIGENT_BONUS


def domestication_bonus(domestication):
    if domestication == UNTAMED_TEXT:
        trace.flow("Untamed: -20")
        return UNTAMED_BONUS
    elif domestication == TAME_TEXT:
        trace.flow("Tame: +0")
        return TAME_BONUS
    else:
        trace.flow("Befriended from birth: +30")
        return BEFRIENDED_BONUS


def creature_type_bonus(creature_type):
    if creature_type == AMPHIBIAN_TEXT:
        trace.flow("Amphibian: -10")
        return AMPHIBIAN_BONUS
    elif creature_type == ARTHROPOD_TEXT:
        trace.flow("Arthropod: -50")
        return ARTHROPOD_BONUS
    elif creature_type == AVIAN_TEXT:
        trace.flow("Avian: -20")
        return AVIAN_BONUS
    elif creature_type == BOVINE_TEXT:
        trace.flow("Bovine: +0")
        return BOVINE_BONUS
    elif creature_type == CANINE_TEXT:
        trace.flow("Canine: +10")
        return CANINE_BONUS
    elif creature_type == CETACEAN_TEXT:
        trace.flow("Cetacean: -20")
        return CETACEAN_BONUS
    elif creature_type == COELENTERATE_TEXT:
        trace.flow("Coelenterate: -10")
        return COELENTERATE_BONUS
    elif creature_type == EQUINE_TEXT:
        trace.flow("Equine: +0")
        return EQUINE_BONUS
    elif creature_type == FELINE_TEXT:
        trace.flow("Feline: -10")
        return FELINE_BONUS
    elif creature_type == FISH_BONUS:
        trace.flow("Fish: -30")
        return FISH_BONUS
    elif creature_type == MOLLUSC_TEXT:
        trace.flow("Mollusc: -40")
        return MOLLUSC_BONUS
    elif creature_type == PACHYDERM_TEXT:
        trace.flow("Pachyderm: +0")
        return PACHYDERM_BONUS
    elif creature_type == RODENT_TEXT:
        trace.flow("Rodent: +0")
        return RODENT_BONUS
    elif creature_type == SAURIAN_TEXT:
        trace.flow("Saurian: -10")
        return SAURIAN_BONUS
    elif creature_type == SERPENTINE_TEXT:
        trace.flow("Serpentine: -10")
        return SERPENTINE_BONUS
    elif creature_type == SIMIAN_TEXT:
        trace.flow("Simian: -50")
        return SIMIAN_BONUS
    elif creature_type == SWINE_TEXT:
        trace.flow("Swine: +0")
        return SWINE_BONUS
    else:
        trace.flow("Ursine: +0")
        return URSINE_BONUS


class OutdoorAnimalManeuverTable(StaticManeuverTable):
    MANEUVER_ANIMAL_HANDLING = "Animal Handling"
    MANEUVER_ANIMAL_HEALING = "Animal Healing"
    MANEUVER_ANIMAL_MASTERY = "Animal Mastery"
    MANEUVER_ANIMAL_TRAINING = "Animal Training"
    MANEUVER_DRIVING = "Driving"
    MANEUVER_HERDING = "Herding"
    MANEUVER_RIDING = "Riding"

    maneuver_type_options = (
        MANEUVER_ANIMAL_HANDLING, MANEUVER_ANIMAL_HEALING, MANEUVER_ANIMAL_MASTERY,
        MANEUVER_ANIMAL_TRAINING, MANEUVER_DRIVING, MANEUVER_HERDING,
        MANEUVER_RIDING
    )

    maneuver_result_text = {
        BLUNDER:
            "You cad!  Your cruel mistreatment of the beast is life-threatening: roll a "
            "random 'C' critical on the beast.  It lashes out at you, eyes rolling in "
            "frenzy.  After making an attack at +30 against you, it will attempt to "
            "bolt in a random direction, heedless of its own health or safety.  Any "
            "attempt the animal makes to escape a tether will be at +30.  All future "
            "attempts to work with this animal will be at a modification of -30 "
            "(non-cumulative) until you achieve a result of Absolute Success with it. ",
        ABSOLUTE_FAILURE:
            "Your clumsy handling terrifies the poor animal.  It lashes out at you, eyes "
            "rolling in frenzy.  After making an attack at +30 against you, it will "
            "attempt to bolt in a random direction, heedless of its own health or safety. "
            "Any attempt the animal makes to escape a tether will be at +30.",
        FAILURE:
            "The animal responds poorly to your attempt, attempting to move away from "
            "you.  You fail your maneuver.",
        PARTIAL_SUCCESS:
            "Sometimes animals just seem to have a mind of their own, don't they?  "
            "Nothing you do seems to get this animal to listen to you.  "
            "Maybe you should have given it a scooby-snack.",
        NEAR_SUCCESS:
            "The beast is unsure, and reluctantly submits to your ministrations.  Try to "
            "keep your impatience in check, and make another roll next round at +10 if "
            "appropriate.",
        SUCCESS:
            "Your gentle touch and sure hand bring comfort and obedience to the beast.  "
            "You are successful in your maneuver.",
        ABSOLUTE_SUCCESS:
            "Your rapport with the animal is perfect!  It submits to your will almost "
            "instinctively."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 3, -20),
        ABSOLUTE_FAILURE: (-20, 2.5, -10),
        FAILURE: (0, 2, 0),
        PARTIAL_SUCCESS: (10, 1.75, 0),
        NEAR_SUCCESS: (90, 1.25, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.5, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super(StaticManeuverTable, self).__init__(**kwargs)
        self.intelligence = StringVar()
        self.domestication = StringVar()
        self.creature_type = StringVar()

        trace.exit()

    @staticmethod
    def select_outdoor_animal_table(maneuver_type):
        """
        Set the current OutdoorAnimal maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """

        from Maneuvers.OutdoorAnimal.RidingManeuverTable import RidingManeuverTable

        if maneuver_type == OutdoorAnimalManeuverTable.MANEUVER_RIDING:
            trace.flow("Riding maneuver")
            trace.exit()
            return RidingManeuverTable()
        else:
            return OutdoorAnimalManeuverTable()

    def setup_intelligence_frame(self, parent_frame):
        """
        Create a frame with an OptionMenu specifying the level of the creature's intelligence.
        """
        trace.entry()
        FrameUtils.setup_optionmenu_frame(
            parent_frame, INTELLIGENCE_PROMPT, ANIMAL_INTELLIGENCE_TEXT, self.intelligence, *INTELLIGENCE_OPTIONS)
        trace.exit()

    def setup_domestication_frame(self, parent_frame):
        """
        Create a frame with an OptionMenu specifying the level of domestication of the creature.
        """
        trace.entry()
        FrameUtils.setup_optionmenu_frame(
            parent_frame, DOMESTICATION_PROMPT, TAME_TEXT, self.domestication, *DOMESTICATION_OPTIONS)
        trace.exit()

    def setup_creature_type_frame(self, parent_frame):
        """
        Create a frame with an OptionMenu specifying the type of the creature.
        """
        trace.entry()
        FrameUtils.setup_optionmenu_frame(
            parent_frame, CREATURE_TYPE_PROMPT, EQUINE_TEXT, self.creature_type, *CREATURE_TYPE_OPTIONS)
        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """
        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)

        self.setup_intelligence_frame(parent_frame)
        self.setup_domestication_frame(parent_frame)
        self.setup_creature_type_frame(parent_frame)

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += intelligence_bonus(self.intelligence.get())

        bonus += domestication_bonus(self.domestication.get())

        bonus += creature_type_bonus(self.creature_type.get())

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
