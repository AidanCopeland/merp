# -*- coding: utf-8 -*-
"""
The Technical/Trade/Vocational static maneuver table.

Classes:
    TechnicalTradeVocationalManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.general_skills import \
    SKILL_NAVIGATION, SKILL_PREPARING_HERBS, SKILL_HERB_LORE
from console.character.subterfuge_skills import SKILL_DUPING
from console.character.leadership_skills import \
    SKILL_LEADERSHIP_LEADERSHIP, SKILL_PUBLIC_SPEAKING_LEADERSHIP, SKILL_CONTACTING_LEADERSHIP
from console.character.secondary_skills import \
    SKILL_ADVERTISING, SKILL_ARCHITECTURE, SKILL_DRAFTING, SKILL_DIAGNOSTICS, \
    SKILL_DISCERN_WOUNDS, SKILL_DOWSING, SKILL_DROWSING, SKILL_MEDITATION, SKILL_ENGINEERING, \
    SKILL_REGION_LORE_WILD, SKILL_CULTURE_WILD, SKILL_MECHANITION, SKILL_SMITHING, \
    SKILL_MILITARY_ORGANISATION, SKILL_MINING, SKILL_SECOND_AID, SKILL_FIRST_AID, SKILL_SURGERY, \
    SKILL_ADMINISTRATION, SKILL_APPRAISAL, SKILL_EVALUATE_ARMOUR, SKILL_EVALUATE_METAL, \
    SKILL_EVALUATE_STONE, SKILL_EVALUATE_WEAPON, SKILL_BOAT_PILOT, SKILL_CARTOGRAPHY, \
    SKILL_GIMMICKRY, SKILL_HYPNOSIS, SKILL_MIDWIFERY, SKILL_ORIENTEERING, SKILL_SERVICE, \
    SKILL_SIEGE_ENGINEERING, SKILL_TACTICS

import trace_log as trace

sys.path.append('../')


class TechnicalTradeVocationalManeuverTable(StaticManeuverTable):
    """
    Technical/Trade/Vocational static maneuver table.

    Methods:
        select_technical_trade_vocational_table(maneuver_type)
    """
    MANEUVER_ADVERTISING = "Advertising"
    MANEUVER_ARCHITECTURE = "Architecture"
    MANEUVER_DIAGNOSTICS = "Diagnostics"
    MANEUVER_DOWSING = "Dowsing"
    MANEUVER_DROWSING = "Drowsing"
    MANEUVER_ENGINEERING = "Engineering"
    MANEUVER_MECHANITION = "Mechanition"
    MANEUVER_MILITARY_ORGANISATION = "Military Organisation"
    MANEUVER_MINING = "Mining"
    MANEUVER_SECOND_AID = "Second Aid"
    MANEUVER_SURGERY = "Surgery"
    MANEUVER_ADMINISTRATION = "Administration"
    MANEUVER_APPRAISAL = "Appraisal"
    MANEUVER_BOAT_PILOT = "Boat Pilot"
    MANEUVER_CARTOGRAPHY = "Cartography"
    MANEUVER_EVALUATE_ARMOUR = "Evaluate Armour"
    MANEUVER_EVALUATE_METAL = "Evaluate Metal"
    MANEUVER_EVALUATE_STONE = "Evaluate Stone"
    MANEUVER_EVALUATE_WEAPON = "Evaluate Weapon"
    MANEUVER_GIMMICKRY = "Gimmickry"
    MANEUVER_HYPNOSIS = "Hypnosis"
    MANEUVER_MIDWIFERY = "Midwifery"
    MANEUVER_NAVIGATION = "Navigation"
    MANEUVER_PREPARING_HERBS = "Preparing Herbs"
    MANEUVER_PREPARING_POISONS = "Preparing Poisons"
    MANEUVER_SERVICE = "Service"
    MANEUVER_SIEGE_ENGINEERING = "Siege Engineering"
    MANEUVER_TACTICS = "Tactics"

    maneuver_type_options = (
        MANEUVER_ADVERTISING, MANEUVER_ARCHITECTURE, MANEUVER_DIAGNOSTICS,
        MANEUVER_DOWSING, MANEUVER_DROWSING, MANEUVER_ENGINEERING,
        MANEUVER_MECHANITION, MANEUVER_MILITARY_ORGANISATION, MANEUVER_MINING,
        MANEUVER_SECOND_AID, MANEUVER_SURGERY, MANEUVER_ADMINISTRATION,
        MANEUVER_APPRAISAL, MANEUVER_BOAT_PILOT, MANEUVER_CARTOGRAPHY,
        MANEUVER_EVALUATE_ARMOUR, MANEUVER_EVALUATE_METAL, MANEUVER_EVALUATE_STONE,
        MANEUVER_EVALUATE_WEAPON, MANEUVER_GIMMICKRY, MANEUVER_HYPNOSIS,
        MANEUVER_MIDWIFERY, MANEUVER_NAVIGATION, MANEUVER_PREPARING_HERBS,
        MANEUVER_PREPARING_POISONS, MANEUVER_SERVICE, MANEUVER_SIEGE_ENGINEERING, MANEUVER_TACTICS
    )

    maneuver_result_text = {
        BLUNDER:
            "Your blatant disregard of professional methods might seem daring to some; "
            "the Guild finds if merely irresponsible and expels you, announcing your "
            "expulsion to the public.  Your work is dangerous and quickly condemned by "
            "all.  Wow.  Tough luck, dude.",
        ABSOLUTE_FAILURE:
            "Ineptitude becomes you, and you wear it like a badge while trying to "
            "complete this task.  If you are working in a professional capacity, your "
            "clients/charges are disgusted with your methods and avail themselves of "
            "your competitors.  Otherwise, you have achieved negative results with your "
            "efforts.",
        FAILURE:
            "Experience doesn't always outweigh knowledge.  You should have studied "
            "more.  You fail.",
        PARTIAL_SUCCESS:
            "To your chagrin, you will have to consult another expert.  If you are "
            "able to do so, you may try again in 24 hours to complete your task. "
            "Otherwise, you are stumped.",
        NEAR_SUCCESS:
            "Your skills in this particular area are rusty.  After 1 hour, you may roll "
            "again with a +10 modification.",
        SUCCESS:
            "Good work, Master Tradesman!  Your effort succeeds in all respects.",
        ABSOLUTE_SUCCESS:
            "The spirit of the MUse enters you, and your work achieves the status of "
            "art.  Your efficient design/work is combined with an elegance and "
            "simplicity of form that is admired even by those unlearned in the trade. "
            "You may work on similar projects at a modification of +20 (non-cumulative) "
            "until you receive a result of Absolute Failure or Blunder on this table."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 2, -20),
        ABSOLUTE_FAILURE: (-25, 1.5, -10),
        FAILURE: (0, 1.25, 0),
        PARTIAL_SUCCESS: (20, 1.5, 5),
        NEAR_SUCCESS: (80, 1.25, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (125, 1, 30)
    }

    @staticmethod
    def select_technical_trade_vocational_table():
        """
        Set the current TechnicalTradeVocational maneuver table to use.
        :return: The maneuver table.
        """
        return TechnicalTradeVocationalManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            TechnicalTradeVocationalManeuverTable.MANEUVER_ADVERTISING:
                [SKILL_ADVERTISING,
                 SKILL_DUPING,
                 SKILL_LEADERSHIP_LEADERSHIP,
                 SKILL_PUBLIC_SPEAKING_LEADERSHIP],
            TechnicalTradeVocationalManeuverTable.MANEUVER_ARCHITECTURE:
                [SKILL_ARCHITECTURE, SKILL_DRAFTING, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_DIAGNOSTICS:
                [SKILL_DIAGNOSTICS, SKILL_DISCERN_WOUNDS],
            TechnicalTradeVocationalManeuverTable.MANEUVER_DOWSING:
                [SKILL_DOWSING, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_DROWSING:
                [SKILL_DROWSING, SKILL_MEDITATION],
            TechnicalTradeVocationalManeuverTable.MANEUVER_ENGINEERING:
                [SKILL_ENGINEERING, SKILL_REGION_LORE_WILD, SKILL_CULTURE_WILD, SKILL_MECHANITION],
            TechnicalTradeVocationalManeuverTable.MANEUVER_MECHANITION:
                [SKILL_MECHANITION, SKILL_ENGINEERING, SKILL_SMITHING],
            TechnicalTradeVocationalManeuverTable.MANEUVER_MILITARY_ORGANISATION:
                [SKILL_MILITARY_ORGANISATION, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_MINING:
                [SKILL_MINING, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_SECOND_AID:
                [SKILL_SECOND_AID, SKILL_SURGERY, SKILL_FIRST_AID],
            TechnicalTradeVocationalManeuverTable.MANEUVER_SURGERY:
                [SKILL_SURGERY, SKILL_SECOND_AID],
            TechnicalTradeVocationalManeuverTable.MANEUVER_ADMINISTRATION:
                [SKILL_ADMINISTRATION, SKILL_LEADERSHIP_LEADERSHIP, SKILL_CONTACTING_LEADERSHIP],
            TechnicalTradeVocationalManeuverTable.MANEUVER_APPRAISAL:
                [SKILL_APPRAISAL,
                 SKILL_EVALUATE_ARMOUR,
                 SKILL_EVALUATE_METAL,
                 SKILL_EVALUATE_STONE,
                 SKILL_EVALUATE_WEAPON],
            TechnicalTradeVocationalManeuverTable.MANEUVER_BOAT_PILOT:
                [SKILL_BOAT_PILOT, SKILL_NAVIGATION],
            TechnicalTradeVocationalManeuverTable.MANEUVER_CARTOGRAPHY:
                [SKILL_CARTOGRAPHY, SKILL_NAVIGATION],
            TechnicalTradeVocationalManeuverTable.MANEUVER_EVALUATE_ARMOUR:
                [SKILL_EVALUATE_ARMOUR, SKILL_APPRAISAL],
            TechnicalTradeVocationalManeuverTable.MANEUVER_EVALUATE_METAL:
                [SKILL_EVALUATE_METAL, SKILL_APPRAISAL],
            TechnicalTradeVocationalManeuverTable.MANEUVER_EVALUATE_STONE:
                [SKILL_EVALUATE_STONE, SKILL_APPRAISAL],
            TechnicalTradeVocationalManeuverTable.MANEUVER_EVALUATE_WEAPON:
                [SKILL_EVALUATE_WEAPON, SKILL_APPRAISAL],
            TechnicalTradeVocationalManeuverTable.MANEUVER_GIMMICKRY:
                [SKILL_GIMMICKRY, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_HYPNOSIS:
                [SKILL_HYPNOSIS, SKILL_DUPING],
            TechnicalTradeVocationalManeuverTable.MANEUVER_MIDWIFERY:
                [SKILL_MIDWIFERY, SKILL_SECOND_AID, SKILL_SURGERY],
            TechnicalTradeVocationalManeuverTable.MANEUVER_NAVIGATION:
                [SKILL_NAVIGATION, SKILL_ORIENTEERING],
            TechnicalTradeVocationalManeuverTable.MANEUVER_PREPARING_HERBS:
                [SKILL_PREPARING_HERBS, SKILL_HERB_LORE],
            TechnicalTradeVocationalManeuverTable.MANEUVER_SERVICE:
                [SKILL_SERVICE, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_SIEGE_ENGINEERING:
                [SKILL_SIEGE_ENGINEERING, ],
            TechnicalTradeVocationalManeuverTable.MANEUVER_TACTICS:
                [SKILL_TACTICS, ]

        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
