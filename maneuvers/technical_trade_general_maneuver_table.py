# -*- coding: utf-8 -*-
"""
The Technical/Trade/General static maneuver table.

Classes:
    TechnicalTradeGeneralManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.general_skills import \
    SKILL_NAVIGATION, SKILL_SAILING, SKILL_ROWING, SKILL_HERB_LORE, SKILL_PREPARING_HERBS
from console.character.leadership_skills import SKILL_DIPLOMACY
from console.character.secondary_skills import \
    SKILL_BEGGING, SKILL_FIRST_AID, SKILL_DISCERN_WOUNDS, SKILL_GAMBLING, SKILL_MAPPING, \
    SKILL_OPERATING_EQUIPMENT, SKILL_ORIENTEERING, SKILL_TACTICAL_GAMES, SKILL_USING_PREPARED_HERBS

import trace_log as trace

sys.path.append('../')


class TechnicalTradeGeneralManeuverTable(StaticManeuverTable):
    """
    Technical/Trade/General static maneuver table.

    Methods:
        select_technical_trade_table(maneuver_type)
    """
    MANEUVER_BEGGING = "Begging"
    MANEUVER_FIRST_AID = "First Aid"
    MANEUVER_GAMBLING = "Gambling"
    MANEUVER_MAPPING = "Mapping"
    MANEUVER_OPERATING_EQUIPMENT = "Operating Equipment"
    MANEUVER_ORIENTEERING = "Orienteering"
    MANEUVER_SAILING = "Sailing"
    MANEUVER_TACTICAL_GAMES = "Tactical Games"
    MANEUVER_USE_PREPARED_HERBS = "Use Prepared Herbs"

    maneuver_type_options = (
        MANEUVER_BEGGING, MANEUVER_FIRST_AID, MANEUVER_GAMBLING,
        MANEUVER_MAPPING, MANEUVER_OPERATING_EQUIPMENT, MANEUVER_ORIENTEERING,
        MANEUVER_SAILING, MANEUVER_TACTICAL_GAMES, MANEUVER_USE_PREPARED_HERBS
    )

    maneuver_result_text = {
        BLUNDER:
            "You manage to ruin the tools of your trade through carelessness and "
            "frustration.  Your fumbling hands also inflict an 'A' Critical of an "
            "appropriate type upon your person.  Is this your idea of fun?",
        ABSOLUTE_FAILURE:
            "You perform with uncharacteristic nervousness that is obvious to all.  "
            "If the reaction of others is significant in your work, those reactions "
            "are modified by -30.  Your failure is on display.",
        FAILURE:
            "This is just not going to work.  You realize you will be unable to "
            "accomplish this task after half of the initial time estimate has passed. "
            "No wonder you're just a journeyman.",
        PARTIAL_SUCCESS:
            "Unusual complications have arisen.  Nothing you can't handle... but it's "
            "going to take some time.  You may attempt to finish your work after "
            "spending a time period equal to twice the initial estimate.",
        NEAR_SUCCESS:
            "This project is taking too much time... but you can't quit now.  You may "
            "make another attempt with a +10 modification after a round.",
        SUCCESS:
            "You perform your task with admirable skill.  Now quit patting yourself on "
            "the back and get back to work.",
        ABSOLUTE_SUCCESS:
            "Your subtle mastery of your trade is reflected in your remarkable success "
            "and you receive favourable reactions to your work.  You may perform this "
            "specific activity at a modification of +20 (non-cumulative) until you "
            "receive a result of Absolute Failure or Blunder."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -20),
        ABSOLUTE_FAILURE: (-20, 1, -10),
        FAILURE: (0, 0.5, 0),
        PARTIAL_SUCCESS: (20, 3, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_technical_trade_general_table():
        """
        Set the current TechnicalTradeGeneral maneuver table to use.
        :return: The maneuver table.
        """
        return TechnicalTradeGeneralManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            TechnicalTradeGeneralManeuverTable.MANEUVER_BEGGING:
                [SKILL_BEGGING, SKILL_DIPLOMACY],
            TechnicalTradeGeneralManeuverTable.MANEUVER_FIRST_AID:
                [SKILL_FIRST_AID, SKILL_DISCERN_WOUNDS],
            TechnicalTradeGeneralManeuverTable.MANEUVER_GAMBLING:
                [SKILL_GAMBLING, ],
            TechnicalTradeGeneralManeuverTable.MANEUVER_MAPPING:
                [SKILL_MAPPING, SKILL_NAVIGATION],
            TechnicalTradeGeneralManeuverTable.MANEUVER_OPERATING_EQUIPMENT:
                [SKILL_OPERATING_EQUIPMENT, ],
            TechnicalTradeGeneralManeuverTable.MANEUVER_ORIENTEERING:
                [SKILL_ORIENTEERING, SKILL_NAVIGATION],
            TechnicalTradeGeneralManeuverTable.MANEUVER_SAILING:
                [SKILL_SAILING, SKILL_ROWING],
            TechnicalTradeGeneralManeuverTable.MANEUVER_TACTICAL_GAMES:
                [SKILL_TACTICAL_GAMES, ],
            TechnicalTradeGeneralManeuverTable.MANEUVER_USE_PREPARED_HERBS:
                [SKILL_USING_PREPARED_HERBS, SKILL_HERB_LORE, SKILL_PREPARING_HERBS]
        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
