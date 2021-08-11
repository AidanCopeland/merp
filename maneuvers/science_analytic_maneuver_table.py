# -*- coding: utf-8 -*-
"""
The Science/Analytic static maneuver table.

Classes:
    ScienceAnalyticManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.secondary_skills import \
    SKILL_MATHS, SKILL_SCIENTIFIC_RESEARCH, SKILL_ANTHROPOLOGY, SKILL_ALCHEMY, SKILL_ASTRONOMY, \
    SKILL_BIOCHEMISTRY, SKILL_PSYCHOLOGY
from console.character.magical_skills import SKILL_SANITY_HEALING
import trace_log as trace

sys.path.append('../')


class ScienceAnalyticManeuverTable(StaticManeuverTable):
    """
    Science/Analytic static maneuver table.

    Methods:
        select_science_analytic_table(maneuver_type)
    """
    MANEUVER_MATHEMATICS = "Mathematics"
    MANEUVER_RESEARCH = "Research"
    MANEUVER_ANTHROPOLOGY = "Anthropology"
    MANEUVER_ALCHEMY = "Alchemy"
    MANEUVER_ASTRONOMY = "Astronomy"
    MANEUVER_BIOCHEMISTRY = "Biochemistry"
    MANEUVER_PSYCHOLOGY = "Psychology"
    MANEUVER_SANITY_HEALING = "Sanity Healing"

    maneuver_type_options = (
        MANEUVER_MATHEMATICS, MANEUVER_RESEARCH, MANEUVER_ANTHROPOLOGY,
        MANEUVER_ALCHEMY, MANEUVER_ASTRONOMY, MANEUVER_BIOCHEMISTRY,
        MANEUVER_PSYCHOLOGY, MANEUVER_SANITY_HEALING
    )

    maneuver_result_text = {
        BLUNDER:
            "Pitiful.  YOu not only fail to produce accurate results, your analysis "
            "produces _wrong_ results.  Even if you recognise that the results are "
            "wrong, you cannot for the life of you discover where you made your "
            "mistake.  You may not attempt this task again until you have increased "
            "your rank in this skill.",
        ABSOLUTE_FAILURE:
            "You utterly fail to grasp the basic concept.  Any time you have spent is "
            "wasted.  Double the basic time required for this task.  You may not "
            "attempt again until at least 24 hours have passed.",
        FAILURE:
            "This stuff is _way_ over your head.  You fail to achieve at least "
            "satisfactory results and may not attempt again until at least 24 hours "
            "have passed.  Perhaps you should try something in the service industry...",
        PARTIAL_SUCCESS:
            "Persistence yields results.  So persist.",
        NEAR_SUCCESS:
            "This was tougher than it looked at first.  You thought you'd be done by "
            "now, but in fact, you've only completed 70% of the job.  Continue your "
            "research by spending another 50% of the original time and roll again with "
            "a +10 modification.",
        SUCCESS:
            "100% success!  You've properly analysed the material and arrived at what "
            "you're sure is the right answer.  Pretty sure.  No, it's right.  Almost "
            "certainly right...",
        ABSOLUTE_SUCCESS:
            "Your seldom-appreciated genius rises to the fore.  You power through your "
            "analysis in but 70% of the time normally required.  In addition, you now "
            "hold a command of the material that will yield a +15 modification (non-"
            "cumulative) to future attempts about this specific topic."
    }

    maneuver_result_stats = {
        BLUNDER: (-150, 2, -30),
        ABSOLUTE_FAILURE: (-100, 2, -15),
        FAILURE: (10, 1.5, 0),
        PARTIAL_SUCCESS: (30, 1, 10),
        NEAR_SUCCESS: (70, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (130, 0.7, 35)
    }

    @staticmethod
    def select_science_analytic_table(maneuver_type):
        """
        Set the current ScienceAnalytic maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.science_analytic.alchemy_maneuver_table import AlchemyManeuverTable
        from maneuvers.science_analytic.psychology_maneuver_table import PsychologyManeuverTable

        if maneuver_type == ScienceAnalyticManeuverTable.MANEUVER_ALCHEMY:
            trace.flow("Alchemy maneuver")
            trace.exit()
            return AlchemyManeuverTable()
        elif maneuver_type == ScienceAnalyticManeuverTable.MANEUVER_PSYCHOLOGY:
            trace.flow("Psychology maneuver")
            trace.exit()
            return PsychologyManeuverTable()
        else:
            trace.flow("Other maneuver")
            return ScienceAnalyticManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            ScienceAnalyticManeuverTable.MANEUVER_ALCHEMY:
                [SKILL_ALCHEMY, ],
            ScienceAnalyticManeuverTable.MANEUVER_MATHEMATICS:
                [SKILL_MATHS, ],
            ScienceAnalyticManeuverTable.MANEUVER_RESEARCH:
                [SKILL_SCIENTIFIC_RESEARCH, ],
            ScienceAnalyticManeuverTable.MANEUVER_ANTHROPOLOGY:
                [SKILL_ANTHROPOLOGY, ],
            ScienceAnalyticManeuverTable.MANEUVER_ASTRONOMY:
                [SKILL_ASTRONOMY, ],
            ScienceAnalyticManeuverTable.MANEUVER_BIOCHEMISTRY:
                [SKILL_BIOCHEMISTRY, ],
            ScienceAnalyticManeuverTable.MANEUVER_PSYCHOLOGY:
                [SKILL_PSYCHOLOGY, ],
            ScienceAnalyticManeuverTable.MANEUVER_SANITY_HEALING:
                [SKILL_SANITY_HEALING, ]
        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
