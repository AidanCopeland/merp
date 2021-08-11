# -*- coding: utf-8 -*-
"""
The Urban static maneuver table.

Classes:
    UrbanManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.general_skills import SKILL_FORAGING
from console.character.subterfuge_skills import \
    SKILL_CONTACTING_SUBTERFUGE, SKILL_STREETWISE, SKILL_STALK_HIDE
from console.character.secondary_skills import SKILL_MINGLING, SKILL_SCROUNGING

import trace_log as trace

sys.path.append('../')


class UrbanManeuverTable(StaticManeuverTable):
    """
    Urban static maneuver table.

    Methods:
        select_urban_table(maneuver_type)
    """
    MANEUVER_CONTACTING = "Contacting"
    MANEUVER_MINGLING = "Mingling"
    MANEUVER_SCROUNGING = "Scrounging"
    MANEUVER_STREETWISE = "Streetwise"

    maneuver_type_options = (
        MANEUVER_CONTACTING, MANEUVER_MINGLING, MANEUVER_SCROUNGING, MANEUVER_STREETWISE
    )

    maneuver_result_text = {
        BLUNDER:
            "You have blundered badly, alienating your contacts and sources in this "
            "area.  If they are inclined to violence, they will be so disposed towards "
            "you.  Otherwise, they will hinder you when it is convenient to them, "
            "although they will not go out of their way to make your life miserable. "
            "What did you say, anyway?",
        ABSOLUTE_FAILURE:
            "Bad luck.  Someone has recognised you from other circumstances... ones you "
            "would rather not have brought up just now.  Any attempt to extricate "
            "yourself from this situation is at a -20 modification.",
        FAILURE:
            "Your wits have deserted you.  You fail your maneuver.",
        PARTIAL_SUCCESS:
            "You achieve only a fraction of your goal before you are interrupted by a "
            "civil disturbance in which you are embroiled.  Spend 2d10 hours "
            "extricating yourself from this sticky situation before you attempt your "
            "maneuver again.",
        NEAR_SUCCESS:
            "You are almost successful, but you've hit that final wall so common in "
            "the urban environment... the greed of a functionary.  You may use an "
            "appropriate Influence skill to complete this task (bribery, etc.), or you "
            "may roll again after two rounds on this chart with a -10 modification.",
        SUCCESS:
            "You are a creature of the streets, my friend.  Your instincts serve you "
            "true, and you complete your task with alacrity.",
        ABSOLUTE_SUCCESS:
            "Your quick wits have gathered a new sheep into your fold.  You make a new "
            "contact who is kindly disposed towards you.  Your next transaction with "
            "them will have a +30 modifier in your favour for their reaction."
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 1.5, -20),
        ABSOLUTE_FAILURE: (-20, 1.2, -10),
        FAILURE: (0, 1.5, 0),
        PARTIAL_SUCCESS: (20, 0.8, 5),
        NEAR_SUCCESS: (80, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 1, 30)
    }

    @staticmethod
    def select_urban_table():
        """
        Set the current Urban maneuver table to use.
        :return: The maneuver table.
        """
        return UrbanManeuverTable()

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_type_to_skills = {
            UrbanManeuverTable.MANEUVER_CONTACTING:
                [SKILL_CONTACTING_SUBTERFUGE, ],
            UrbanManeuverTable.MANEUVER_MINGLING:
                [SKILL_MINGLING, SKILL_STALK_HIDE, SKILL_STREETWISE],
            UrbanManeuverTable.MANEUVER_SCROUNGING:
                [SKILL_SCROUNGING, SKILL_FORAGING],
            UrbanManeuverTable.MANEUVER_STREETWISE:
                [SKILL_STREETWISE, SKILL_MINGLING]
        }

        skills_list = maneuver_type_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
