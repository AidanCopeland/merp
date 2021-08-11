# -*- coding: utf-8 -*-
"""
The Outdoor/Animal static maneuver table.

Classes:
    OutdoorAnimalManeuverTable
"""
from __future__ import absolute_import
import sys
from tkinter import StringVar

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.secondary_skills import \
    SKILL_ANIMAL_HANDLING, SKILL_ANIMAL_HEALING, SKILL_ANIMAL_HUSBANDRY, SKILL_ANIMAL_TRAINING, \
    SKILL_BEAST_MASTERY, SKILL_HERDING, SKILL_DRIVING
from console.character.general_skills import SKILL_ANIMAL_MASTERY, SKILL_RIDE

import frame_utils
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
    """
    Determine the bonus to maneuver based on intelligence.
    :param intelligence: The animal intelligence level.
    :returns: The bonus to maneuver.
    """
    bonus = _intelligence_bonus.get(intelligence, 0)
    trace.detail("%s: bonus %d" % (intelligence, bonus))
    return bonus


_intelligence_bonus = {
    ANIMAL_INTELLIGENCE_TEXT: ANIMAL_INTELLIGENCE_BONUS,
    LOW_INTELLIGENCE_TEXT: LOW_INTELLIGENCE_BONUS,
    NON_INTELLIGENT_TEXT: NON_INTELLIGENT_BONUS
}


def domestication_bonus(domestication):
    """
    Determine the bonus to maneuvers based on the level of domestication.
    :param domestication: The level of domestication.
    :returns: The bonus to maneuvers.
    """
    bonus = _domestication_bonus.get(domestication, 0)
    trace.detail("%s: bonus %d" % (domestication, bonus))
    return bonus


_domestication_bonus = {
    UNTAMED_TEXT: UNTAMED_BONUS,
    TAME_TEXT: TAME_BONUS,
    BEFRIENDED_TEXT: BEFRIENDED_BONUS
}


def creature_type_bonus(creature_type):
    """
    Determine the bonus to maneuvers based on the creature type.
    :param creature_type: The creature type.
    :return: The bonus to maneuvers.
    """
    bonus = _creature_bonus.get(creature_type, 0)
    trace.detail("%s: bonus %d" % (creature_type, bonus))
    return bonus


_creature_bonus = {
    AMPHIBIAN_TEXT: AMPHIBIAN_BONUS,
    ARTHROPOD_TEXT: ARTHROPOD_BONUS,
    AVIAN_TEXT: AVIAN_BONUS,
    BOVINE_TEXT: BOVINE_BONUS,
    CANINE_TEXT: CANINE_BONUS,
    CETACEAN_TEXT: CETACEAN_BONUS,
    COELENTERATE_TEXT: COELENTERATE_BONUS,
    EQUINE_TEXT: EQUINE_BONUS,
    FELINE_TEXT: FELINE_BONUS,
    FISH_TEXT: FISH_BONUS,
    MOLLUSC_TEXT: MOLLUSC_BONUS,
    PACHYDERM_TEXT: PACHYDERM_BONUS,
    RODENT_TEXT: RODENT_BONUS,
    SAURIAN_TEXT: SAURIAN_BONUS,
    SERPENTINE_TEXT: SERPENTINE_BONUS,
    SIMIAN_TEXT: SIMIAN_BONUS,
    SWINE_TEXT: SWINE_BONUS,
    URSINE_TEXT: URSINE_TEXT
}


class OutdoorAnimalManeuverTable(StaticManeuverTable):
    """
    Outdoor/Animal static maneuver table.

    Methods:
        intelligence_bonus(intelligence)
        domestication_bonus(domestication)
        creature_type_bonus(creature_type)
    """
    MANEUVER_ANIMAL_HANDLING = "Animal Handling"
    MANEUVER_ANIMAL_HEALING = "Animal Healing"
    MANEUVER_ANIMAL_HUSBANDRY = "Animal Husbandry"
    MANEUVER_ANIMAL_MASTERY = "Animal Mastery"
    MANEUVER_ANIMAL_TRAINING = "Animal Training"
    MANEUVER_BEAST_MASTERY = "Beast Mastery"
    MANEUVER_DRIVING = "Driving"
    MANEUVER_HERDING = "Herding"
    MANEUVER_RIDING = "Riding"

    maneuver_type_options = (
        MANEUVER_ANIMAL_HANDLING, MANEUVER_ANIMAL_HEALING, MANEUVER_ANIMAL_HUSBANDRY,
        MANEUVER_ANIMAL_MASTERY, MANEUVER_ANIMAL_TRAINING, MANEUVER_BEAST_MASTERY, MANEUVER_DRIVING,
        MANEUVER_HERDING, MANEUVER_RIDING
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
        super().__init__(**kwargs)
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
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.outdoor_animal.riding_maneuver_table import RidingManeuverTable

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
        frame_utils.setup_optionmenu_frame(parent_frame,
                                           INTELLIGENCE_PROMPT,
                                           ANIMAL_INTELLIGENCE_TEXT,
                                           self.intelligence,
                                           *INTELLIGENCE_OPTIONS)
        trace.exit()

    def setup_domestication_frame(self, parent_frame):
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

    def setup_creature_type_frame(self, parent_frame):
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

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """
        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)

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

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            OutdoorAnimalManeuverTable.MANEUVER_ANIMAL_HANDLING:
                [SKILL_ANIMAL_HANDLING, SKILL_ANIMAL_MASTERY],
            OutdoorAnimalManeuverTable.MANEUVER_ANIMAL_HEALING:
                [SKILL_ANIMAL_HEALING, SKILL_ANIMAL_MASTERY],
            OutdoorAnimalManeuverTable.MANEUVER_ANIMAL_HUSBANDRY:
                [SKILL_ANIMAL_HUSBANDRY, SKILL_ANIMAL_HANDLING, SKILL_ANIMAL_MASTERY],
            OutdoorAnimalManeuverTable.MANEUVER_ANIMAL_MASTERY:
                [SKILL_ANIMAL_MASTERY, ],
            OutdoorAnimalManeuverTable.MANEUVER_ANIMAL_TRAINING:
                [SKILL_ANIMAL_TRAINING, SKILL_ANIMAL_MASTERY],
            OutdoorAnimalManeuverTable.MANEUVER_BEAST_MASTERY:
                [SKILL_BEAST_MASTERY, SKILL_ANIMAL_MASTERY],
            OutdoorAnimalManeuverTable.MANEUVER_DRIVING:
                [SKILL_DRIVING, SKILL_RIDE],
            OutdoorAnimalManeuverTable.MANEUVER_HERDING:
                [SKILL_HERDING, SKILL_ANIMAL_MASTERY]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
