# -*- coding: utf-8 -*-
"""
The Power Manipulation static maneuver table.

Classes:
    PowerManipulationManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.magical_skills import \
    SKILL_CHANNELING, SKILL_DIRECTED_SPELLS, SKILL_MAGIC_RITUAL, SKILL_MENTAL_CONTROL, \
    SKILL_SPELL_ARTISTRY, SKILL_SPELL_MASTERY, SKILL_SPELL_TRICKERY, SKILL_SUMMONING
from console.character.secondary_skills import SKILL_TRANSCEND_ARMOUR

import trace_log as trace

sys.path.append('../')


class PowerManipulationManeuverTable(StaticManeuverTable):
    """
    Power Manipulation static maneuver table.

    Methods:
        select_power_manipulation_table(maneuver_type)
    """
    MANEUVER_CHANNELING = "Channeling"
    MANEUVER_DIRECTED_SPELLS = "Directed Spells"
    MANEUVER_MAGIC_RITUAL = "Magic Ritual"
    MANEUVER_MENTAL_CONTROL = "Mental Control"
    MANEUVER_SPELL_ARTISTRY = "Spell Artistry"
    MANEUVER_SPELL_MASTERY = "Spell Mastery"
    MANEUVER_SPELL_TRICKERY = "Spell Trickery"
    MANEUVER_SUMMONING = "Summoning"
    MANEUVER_TRANSCEND_ARMOUR = "Transcend Armour"

    maneuver_type_options = (
        MANEUVER_CHANNELING, MANEUVER_DIRECTED_SPELLS, MANEUVER_MAGIC_RITUAL,
        MANEUVER_MENTAL_CONTROL, MANEUVER_SPELL_ARTISTRY, MANEUVER_SPELL_MASTERY,
        MANEUVER_SPELL_TRICKERY, MANEUVER_SUMMONING, MANEUVER_TRANSCEND_ARMOUR
    )

    maneuver_result_text = {
        BLUNDER:
            "Run for your life!  You have torn the magical fabric of the plane!  A "
            "bright, devouring hole appears in the air before you and will consume any "
            "matter or magical energies it encounters as it floats gently in a random "
            "direction at a walking pace for 1 - 100 rounds.  After this time, it will "
            "seal itself over and disappear.  You are completely drained of power points "
            "due to your proximity to the thing.",
        ABSOLUTE_FAILURE:
            "Your reach has exceeded your grasp this time.  Your attempt to manipulate "
            "the magical energies ends in an involuntary channeling.  Roll on the "
            "Spell Failure Table, ""Force"" column with a modification of +1 per power"
            "point involved.",
        FAILURE:
            "Your manipulation fails.  Are you sure you were supposed to goggle your "
            "eyes like that?",
        PARTIAL_SUCCESS:
            "Your manipulation does not go as well as hoped.  You take 10 concussion "
            "hits as you improperly manipulate the magical energies.",
        NEAR_SUCCESS:
            "You grit your teeth as you attempt to bend the magical energies to your "
            "will.  If the maneuver spans several rounds, you may make another roll "
            "with a +10 modification to complete the maneuver successfully.",
        SUCCESS:
            "Only a slight squint of concentration betrays the effort involved in your "
            "magical manipulations.",
        ABSOLUTE_SUCCESS:
            "The ease with which you control the magical energies surprises even you.  "
            "No wonder you get to wear the pointy hat."
    }

    maneuver_result_stats = {
        BLUNDER: (-100, 0.5, -30),
        ABSOLUTE_FAILURE: (-50, 0.8, -20),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (40, 1, 0),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_power_manipulation_table(maneuver_type):
        """
        Set the current PowerManipulation maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        trace.entry()
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.power_manipulation.magic_ritual_maneuver_table import \
            MagicRitualManeuverTable
        from maneuvers.power_manipulation.spell_mastery_maneuver_table import \
            SpellMasteryManeuverTable

        if maneuver_type == PowerManipulationManeuverTable.MANEUVER_MAGIC_RITUAL:
            trace.flow("Magic ritual maneuver")
            trace.exit()
            return MagicRitualManeuverTable()
        elif maneuver_type == PowerManipulationManeuverTable.MANEUVER_SPELL_MASTERY:
            trace.flow("Spell Mastery maneuver")
            trace.exit()
            return SpellMasteryManeuverTable()
        else:
            trace.flow("Power Manipulation maneuver")
            trace.exit()
            return PowerManipulationManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            PowerManipulationManeuverTable.MANEUVER_CHANNELING:
                [SKILL_CHANNELING, ],
            PowerManipulationManeuverTable.MANEUVER_DIRECTED_SPELLS:
                [SKILL_DIRECTED_SPELLS, ],
            PowerManipulationManeuverTable.MANEUVER_MAGIC_RITUAL:
                [SKILL_MAGIC_RITUAL, SKILL_SPELL_MASTERY],
            PowerManipulationManeuverTable.MANEUVER_MENTAL_CONTROL:
                [SKILL_MENTAL_CONTROL, ],
            PowerManipulationManeuverTable.MANEUVER_SPELL_ARTISTRY:
                [SKILL_SPELL_ARTISTRY, SKILL_SPELL_MASTERY],
            PowerManipulationManeuverTable.MANEUVER_SPELL_MASTERY:
                [SKILL_SPELL_MASTERY, ],
            PowerManipulationManeuverTable.MANEUVER_SPELL_TRICKERY:
                [SKILL_SPELL_TRICKERY, SKILL_SPELL_ARTISTRY, SKILL_SPELL_MASTERY],
            PowerManipulationManeuverTable.MANEUVER_SUMMONING:
                [SKILL_SUMMONING, ],
            PowerManipulationManeuverTable.MANEUVER_TRANSCEND_ARMOUR:
                [SKILL_TRANSCEND_ARMOUR, ]
        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
