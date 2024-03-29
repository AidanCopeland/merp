# -*- coding: utf-8 -*-
"""
The Influence static maneuver table.

Classes:
    InfluenceManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.subterfuge_skills import SKILL_BRIBERY, SKILL_DUPING, SKILL_INTERROGATION
from console.character.leadership_skills import \
    SKILL_DIPLOMACY, SKILL_LEADERSHIP_LEADERSHIP, SKILL_PUBLIC_SPEAKING_LEADERSHIP
from console.character.secondary_skills import \
    SKILL_PROPAGANDA, SKILL_SEDUCTION, SKILL_TRADING, SKILL_TRADING_LORE
import trace_log as trace

sys.path.append('../')


class InfluenceManeuverTable(StaticManeuverTable):
    """
    influence static maneuver table.

    Methods:
        select_influence_table(maneuver_type)
    """
    MANEUVER_BRIBERY = "Bribery"
    MANEUVER_DIPLOMACY = "Diplomacy"
    MANEUVER_DUPING = "Duping"
    MANEUVER_INTERROGATION = "Interrogation"
    MANEUVER_LEADERSHIP = "Leadership"
    MANEUVER_PROPAGANDA = "Propaganda"
    MANEUVER_PUBLIC_SPEAKING = "Public Speaking"
    MANEUVER_SEDUCTION = "Seduction"
    MANEUVER_TRADING = "Trading"

    maneuver_type_options = (
        MANEUVER_BRIBERY, MANEUVER_DIPLOMACY, MANEUVER_DUPING,
        MANEUVER_INTERROGATION, MANEUVER_LEADERSHIP, MANEUVER_PROPAGANDA,
        MANEUVER_PUBLIC_SPEAKING, MANEUVER_SEDUCTION, MANEUVER_TRADING
    )

    maneuver_result_text = {
        BLUNDER:
            "You've tried your tricks on the wrong person, this time.  The worst possible "
            "reaction will be engendered in your target(s), and violence is a distinct "
            "possibility.  With any luck, you'll just be arrested...",
        ABSOLUTE_FAILURE:
            "Your clumsy attempts at manipulation are transparent to all.  The GM should "
            "roll for the reaction of the target(s), modified by -30.  Any future attempt "
            "to influence this target will fail unless a result of _Absolute Success_ is "
            "achieved.",
        FAILURE:
            "You fail to influence your target in the least.  Your target may make a "
            "maneuver (open-ended roll modified by IT stat bonus) to note your attempt.",
        PARTIAL_SUCCESS:
            "You were doing great until you got impatient.  You cut to the chase too soon, "
            "and your target is wary.  If appropriate, roll again on this table next round "
            "with a -10 modification.",
        NEAR_SUCCESS:
            "It's taken longer than you had hoped, but you've almost successfully "
            "influenced your target.  If appropriate, roll again next round with a +10 "
            "modification.",
        SUCCESS:
            "Oh ye of the silver tongue!  You smooth-talk your target into tractability.  "
            "Have you considered a career in politics?",
        ABSOLUTE_SUCCESS:
            "You must have been an incubus in a former life.  In any case, you have your "
            "target(s) wrapped around your little finger, and any reactions are modified "
            "by +30 in your favour.  This might be a good time to ask about that raise..."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 1.5, -30),
        ABSOLUTE_FAILURE: (-25, 1.2, -10),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (30, 1, 0),
        NEAR_SUCCESS: (80, 1.5, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_influence_table(maneuver_type):
        """
        Set the current influence maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.influence.interrogation_maneuver_table import InterrogationManeuverTable

        if maneuver_type == InfluenceManeuverTable.MANEUVER_INTERROGATION:
            trace.flow("Interrogation maneuver")
            trace.exit()
            return InterrogationManeuverTable()
        else:
            return InfluenceManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            InfluenceManeuverTable.MANEUVER_BRIBERY:
                [SKILL_BRIBERY, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_DIPLOMACY:
                [SKILL_DIPLOMACY, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_DUPING:
                [SKILL_DUPING, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_INTERROGATION:
                [SKILL_INTERROGATION, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_LEADERSHIP:
                [SKILL_LEADERSHIP_LEADERSHIP, ],
            InfluenceManeuverTable.MANEUVER_PROPAGANDA:
                [SKILL_PROPAGANDA, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_PUBLIC_SPEAKING:
                [SKILL_PUBLIC_SPEAKING_LEADERSHIP, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_SEDUCTION:
                [SKILL_SEDUCTION, SKILL_LEADERSHIP_LEADERSHIP],
            InfluenceManeuverTable.MANEUVER_TRADING:
                [SKILL_TRADING, SKILL_TRADING_LORE]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
