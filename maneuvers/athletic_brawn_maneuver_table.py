# -*- coding: utf-8 -*-
"""
The Athletic/Brawn static maneuver table.

Classes:
    AthleticBrawnManeuverTable
"""
from __future__ import absolute_import
import sys
from tkinter import IntVar

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from maneuvers import maneuver_utils
from console.character.secondary_skills import \
    SKILL_ATHLETIC_GAMES, SKILL_JUMPING, SKILL_WEIGHT_LIFTING
from console.character.weapon_skills import \
    SKILL_POWER_STRIKING, SKILL_POWER_THROWING, SKILL_ADRENAL_STRENGTH

import trace_log as trace


sys.path.append('../')

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


# noinspection SpellCheckingInspection
class AthleticBrawnManeuverTable(StaticManeuverTable):
    """
    Athletic/Brawn static maneuver table.

    Methods:
        select_athletic_brawn_table(maneuver_type)
        setup_maneuver_table_frames(self, parent_frame)
        table_bonus(self)
    """
    MANEUVER_ATHLETIC_GAMES_BRAWN = "Athletic Games (Brawn)"
    MANEUVER_JUMPING = "Jumping"
    MANEUVER_POWER_STRIKING = "Power-striking"
    MANEUVER_POWER_THROWING = "Power-throwing"
    MANEUVER_WEIGHT_LIFTING = "Weight-lifting"

    maneuver_type_options = (
        MANEUVER_ATHLETIC_GAMES_BRAWN, MANEUVER_JUMPING, MANEUVER_POWER_STRIKING,
        MANEUVER_POWER_THROWING, MANEUVER_WEIGHT_LIFTING
    )

    maneuver_result_text = {
        BLUNDER:
            "Agony!  Mere strength cannot overcome bad leverage; you may have snapped a bone or "
            "severed a muscle; take a 'B' Crush or Slash critical and add 5 rounds of stun. You "
            "will operate at a -25 modification (-50 to this skill) until this ""Medium"" injury "
            "has fully healed.  "
            "You failed the maneuver, by the way.",
        ABSOLUTE_FAILURE:
            "Sloppy, sloppy... you planted poorly and pulled a muscle; you will operate at a -20 "
            "modification (-40 to this skill) until this ""Light"" injury has fully healed.  Oh, "
            "and you failed.",
        FAILURE:
            "Who are you trying to impress?  You just sound constipated.  You failed your "
            "maneuver.",
        PARTIAL_SUCCESS:
            "You have potential... perhaps some kind of training regimen...? "
            "Might solve that sand-in-the-face problem...",
        NEAR_SUCCESS:
            "Argh, so close!  If appropriate, you may make a roll to finish the maneuver next "
            "round at a +10 modification.",
        SUCCESS:
            "Unnff!  Ah, nice work!  Your mighty thews have carried the day.  You feel the burn.",
        ABSOLUTE_SUCCESS:
            "You have a place waiting for you at the circus, Herc."
    }

    maneuver_result_stats = {
        BLUNDER: (5, 1.5, -25),
        ABSOLUTE_FAILURE: (10, 1.2, -15),
        FAILURE: (15, 1, -10),
        PARTIAL_SUCCESS: (30, 1, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.equipment_bonus = IntVar()

        trace.exit()

    @staticmethod
    def select_athletic_brawn_table(maneuver_type):
        """
        Set the current athletic/brawn maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.athletic_brawn.jumping_maneuver_table import JumpingManeuverTable
        from maneuvers.athletic_brawn.power_striking_maneuver_table import \
            PowerStrikingManeuverTable
        from maneuvers.athletic_brawn.power_throwing_maneuver_table import \
            PowerThrowingManeuverTable
        from maneuvers.athletic_brawn.weight_lifting_maneuver_table import \
            WeightLiftingManeuverTable

        if maneuver_type == AthleticBrawnManeuverTable.MANEUVER_ATHLETIC_GAMES_BRAWN:
            trace.flow("Athletic Games maneuver")
            trace.exit()
            return AthleticBrawnManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_JUMPING:
            trace.flow("Jumping maneuver")
            trace.exit()
            return JumpingManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_POWER_STRIKING:
            trace.flow("Power-striking maneuver")
            trace.exit()
            return PowerStrikingManeuverTable()

        elif maneuver_type == AthleticBrawnManeuverTable.MANEUVER_POWER_THROWING:
            trace.flow("Power-throwing maneuver")
            trace.exit()
            return PowerThrowingManeuverTable()

        else:
            trace.flow("Weight-lifting maneuver")
            assert maneuver_type == AthleticBrawnManeuverTable.MANEUVER_WEIGHT_LIFTING
            trace.exit()
            return WeightLiftingManeuverTable()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """
        maneuver_utils.setup_maneuver_table_frames_for_equipment(self, parent_frame)

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        return maneuver_utils.table_bonus_from_equipment(self)

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            AthleticBrawnManeuverTable.MANEUVER_ATHLETIC_GAMES_BRAWN: [SKILL_ATHLETIC_GAMES, ],
            AthleticBrawnManeuverTable.MANEUVER_JUMPING: [SKILL_JUMPING, ],
            AthleticBrawnManeuverTable.MANEUVER_POWER_STRIKING:
                [SKILL_POWER_STRIKING, SKILL_ADRENAL_STRENGTH],
            AthleticBrawnManeuverTable.MANEUVER_POWER_THROWING:
                [SKILL_POWER_THROWING, SKILL_ADRENAL_STRENGTH],
            AthleticBrawnManeuverTable.MANEUVER_WEIGHT_LIFTING: [SKILL_WEIGHT_LIFTING]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
