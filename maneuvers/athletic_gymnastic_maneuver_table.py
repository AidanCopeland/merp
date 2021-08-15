# -*- coding: utf-8 -*-
"""
The Athletic/Gymnastics static maneuver table.

Classes:
    AthleticGymnasticsManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.secondary_skills import \
    SKILL_ATHLETIC_GAMES, SKILL_CONTORTIONS, SKILL_JUGGLING, SKILL_TUMBLING
from console.character.general_skills import \
    SKILL_ACROBATICS, SKILL_CLIMB, SKILL_DIVING, SKILL_POLE_VAULTING, SKILL_RAPPELLING, \
    SKILL_TIGHTROPE_WALKING, SKILL_SWIM

import trace_log as trace

sys.path.append('../')


class AthleticGymnasticsManeuverTable(StaticManeuverTable):
    """
    Athletic/Gymnastics static maneuver table.

    Methods:
        select_athletic_endurance_table(maneuver_type)
    """
    MANEUVER_ACROBATICS = "Acrobatics"
    MANEUVER_ATHLETIC_GAMES_GYMNASTICS = "Athletic Games (Gymnastics)"
    MANEUVER_CLIMBING = "Climbing"
    MANEUVER_CONTORTIONS = "Contortions"
    MANEUVER_DIVING = "Diving"
    MANEUVER_FLYING_GLIDING = "Flying/Gliding"
    MANEUVER_JUGGLING = "Juggling"
    MANEUVER_POLE_VAULTING = "Pole-vaulting"
    MANEUVER_RAPPELLING = "Rappelling"
    MANEUVER_SKATING = "Skating"
    MANEUVER_SKIING = "Skiing"
    MANEUVER_STILT_WALKING = "Stilt-walking"
    MANEUVER_SURFING = "Surfing"
    MANEUVER_TIGHTROPE_WALKING = "Tightrope-walking"
    MANEUVER_TUMBLING = "Tumbling"

    maneuver_type_options = (
        MANEUVER_ACROBATICS, MANEUVER_ATHLETIC_GAMES_GYMNASTICS, MANEUVER_CLIMBING,
        MANEUVER_CONTORTIONS, MANEUVER_DIVING, MANEUVER_FLYING_GLIDING, MANEUVER_JUGGLING,
        MANEUVER_POLE_VAULTING, MANEUVER_RAPPELLING, MANEUVER_SKATING, MANEUVER_SKIING,
        MANEUVER_STILT_WALKING, MANEUVER_SURFING, MANEUVER_TIGHTROPE_WALKING, MANEUVER_TUMBLING
    )

    # noinspection SpellCheckingInspection
    maneuver_result_text = {
        BLUNDER:
            "In your zeal, you have forgotten to fully warm up.  You severely pull a major muscle "
            "group in the middle of your maneuver, inflicting a ""Medium"" Muscle wound (with a "
            "-30 penalty) and two rounds of stun (from the pain).  Yer goin' down, buddy!",
        ABSOLUTE_FAILURE:
            "Poor judgement yields poor control.  You slip and fall to the ground, taking damage "
            "commensurate with the distance fallen.",
        FAILURE:
            "You freeze at the critical moment, failing your maneuver.  If appropriate, you may "
            "roll on the General Static Maneuver Table with a +20 modification to abort your "
            "maneuver in time.  "
            "Otherwise, you take your chances like the rest of us.",
        PARTIAL_SUCCESS:
            "And everything was going so well... you cannot seem to follow through, and it is "
            "going to take longer than you thought to get this maneuver back under control...",
        NEAR_SUCCESS:
            "You are seeming inches from your goal... if appropriate, you may roll again next "
            "round at a +10 modification to complete your maneuver.",
        SUCCESS:
            "Fancy footwork, my friend!  You complete your maneuver in fine form.",
        ABSOLUTE_SUCCESS:
            "You barely broke a sweat.  Must be the shoes."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 1.5, -20),
        ABSOLUTE_FAILURE: (10, 1.5, -10),
        FAILURE: (0, 1.25, 0),
        PARTIAL_SUCCESS: (20, 2, 5),
        NEAR_SUCCESS: (80, 0.8, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_athletic_gymnastics_table(maneuver_type):
        """
        Set the current athletic/gymnastics maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=too-many-branches
        # pylint: disable=too-many-statements
        # pylint: disable=too-many-return-statements
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.moving_maneuver_table import MovingManeuverTable
        from maneuvers.athletic_gymnastics.contortions_maneuver_table import \
            ContortionsManeuverTable
        from maneuvers.athletic_gymnastics.juggling_maneuver_table import JugglingManeuverTable
        from maneuvers.athletic_gymnastics.pole_vaulting_maneuver_table import \
            PoleVaultingManeuverTable
        from maneuvers.athletic_gymnastics.rappelling_maneuver_table import RappellingManeuverTable
        from maneuvers.athletic_gymnastics.tightrope_walking_maneuver_table import \
            TightropeWalkingManeuverTable

        if maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_ACROBATICS:
            trace.flow("Acrobatics maneuver")
            trace.exit()
            return AthleticGymnasticsManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_ATHLETIC_GAMES_GYMNASTICS:
            trace.flow("Athletic Games maneuver")
            trace.exit()
            return AthleticGymnasticsManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_CLIMBING:
            trace.flow("Climbing maneuver")
            trace.exit()
            return MovingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_CONTORTIONS:
            trace.flow("Contortions maneuver")
            trace.exit()
            return ContortionsManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_DIVING:
            trace.flow("Diving maneuver")
            trace.exit()
            return AthleticGymnasticsManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_FLYING_GLIDING:
            trace.flow("Flying/Gliding maneuver")
            trace.exit()
            return MovingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_JUGGLING:
            trace.flow("Juggling maneuver")
            trace.exit()
            return JugglingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_POLE_VAULTING:
            trace.flow("Pole vaulting maneuver")
            trace.exit()
            return PoleVaultingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_RAPPELLING:
            trace.flow("Rappelling maneuver")
            trace.exit()
            return RappellingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_SKATING:
            trace.flow("Skating maneuver")
            trace.exit()
            return MovingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_SKIING:
            trace.flow("Skiing maneuver")
            trace.exit()
            return MovingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_STILT_WALKING:
            trace.flow("Stilt-walking maneuver")
            trace.exit()
            return MovingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_SURFING:
            trace.flow("Surfing maneuver")
            trace.exit()
            return MovingManeuverTable()

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_TIGHTROPE_WALKING:
            trace.flow("Tightrope-walking maneuver")
            trace.exit()
            return TightropeWalkingManeuverTable()

        else:
            trace.flow("Tumbling maneuver")
            assert maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_TUMBLING
            trace.exit()
            return AthleticGymnasticsManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            AthleticGymnasticsManeuverTable.MANEUVER_ACROBATICS:
                [SKILL_ACROBATICS, ],
            AthleticGymnasticsManeuverTable.MANEUVER_ATHLETIC_GAMES_GYMNASTICS:
                [SKILL_ATHLETIC_GAMES, ],
            AthleticGymnasticsManeuverTable.MANEUVER_CONTORTIONS:
                [SKILL_CONTORTIONS, SKILL_ACROBATICS, ],
            AthleticGymnasticsManeuverTable.MANEUVER_DIVING:
                [SKILL_DIVING, SKILL_SWIM, ],
            AthleticGymnasticsManeuverTable.MANEUVER_JUGGLING:
                [SKILL_JUGGLING, SKILL_ACROBATICS],
            AthleticGymnasticsManeuverTable.MANEUVER_POLE_VAULTING:
                [SKILL_POLE_VAULTING, SKILL_CLIMB, ],
            AthleticGymnasticsManeuverTable.MANEUVER_RAPPELLING:
                [SKILL_RAPPELLING, SKILL_CLIMB],
            AthleticGymnasticsManeuverTable.MANEUVER_TIGHTROPE_WALKING:
                [SKILL_TIGHTROPE_WALKING, SKILL_ACROBATICS],
            AthleticGymnasticsManeuverTable.MANEUVER_TUMBLING:
                [SKILL_TIGHTROPE_WALKING, SKILL_ACROBATICS]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
