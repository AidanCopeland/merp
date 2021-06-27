# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division

from past.utils import old_div
from Maneuvers.StaticManeuverTable import *
from tkinter import IntVar

import trace_log as trace
standard_library.install_aliases()

sys.path.append('../')

ROUNDS_PREPARED_TEXT = "Number of consecutive rounds prepared (100% activity)"
CONSECUTIVE_ROUNDS_NEEDED = 3
CONSECUTIVE_ROUNDS_BONUS = 10
MAX_PREPARATION_BONUS = 50


class SelfControlManeuverTable(StaticManeuverTable):
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
    MANEUVER_FRENZY = "Frenzy"
    MANEUVER_HEALING_TRANCE = "Healing Trance"
    MANEUVER_MEDITATION = "Meditation"
    MANEUVER_MNEMONICS = "Mnemonics"
    MANEUVER_SLEEP_TRANCE = "Sleep Trance"
    MANEUVER_SPELL_CONCENTRATION = "Spell Concentration"
    MANEUVER_STUNNED_MANEUVERING = "Stunned Maneuvering"

    maneuver_type_options = (
        MANEUVER_ADRENAL_BALANCE, MANEUVER_ADRENAL_CONCENTRATION, MANEUVER_ADRENAL_LANDING,
        MANEUVER_ADRENAL_LEAPING, MANEUVER_ADRENAL_QUICKDRAW, MANEUVER_ADRENAL_SPEED,
        MANEUVER_ADRENAL_STABILIZATION, MANEUVER_ADRENAL_STRENGTH, MANEUVER_CLEANSING_TRANCE,
        MANEUVER_CONTROL_LYCANTHROPY, MANEUVER_DEATH_TRANCE, MANEUVER_FRENZY,
        MANEUVER_HEALING_TRANCE, MANEUVER_MEDITATION, MANEUVER_MNEMONICS,
        MANEUVER_SLEEP_TRANCE, MANEUVER_SPELL_CONCENTRATION, MANEUVER_STUNNED_MANEUVERING
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
        ABSOLUTE_FAILURE: (-0, 1, -25),
        FAILURE: (0, 1, -5),
        PARTIAL_SUCCESS: (30, 0.5, 0),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.1, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super(StaticManeuverTable, self).__init__(**kwargs)
        self.rounds_prepared = IntVar()

        trace.exit()

    @staticmethod
    def select_self_control_table(maneuver_type):
        """
        Set the current SelfControl maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        trace.entry()

        from Maneuvers.CombatManeuvers.QuickdrawManeuverTable import QuickdrawManeuverTable
        from Maneuvers.SelfControl.AdrenalStablizationManeuverTable import AdrenalStabilizationManeuverTable
        from Maneuvers.SelfControl.AdrenalStrengthManeuverTable import AdrenalStrengthManeuverTable
        from Maneuvers.SelfControl.ControlLycanthropyManeuverTable import ControlLycanthropyManeuverTable
        from Maneuvers.SelfControl.MeditationManeuverTable import MeditationManeuverTable
        from Maneuvers.SelfControl.MnemonicsManeuverTable import MnemonicsManeuverTable
        from Maneuvers.SelfControl.SpellConcentrationManeuverTable import SpellConcentrationManeuverTable
        from Maneuvers.SelfControl.StunnedManeuveringManeuverTable import StunnedManeuveringManeuverTable

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
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_MEDITATION:
            trace.flow("Meditation maneuver")
            trace.exit()
            return MeditationManeuverTable()
        elif maneuver_type == SelfControlManeuverTable.MANEUVER_MNEMONICS:
            trace.flow("Mnemonics maneuver")
            trace.exit()
            return MnemonicsManeuverTable()
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
            FrameUtils.setup_entry_frame(parent_frame, ROUNDS_PREPARED_TEXT, self.rounds_prepared)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
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
