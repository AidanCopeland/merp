# -*- coding: utf-8 -*-
"""
The Lore static maneuver table.

Classes:
    LoreManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
import trace_log as trace

sys.path.append('../')


class LoreManeuverTable(StaticManeuverTable):
    """
    Awareness/Perceptions static maneuver table.

    Methods:
        select_lore_table(maneuver_type)
    """
    MANEUVER_CULTURE_LORE = "Culture Lore"
    MANEUVER_FAUNA_LORE = "Fauna Lore"
    MANEUVER_FLORA_LORE = "Flora Lore"
    MANEUVER_HERALDRY = "Heraldry"
    MANEUVER_HISTORY = "History"
    MANEUVER_PHILOSOPHY = "Philosophy"
    MANEUVER_REGION_LORE = "Region Lore"
    MANEUVER_RELIGION = "Religion"
    MANEUVER_ARTIFACT_LORE = "Artifact Lore"
    MANEUVER_DIVINATION_LORE = "Divination Lore"
    MANEUVER_DREAM_LORE = "Dream Lore"
    MANEUVER_MAGICAL_LORE = "Magical Lore"
    MANEUVER_SPELL_LORE = "Spell Lore"
    MANEUVER_SYMBOL_LORE = "Symbol Lore"
    MANEUVER_UNDEAD_LORE = "Undead Lore"
    MANEUVER_WARDING_LORE = "Warding Lore"
    MANEUVER_DEMON_LORE = "Demon Lore"
    MANEUVER_DRAGON_LORE = "Dragon Lore"
    MANEUVER_FAERIE_LORE = "Faerie Lore"
    MANEUVER_HERB_LORE = "Herb Lore"
    MANEUVER_LOCK_LORE = "Lock Lore"
    MANEUVER_METAL_LORE = "Metal Lore"
    MANEUVER_POISON_LORE = "Poison Lore"
    MANEUVER_STONE_LORE = "Stone Lore"
    MANEUVER_TRADING_LORE = "Trading Lore"

    maneuver_type_options = (
        MANEUVER_CULTURE_LORE, MANEUVER_FAUNA_LORE, MANEUVER_FLORA_LORE,
        MANEUVER_HERALDRY, MANEUVER_HISTORY, MANEUVER_PHILOSOPHY, MANEUVER_REGION_LORE,
        MANEUVER_RELIGION, MANEUVER_ARTIFACT_LORE, MANEUVER_DIVINATION_LORE,
        MANEUVER_DREAM_LORE, MANEUVER_MAGICAL_LORE, MANEUVER_SPELL_LORE,
        MANEUVER_SYMBOL_LORE, MANEUVER_UNDEAD_LORE, MANEUVER_WARDING_LORE,
        MANEUVER_DEMON_LORE, MANEUVER_DRAGON_LORE, MANEUVER_FAERIE_LORE,
        MANEUVER_HERB_LORE, MANEUVER_LOCK_LORE, MANEUVER_METAL_LORE,
        MANEUVER_POISON_LORE, MANEUVER_STONE_LORE, MANEUVER_TRADING_LORE
    )

    maneuver_result_text = {
        BLUNDER:
            "Disaster!  If researching a topic, you have accidentally damaged or "
            "destroyed your study materials with the beverage you up-ended upon them!  "
            "Those materials that can be salvaged require a full day of careful "
            "tending, or they will be useless.  Regardless, they will offer a "
            "permanent -10 modification to future skill rolls which utilize them even if "
            "they are saved from destruction.  If you are attempting to remember a topic, "
            "you find your mind is blank.  Due to your mental block on the subject, you "
            "will suffer a -30 (non-cumulative) modification to all attempts to recall "
            "the subject until you achieve an _Absolute Success_ on this table.",
        ABSOLUTE_FAILURE:
            "What's all this?  If you are attempting to study a subject, you have gotten "
            "your topics confused, and you spend a full day just trying to sort out your "
            "references.  If attempting to recall a subject, you irretrievably confused "
            "yourself, and you cannot possibly recall this information without at least "
            "12 hours of study to refamiliarize yourself with the topic.",
        FAILURE:
            "Hmmm.  Nope.  Nothing springs to mind.  "
            "Perhaps if you were to spend another six hours studying the matter...",
        PARTIAL_SUCCESS:
            "You uncover/remember some of the details of the subject... but no specific "
            "ones.  Another hour of analysis might reveal some information, but for now, "
            "you have only the barest sketch of the topic as relates to your current "
            "search.  (If you were studying a topic, your research took 2 hours; if you "
            "were merely attempting to remember a fact, it took only a few moments, but "
            "the full analysis time will be required to refresh yourself on the "
            "information.",
        NEAR_SUCCESS:
            "It's hovering at the edge of your consciousness... can you afford to spend "
            "10 more minutes tracking it down?  If so, you may roll again at +10 to put "
            "the final pieces in place.  (If you were studying a topic, your research "
            "took 1 hour.)",
        SUCCESS:
            "Ah!  Of course!  You already knew where to look to find this information, "
            "so your research was done inside of 20 minutes.  A simple fact, of course, "
            "was right on the tip of your tongue.",
        ABSOLUTE_SUCCESS:
            "With a nonchalant air, you may relate the details of the topic from memory, "
            "including relevant quotations and analyses by authorities of note.  "
            "_Now_ who's the savant around here?"
    }

    maneuver_result_stats = {
        BLUNDER: (-100, 3, -30),
        ABSOLUTE_FAILURE: (-50, 2, -20),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (25, 1, 0),
        NEAR_SUCCESS: (75, 1.2, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.5, 30)
    }

    @staticmethod
    def select_lore_table(maneuver_type):
        """
        Set the current Lore maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.lore.spell_lore_maneuver_table import SpellLoreManeuverTable

        if maneuver_type == LoreManeuverTable.MANEUVER_SPELL_LORE:
            trace.flow("Spell Lore maneuver")
            trace.exit()
            return SpellLoreManeuverTable()
        else:
            return LoreManeuverTable()
