# -*- coding: utf-8 -*-
"""
The Self Control static maneuver table.

Classes:
    SelfControlManeuverTable
"""
from __future__ import absolute_import
from __future__ import division
import sys
from tkinter import IntVar
from past.utils import old_div

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.movement_skills import \
    SKILL_ADRENAL_BALANCE, SKILL_ADRENAL_LANDING, SKILL_ADRENAL_LEAPING, SKILL_ADRENAL_SPEED
from console.character.weapon_skills import \
    SKILL_ADRENAL_QUICKDRAW, SKILL_QUICKDRAW, SKILL_ADRENAL_STABILIZATION, SKILL_ADRENAL_STRENGTH, \
    SKILL_FRENZY, SKILL_STUNNED_MANEUVERING, SKILL_POWER_STRIKING
from console.character.general_skills import SKILL_TIGHTROPE_WALKING, SKILL_ACROBATICS
from console.character.magical_skills import SKILL_SPELL_CONCENTRATION
from console.character.secondary_skills import \
    SKILL_ADRENAL_CONCENTRATION, SKILL_CLEANSING_TRANCE, SKILL_CONTROL_LYCANTHROPY, \
    SKILL_DEATH_TRANCE, SKILL_DRUG_TOLERANCE, SKILL_HEALING_TRANCE, SKILL_MEDITATION, \
    SKILL_MNEMONICS, SKILL_POISON_TOLERANCE, SKILL_SLEEP_TRANCE, SKILL_TUMBLING
import frame_utils
import trace_log as trace

sys.path.append('../')

ROUNDS_PREPARED_TEXT = "Number of consecutive rounds prepared (100% activity)"
CONSECUTIVE_ROUNDS_NEEDED = 3
CONSECUTIVE_ROUNDS_BONUS = 10
MAX_PREPARATION_BONUS = 50


