# -*- coding: utf-8 -*-
import sys

from StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')


class AthleticGymnasticsManeuverTable(StaticManeuverTable):
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
        MANEUVER_ACROBATICS, MANEUVER_ATHLETIC_GAMES_GYMNASTICS, MANEUVER_CLIMBING, MANEUVER_CONTORTIONS,
        MANEUVER_DIVING, MANEUVER_FLYING_GLIDING, MANEUVER_JUGGLING, MANEUVER_POLE_VAULTING,
        MANEUVER_RAPPELLING, MANEUVER_SKATING, MANEUVER_SKIING, MANEUVER_STILT_WALKING, MANEUVER_SURFING,
        MANEUVER_TIGHTROPE_WALKING, MANEUVER_TUMBLING
    )

    maneuver_result_text = {
        BLUNDER: "In your zeal, you have forgotten to fully warm up.  You severely pull a major muscle group in the "
                 "middle of your maneuver, inflicting a ""Medium"" Muscle wound (with a -30 penalty) and two rounds of "
                 "stun (from the pain).  Yer goin' down, buddy!",
        ABSOLUTE_FAILURE: "Poor judgement yields poor control.  You slip and fall to the ground, taking damage "
                          "commensurate with the distance fallen.",
        FAILURE: "You freeze at the critical moment, failing your maneuver.  "
                 "If appropriate, you may roll on the General Static Maneuver Table with a +20 modification to abort "
                 "your maneuver in time."
                 "Otherwise, you take your chances lik the rest of us.",
        PARTIAL_SUCCESS: "And everything was going so well... you cannot seem to follow through, and it is going to "
                         "take longer than you thought to get this maneuver back under control...",
        NEAR_SUCCESS: "You are seeming inches from your goal... if appropriate, you may roll again next round at a +10 "
                      "modification to complete your maneuver.",
        SUCCESS: "Fancy footwork, my friend!  You complete your maneuver in fine form.",
        ABSOLUTE_SUCCESS: "You barely broke a sweat.  Must be the shoes."
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
        from Maneuvers.MovingManeuverTable import MovingManeuverTable
        from Maneuvers.AthleticGymnastics.ContortionsManeuverTable import ContortionsManeuverTable
        from Maneuvers.AthleticGymnastics.JugglingManeuverTable import JugglingManeuverTable
        from Maneuvers.AthleticGymnastics.PoleVaultingManeuverTable import PoleVaultingManeuverTable
        from Maneuvers.AthleticGymnastics.RappellingManeuverTable import RappellingManeuverTable
        from Maneuvers.AthleticGymnastics.TightropeWalkingManeuverTable import TightropeWalkingManeuverTable

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

        elif maneuver_type == AthleticGymnasticsManeuverTable.MANEUVER_TUMBLING:
            trace.flow("Tumbling maneuver")
            trace.exit()
            return AthleticGymnasticsManeuverTable()

