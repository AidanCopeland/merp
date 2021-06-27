# -*- coding: utf-8 -*-
import sys
import trace_log as trace
from Maneuvers.CombatManeuversManeuverTable import CombatManeuversManeuverTable
from Maneuvers.StaticManeuverTable import BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS

sys.path.append('../')


class QuickdrawManeuverTable(CombatManeuversManeuverTable):
    speed_effect_text = {
        BLUNDER:
            "Take an additional -5 initiative penalty this round.",
        ABSOLUTE_FAILURE:
            "Take an additional -2 initiative penalty this round.",
        FAILURE:
            "Take an additional -1 initiative penalty this round.",
        PARTIAL_SUCCESS:
            "",
        NEAR_SUCCESS:
            "Reduce your initiative penalty to -1 and your OB penalty to -10 (instead of -3 and -30).",
        SUCCESS:
            "Remove all penalties and act normally this round.",
        ABSOLUTE_SUCCESS:
            "Remove all penalties and take a +2 initiative bonus this round."
    }

    maneuver_result_stats = {
        BLUNDER: (0, 1, -30),
        ABSOLUTE_FAILURE: (0, 1, -15),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (100, 1, 5),
        NEAR_SUCCESS: (100, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (100, 1, 30)
    }

    def result_text(self, result):
        """
        Return additional text to report for the maneuver result.
        :param result: The type of result achieved.
        """
        trace.detail("Result is %s" % result)

        result_text = self.maneuver_result_text[result]
        speed_effect_text = self.speed_effect_text[result]

        return result_text + "\n\n" + speed_effect_text