class SelfControlManeuverTable(StaticManeuverTable):
    """
    Self Control static maneuver table.

    Methods:
        select_self_control_table(maneuver_type)
        setup_maneuver_table_frames(self, parent_frame)
        table_bonus(self)
    """
    MANEUVER_ADRENAL_BALANCE = "Adrenal Balance"
    MANEUVER_ADRENAL_CONCENTRATION = "Adrenal Concentration"
    MANEUVER_ADRENAL_LANDING = "Adrenal Landing"
    MANEUVER_ADRENAL_LEAPING = "Adrenal Leaping"
    MANEUVER_ADRENAL_QUICKDRAW = "Adrenal Quickdraw"
    MANEUVER_ADRENAL_SPEED = "Adrenal Speed"
    MANEUVER_ADRENAL_STABILIZATION = "Adrenal Stabilization"
    MANEUVER_ADRENAL_STRENGTH = "Adrenal Strength"
    MANEUVER_CLEANSING_TRANCE = "Cleansing Trance"
    MANEUVER_CONTROL_LYCANTHROPY = "Control Lycanthropy"
    MANEUVER_DEATH_TRANCE = "Death Trance"
    MANEUVER_DRUG_TOLERANCE = "Drug Tolerance"
    MANEUVER_FRENZY = "Frenzy"
    MANEUVER_HEALING_TRANCE = "Healing Trance"
    MANEUVER_MEDITATION = "Meditation"
    MANEUVER_MNEMONICS = "Mnemonics"
    MANEUVER_POISON_TOLERANCE = "Poison Tolerance"
    MANEUVER_SLEEP_TRANCE = "Sleep Trance"
    MANEUVER_SPELL_CONCENTRATION = "Spell Concentration"
    MANEUVER_STUNNED_MANEUVERING = "Stunned Maneuvering"

    maneuver_type_options = (
        MANEUVER_ADRENAL_BALANCE, MANEUVER_ADRENAL_CONCENTRATION, MANEUVER_ADRENAL_LANDING,
        MANEUVER_ADRENAL_LEAPING, MANEUVER_ADRENAL_QUICKDRAW, MANEUVER_ADRENAL_SPEED,
        MANEUVER_ADRENAL_STABILIZATION, MANEUVER_ADRENAL_STRENGTH, MANEUVER_CLEANSING_TRANCE,
        MANEUVER_CONTROL_LYCANTHROPY, MANEUVER_DEATH_TRANCE, MANEUVER_DRUG_TOLERANCE,
        MANEUVER_FRENZY, MANEUVER_HEALING_TRANCE, MANEUVER_MEDITATION, MANEUVER_MNEMONICS,
        MANEUVER_POISON_TOLERANCE, MANEUVER_SLEEP_TRANCE, MANEUVER_SPELL_CONCENTRATION,
        MANEUVER_STUNNED_MANEUVERING
    )

    maneuver_result_text = {
        BLUNDER:
            "What were you thinking?  Your feeble attempt at focus has actually created "
            "a mental block which causes you to operate at a -30 modification (non-"
            "cumulative) to this skill until you achieve a result of Absolute Success "
            "on this table.  In addition, you are stunned for two rounds as you "
            "contemplate your failure.",
        ABSOLUTE_FAILURE:
            "Surely you jest.  I hope this wasn't a preparation round, because you get "
            "no benefits, and you lose 30% activity next round.",
        FAILURE:
            "You fail to summon the inner focus necessary for this feat, and receive "
            "no benefit or effects from your attempt.  Thanks for playing.",
        PARTIAL_SUCCESS:
            "You are distracted at the critical moment.  If not in combat, you may "
            "abort your attempt and try again.  Perhaps you should switch to decaff.",
        NEAR_SUCCESS:
            "If not in combat, you may immediately make another roll at +10 to achieve "
            "full concentration.  Otherwise, it's tough noogies, friend.",
        SUCCESS:
            "You are a paragon of self-control.  Now maybe you'll stay out of the "
            "cookie jar.",
        ABSOLUTE_SUCCESS:
            "You may attempt this skill again next round without preparation (i.e., you "
            "may operate at 100% activity this round and still use this skill next "
            "round)."
    }

    maneuver_result_stats = {
        BLUNDER: (-25, 1.5, -20),
        ABSOLUTE_FAILURE: (0, 1, -25),
        FAILURE: (0, 1, -5),
        PARTIAL_SUCCESS: (30, 0.5, 0),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.1, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.rounds_prepared = IntVar()

        trace.exit()

    @staticmethod
    def select_self_control_table(maneuver_type):
        """
        Set the current SelfControl maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=too-many-return-statements
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems

        trace.entry()

        from maneuvers.combat_maneuvers.quickdraw_maneuver_table import QuickdrawManeuverTable
        from maneuvers.self_control.adrenal_stablization_maneuver_table import \
            AdrenalStabilizationManeuverTable
        from maneuvers.self_control.adrenal_strength_maneuver_table import \
            AdrenalStrengthManeuverTable
        from maneuvers.self_control.control_lycanthropy_maneuver_table import \
            ControlLycanthropyManeuverTable
        from maneuvers.self_control.drug_tolerance_maneuver_table import \
            DrugToleranceManeuverTable
        from maneuvers.self_control.meditation_maneuver_table import MeditationManeuverTable
        from maneuvers.self_control.mnemonics_maneuver_table import MnemonicsManeuverTable
        from maneuvers.self_control.poison_tolerance_maneuver_table import \
            PoisonToleranceManeuverTable
        from maneuvers.self_control.spell_concentration_maneuver_table import \
            SpellConcentrationManeuverTable
        from maneuvers.self_control.stunned_maneuvering_maneuver_table import \
            StunnedManeuveringManeuverTable

        if maneuver_type == SelfControlManeuverTable.MANEUVER_ADRENAL_QUICKDRAW:
            trace.flow("Adrenal Quickdraw maneuver")
            trace.exit()
            return QuickdrawManeuverTable()
        if maneuver_type == SelfControlManeuverTable.MANEUVER_ADRENAL_STABILIZATION:
            trace.flow("Adrenal Stabilization maneuver")
            trace.exit()
            return AdrenalStabilizationManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_ADRENAL_STRENGTH:
            trace.flow("Adrenal Strength maneuver")
            trace.exit()
            return AdrenalStrengthManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_CONTROL_LYCANTHROPY:
            trace.flow("Control Lycanthropy maneuver")
            trace.exit()
            return ControlLycanthropyManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_DRUG_TOLERANCE:
            trace.flow("Drug Tolerance maneuver")
            trace.exit()
            return DrugToleranceManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_MEDITATION:
            trace.flow("Meditation maneuver")
            trace.exit()
            return MeditationManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_MNEMONICS:
            trace.flow("Mnemonics maneuver")
            trace.exit()
            return MnemonicsManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_POISON_TOLERANCE:
            trace.flow("Poison Tolerance maneuver")
            trace.exit()
            return PoisonToleranceManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_SPELL_CONCENTRATION:
            trace.flow("Spell Concentration maneuver")
            trace.exit()
            return SpellConcentrationManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_STUNNED_MANEUVERING:
            trace.flow("Stunned Maneuvering maneuver")
            trace.exit()
            return StunnedManeuveringManeuverTable()
        else:
            trace.flow("Other maneuver")
            return SelfControlManeuverTable()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_rounds_prepared_frame():
            """
            Create a frame with an Entry indicating the number of rounds of preparation.
            """
            trace.entry()
            frame_utils.setup_entry_frame(parent_frame, ROUNDS_PREPARED_TEXT, self.rounds_prepared)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.rounds_prepared.set(0)
        setup_rounds_prepared_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        rounds_prepared = self.rounds_prepared.get()
        trace.detail("Rounds of full prep: %d" % rounds_prepared)

        full_periods = old_div((rounds_prepared + 1), CONSECUTIVE_ROUNDS_NEEDED)
        bonus = \
            min(MAX_PREPARATION_BONUS, full_periods * CONSECUTIVE_ROUNDS_BONUS)
        trace.detail("Preparation bonus: %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            SelfControlManeuverTable.MANEUVER_ADRENAL_BALANCE:
                [SKILL_ADRENAL_BALANCE, SKILL_TIGHTROPE_WALKING],
            SelfControlManeuverTable.MANEUVER_ADRENAL_CONCENTRATION:
                [SKILL_ADRENAL_CONCENTRATION, SKILL_SPELL_CONCENTRATION, ],
            SelfControlManeuverTable.MANEUVER_ADRENAL_LANDING:
                [SKILL_ADRENAL_LANDING, SKILL_TUMBLING, SKILL_ACROBATICS],
            SelfControlManeuverTable.MANEUVER_ADRENAL_LEAPING:
                [SKILL_ADRENAL_LEAPING, SKILL_ACROBATICS, ],
            SelfControlManeuverTable.MANEUVER_ADRENAL_QUICKDRAW:
                [SKILL_ADRENAL_QUICKDRAW, SKILL_QUICKDRAW],
            SelfControlManeuverTable.MANEUVER_ADRENAL_SPEED:
                [SKILL_ADRENAL_SPEED, ],
            SelfControlManeuverTable.MANEUVER_ADRENAL_STABILIZATION:
                [SKILL_ADRENAL_STABILIZATION, SKILL_DEATH_TRANCE],
            SelfControlManeuverTable.MANEUVER_ADRENAL_STRENGTH:
                [SKILL_ADRENAL_STRENGTH, SKILL_POWER_STRIKING],
            SelfControlManeuverTable.MANEUVER_CLEANSING_TRANCE:
                [SKILL_CLEANSING_TRANCE, SKILL_HEALING_TRANCE, SKILL_DEATH_TRANCE, ],
            SelfControlManeuverTable.MANEUVER_CONTROL_LYCANTHROPY:
                [SKILL_CONTROL_LYCANTHROPY, ],
            SelfControlManeuverTable.MANEUVER_DEATH_TRANCE:
                [SKILL_DEATH_TRANCE, SKILL_SLEEP_TRANCE],
            SelfControlManeuverTable.MANEUVER_DRUG_TOLERANCE:
                [SKILL_DRUG_TOLERANCE, SKILL_POISON_TOLERANCE],
            SelfControlManeuverTable.MANEUVER_FRENZY:
                [SKILL_FRENZY, ],
            SelfControlManeuverTable.MANEUVER_HEALING_TRANCE:
                [SKILL_HEALING_TRANCE, SKILL_CLEANSING_TRANCE, SKILL_SLEEP_TRANCE],
            SelfControlManeuverTable.MANEUVER_MEDITATION:
                [SKILL_MEDITATION, ],
            SelfControlManeuverTable.MANEUVER_MNEMONICS:
                [SKILL_MNEMONICS, ],
            SelfControlManeuverTable.MANEUVER_POISON_TOLERANCE:
                [SKILL_POISON_TOLERANCE, SKILL_DRUG_TOLERANCE],
            SelfControlManeuverTable.MANEUVER_SLEEP_TRANCE:
                [SKILL_SLEEP_TRANCE, SKILL_CLEANSING_TRANCE, SKILL_DEATH_TRANCE],
            SelfControlManeuverTable.MANEUVER_SPELL_CONCENTRATION:
                [SKILL_SPELL_CONCENTRATION, SKILL_ADRENAL_CONCENTRATION],
            SelfControlManeuverTable.MANEUVER_STUNNED_MANEUVERING:
                [SKILL_STUNNED_MANEUVERING, ]
        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
