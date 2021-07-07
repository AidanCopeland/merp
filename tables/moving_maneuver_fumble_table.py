# -*- coding: utf-8 -*-
"""
Classes handling moving maneuver fumbles.

Classes:
    FumbleResult
    MovingManeuverFumbleTable
"""
from __future__ import absolute_import
from dataclasses import dataclass
import sys
import dice
import trace_log as trace
from .tables_utils import find_merp_table_row_entry

sys.path.append('../')

ROUTINE = "Routine"
EASY = "Easy"
LIGHT = "Light"
MEDIUM = "Medium"
HARD = "Hard"
VERY_HARD = "Very Hard"
EXTREMELY_HARD = "Extremely Hard"
SHEER_FOLLY = "Sheer Folly"
ABSURD = "Absurd"

maneuver_fumble_bonuses = {
    ROUTINE: -50,
    EASY: -35,
    LIGHT: -20,
    MEDIUM: -10,
    HARD: 0,
    VERY_HARD: 5,
    EXTREMELY_HARD: 10,
    SHEER_FOLLY: 15,
    ABSURD: 20
}


@dataclass
class FumbleResult:
    """
    Fumble result class.
    """
    result1: str = ""
    result2: str = ""
    chance_worse: int = 0
    hits: int = 0
    stun: int = 0
    modifier: int = 0
    out_of_combat: bool = False
    unconscious: bool = False


fumble_table = [
    FumbleResult(result1="You hesitate and fail to act."),  # 0 - 05
    FumbleResult(result1="You have second thoughts and decide to wait one round."),  # 06 - 20
    FumbleResult(result1="You slip.  -20 from any maneuvers for 2 rounds.",  # 21 - 35
                 result2="You slip and fall.  -20 from any maneuvers for 2 rounds.",
                 chance_worse=30),
    FumbleResult(result1="You stumble.  -30 from any maneuvers for 2 rounds.",  # 36 - 50
                 result2="You stumble and fall.  -30 from any maneuvers for 2 rounds.",
                 chance_worse=45),
    FumbleResult(result1="You stub your toe.",  # 51 - 65
                 result2="You stub your toe and fall.",
                 chance_worse=60,
                 hits=3,
                 modifier=-10),
    FumbleResult(result1="You slip.",  # 66 - 79
                 result2="You slip and fall.",
                 chance_worse=75,
                 stun=2),
    FumbleResult(result1="You twist your ankle",  # 80
                 hits=5,
                 modifier=-10),
    FumbleResult(result1="You fall down.  -20 to activity for 3 rounds.",  # 81 - 86
                 hits=3),
    FumbleResult(result1="You sprain your ankle and tear some tendons.",  # 87 - 89
                 hits=7,
                 stun=3,
                 modifier=-30),
    FumbleResult(result1="Fall breaks your leg.",  # 90
                 hits=8,
                 stun=3,
                 modifier=-30),
    FumbleResult(result1="You break your wrist when you fall.",  # 91 - 96,
                 hits=12,
                 stun=2,
                 modifier=-20),
    FumbleResult(result1="Your arm breaks when you land on it.",  # 97 - 99
                 hits=14,
                 stun=4,
                 modifier=-30),
    FumbleResult(result1=
                 "In an attempt to break your fall you break both of your arms; they are useless.",
                 # 100
                 hits=30,
                 stun=6,
                 out_of_combat=True),
    FumbleResult(result1="When you fall your leg twists under you and breaks.",  # 101 - 106
                 hits=15,
                 stun=3,
                 modifier=-50),
    FumbleResult(result1="Your knee strikes a hard object and shatters as you fall.",  # 107 - 109
                 hits=10,
                 stun=4,
                 modifier=-80),
    FumbleResult(result1="You fall and the resulting concussion causes a year-long coma",
                 unconscious=True),  # 110
    FumbleResult(result1=
                 "You fall and land on your lower spine.  You are paralyzed from the waist down.",
                 # 111 - 116
                 hits=30,
                 out_of_combat=True),
    FumbleResult(result1="You fall and are paralyzed from the neck down.",  # 117 - 119
                 hits=20,
                 out_of_combat=True),
    FumbleResult(result1="Your fall turns into a dive.  You crush your skull and die.",
                 unconscious=True)  # 120
]


def resolve_moving_maneuver_fumble(roll, maneuver_difficulty):
    """
    Resolve a fumble for a moving maneuver.
    :param roll: The fumble roll made.
    :param maneuver_difficulty: The difficulty of the maneuver.
    :return: The text to return.
    """
    dice.randomize()
    resolved_roll = roll + maneuver_fumble_bonuses[maneuver_difficulty]
    resolved_roll = max(min(resolved_roll, 120), 0)
    trace.detail("Resolved roll %d" % resolved_roll)

    result = find_merp_table_row_entry(fumble_table, resolved_roll)
    roll_text = "Resolved fumble roll %d\n" % resolved_roll
    result_text = result.result1

    if result.chance_worse != 0:
        trace.flow("Chance of worse result: %d" % result.chance_worse)
        chance = dice.d100()
        trace.detail("Dice roll %d" % chance)
        if chance <= result.chance_worse:
            trace.flow("Worse result achieved")
            result_text = result.result2
    if result.hits != 0:
        result_text += "\n+%d hits." % result.hits
    if result.stun != 0:
        result_text += "\n+%d rounds stun." % result.stun
    if result.modifier != 0:
        result_text += "\n%d to activity." % result.modifier

    return roll_text + result_text
