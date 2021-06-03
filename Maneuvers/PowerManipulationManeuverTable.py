# -*- coding: utf-8 -*-
import sys

from StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')


class PowerManipulationManeuverTable(StaticManeuverTable):
    MANEUVER_CHANNELING = "Channeling"
    MANEUVER_MAGIC_RITUAL = "Magic Ritual"
    MANEUVER_SPELL_ARTISTRY = "Spell Artistry"
    MANEUVER_SPELL_MASTERY = "Spell Mastery"
    MANEUVER_SPELL_TRICKERY = "Spell Trickery"
    MANEUVER_SUMMONING = "Summoning"

    maneuver_type_options = (
        MANEUVER_CHANNELING, MANEUVER_MAGIC_RITUAL, MANEUVER_SPELL_ARTISTRY,
        MANEUVER_SPELL_MASTERY, MANEUVER_SPELL_TRICKERY, MANEUVER_SUMMONING
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

        from Maneuvers.PowerManipulation.MagicRitualManeuverTable import MagicRitualManeuverTable
        from Maneuvers.PowerManipulation.SpellMasteryManeuverTable import SpellMasteryManeuverTable

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